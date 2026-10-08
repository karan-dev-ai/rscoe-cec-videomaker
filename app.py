import os
import uuid
import time
import shutil
import logging
import json
from typing import List, Optional
import threading
from concurrent.futures import ThreadPoolExecutor

from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from core.processor import process_video_reel, pick_music_track, get_media_duration
from core.quiz_bank import get_random_quiz_set

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("app")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
LOGO_PATH = os.path.join(ASSETS_DIR, "logo", "club_logo.png")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")
UPLOADS_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

app = FastAPI(title="RSCOE CEC Video Maker")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
app.mount("/assets", StaticFiles(directory=ASSETS_DIR), name="assets")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Thread pool for video processing
executor = ThreadPoolExecutor(max_workers=2)

# In-memory job tracker
# job_id -> { "status": "...", "progress": int, "step": str, "clips": [], "output_url": str, "error": str, "created_at": float }
JOBS = {}
LAST_PLAYED_MUSIC = None
jobs_lock = threading.Lock()

def save_job_state(job_id: str):
    job = JOBS.get(job_id)
    if not job:
        return
    job_dir = os.path.join(UPLOADS_DIR, job_id)
    os.makedirs(job_dir, exist_ok=True)
    json_path = os.path.join(job_dir, "job.json")
    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(job, f)
    except Exception as e:
        logger.warning(f"Error saving job state for {job_id}: {e}")

def load_job_state(job_id: str):
    if job_id in JOBS:
        return JOBS[job_id]
    json_path = os.path.join(UPLOADS_DIR, job_id, "job.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                JOBS[job_id] = data
                return data
        except Exception as e:
            logger.warning(f"Error loading job state for {job_id}: {e}")
    return None

def cleanup_old_files():
    """Remove uploads and outputs older than 24 hours to preserve disk space."""
    now = time.time()
    cutoff = now - 24 * 3600
    for folder in [UPLOADS_DIR, OUTPUTS_DIR]:
        if not os.path.exists(folder):
            continue
        for fname in os.listdir(folder):
            fpath = os.path.join(folder, fname)
            try:
                if os.path.isfile(fpath) and os.path.getmtime(fpath) < cutoff:
                    os.remove(fpath)
                elif os.path.isdir(fpath) and os.path.getmtime(fpath) < cutoff:
                    shutil.rmtree(fpath, ignore_errors=True)
            except Exception as e:
                logger.warning(f"Cleanup error for {fpath}: {e}")

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    cleanup_old_files()
    songs = []
    if os.path.exists(MUSIC_DIR):
        for f in os.listdir(MUSIC_DIR):
            if f.lower().endswith((".mp3", ".wav", ".m4a", ".aac")):
                songs.append(f)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"songs": sorted(songs), "has_logo": os.path.exists(LOGO_PATH)}
    )

@app.get("/api/songs")
async def get_songs():
    songs = []
    if os.path.exists(MUSIC_DIR):
        for f in sorted(os.listdir(MUSIC_DIR)):
            if f.lower().endswith((".mp3", ".wav", ".m4a", ".aac")):
                songs.append({
                    "filename": f,
                    "title": f.replace("CEC_", "").replace("_", " ").replace(".mp3", "").title(),
                    "url": f"/assets/music/{f}"
                })
    return {"songs": songs}

@app.post("/api/songs/upload")
async def upload_song(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".mp3", ".wav", ".m4a", ".aac")):
        raise HTTPException(status_code=400, detail="Invalid audio file type.")
    dest_path = os.path.join(MUSIC_DIR, file.filename)
    with open(dest_path, "wb") as f:
        while chunk := await file.read(1024 * 1024):
            f.write(chunk)
    return {"status": "ok", "filename": file.filename}

# Step 1 of robust upload: Create Job Session
@app.post("/api/jobs/create")
async def create_job_session():
    job_id = str(uuid.uuid4())
    job_upload_dir = os.path.join(UPLOADS_DIR, job_id)
    os.makedirs(job_upload_dir, exist_ok=True)

    JOBS[job_id] = {
        "status": "uploading",
        "progress": 5,
        "step": "Session initialized",
        "clips": [],
        "created_at": time.time(),
    }
    save_job_state(job_id)
    logger.info(f"Initialized job session {job_id}")
    return {"job_id": job_id}

# Step 2 of robust upload: Upload individual clip (handles large files smoothly)
@app.post("/api/jobs/{job_id}/upload_clip")
async def upload_clip(
    job_id: str,
    clip_index: int = Form(...),
    clip: UploadFile = File(...)
):
    job = load_job_state(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job session expired or not found.")

    job_upload_dir = os.path.join(UPLOADS_DIR, job_id)
    ext = os.path.splitext(clip.filename)[1] or ".mp4"
    save_path = os.path.join(job_upload_dir, f"clip_{clip_index:03d}{ext}")

    try:
        with open(save_path, "wb") as f:
            while chunk := await clip.read(1024 * 1024): # 1MB chunked read
                f.write(chunk)

        # Record clip path safely
        with jobs_lock:
            clips_list = JOBS[job_id]["clips"]
            while len(clips_list) <= clip_index:
                clips_list.append(None)
            clips_list[clip_index] = save_path
            save_job_state(job_id)

        logger.info(f"Job {job_id}: Saved clip #{clip_index} ({clip.filename}) -> {os.path.getsize(save_path)} bytes")
        return {
            "status": "ok",
            "clip_index": clip_index,
            "filename": clip.filename,
            "size": os.path.getsize(save_path)
        }
    except Exception as e:
        logger.error(f"Error saving clip #{clip_index} for job {job_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed saving clip #{clip_index}: {str(e)}")

def run_video_job(job_id: str, clip_paths: List[str], target_duration: float, title_text: Optional[str], music_choice: Optional[str]):
    global LAST_PLAYED_MUSIC
    try:
        JOBS[job_id]["status"] = "processing"
        JOBS[job_id]["step"] = "Preparing study soundtrack..."
        JOBS[job_id]["progress"] = 52
        save_job_state(job_id)

        # Determine music
        if music_choice and music_choice != "random":
            chosen_music = os.path.join(MUSIC_DIR, music_choice)
            if not os.path.exists(chosen_music):
                chosen_music = pick_music_track(MUSIC_DIR, LAST_PLAYED_MUSIC)
        else:
            chosen_music = pick_music_track(MUSIC_DIR, LAST_PLAYED_MUSIC)

        if chosen_music:
            LAST_PLAYED_MUSIC = chosen_music
            music_name = os.path.basename(chosen_music).replace("CEC_", "").replace("_", " ").replace(".mp3", "").title()
            JOBS[job_id]["music_used"] = music_name
        else:
            JOBS[job_id]["music_used"] = "None"

        output_filename = f"cec_video_{int(time.time())}_{job_id[:6]}.mp4"
        output_filepath = os.path.join(OUTPUTS_DIR, output_filename)

        def on_processor_progress(pct: int, msg: str):
            if job_id in JOBS:
                JOBS[job_id]["progress"] = pct
                JOBS[job_id]["step"] = msg
                save_job_state(job_id)

        JOBS[job_id]["step"] = f"Optimizing {len(clip_paths)} clips for vertical reel..."
        JOBS[job_id]["progress"] = 55
        save_job_state(job_id)

        ok, msg = process_video_reel(
            clip_paths=clip_paths,
            output_path=output_filepath,
            logo_path=LOGO_PATH if os.path.exists(LOGO_PATH) else None,
            music_path=chosen_music,
            target_duration=target_duration,
            title_text=title_text,
            progress_callback=on_processor_progress
        )

        if not ok:
            JOBS[job_id]["status"] = "failed"
            JOBS[job_id]["error"] = msg
            save_job_state(job_id)
            logger.error(f"Job {job_id} failed: {msg}")
            return

        JOBS[job_id]["status"] = "completed"
        JOBS[job_id]["progress"] = 100
        JOBS[job_id]["step"] = "Done!"
        JOBS[job_id]["output_file"] = output_filename
        JOBS[job_id]["output_url"] = f"/api/download/{output_filename}"
        save_job_state(job_id)
        logger.info(f"Job {job_id} completed successfully: {output_filename}")

    except Exception as e:
        logger.exception(f"Unhandled error in job {job_id}")
        JOBS[job_id]["status"] = "failed"
        JOBS[job_id]["error"] = str(e)
        save_job_state(job_id)

# Step 3: Trigger generation once clips are uploaded
@app.post("/api/jobs/{job_id}/start")
async def start_job(
    job_id: str,
    target_duration: float = Form(35.0),
    title_text: Optional[str] = Form(""),
    music_choice: Optional[str] = Form("random")
):
    job = load_job_state(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job session not found.")

    raw_clips = job.get("clips", [])
    valid_clips = [c for c in raw_clips if c and os.path.exists(c)]

    if len(valid_clips) < 2:
        raise HTTPException(status_code=400, detail=f"Expected at least 2 clips, found {len(valid_clips)}.")

    JOBS[job_id]["status"] = "processing"
    JOBS[job_id]["progress"] = 50
    JOBS[job_id]["step"] = f"All {len(valid_clips)} clips received! Starting video render..."
    save_job_state(job_id)

    executor.submit(
        run_video_job,
        job_id,
        valid_clips,
        target_duration,
        title_text,
        music_choice
    )

    return {"status": "started", "job_id": job_id}

@app.get("/api/job/{job_id}")
async def get_job_status(job_id: str):
    job = load_job_state(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found.")
    return job

@app.get("/api/debug/jobs")
async def debug_jobs():
    return {"jobs": JOBS}

@app.get("/api/quiz/questions")
async def get_quiz_questions():
    """Return 5 randomized authentic competitive exam PYQs (UPSC, MPSC, CDS, AFCAT)."""
    return {"questions": get_random_quiz_set(5)}

@app.get("/api/download/{filename}")
async def download_video(filename: str):
    file_path = os.path.join(OUTPUTS_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(
        file_path,
        media_type="video/mp4",
        filename=filename,
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

@app.get("/api/stream/{filename}")
async def stream_video(filename: str):
    file_path = os.path.join(OUTPUTS_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found.")
    return FileResponse(file_path, media_type="video/mp4")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run("app:app", host="0.0.0.0", port=port)

