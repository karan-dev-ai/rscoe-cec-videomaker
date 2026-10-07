import os
import random
import subprocess
import json
import logging
from typing import List, Optional, Tuple
import imageio_ffmpeg

try:
    ffmpeg_bin = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    import shutil
    ffmpeg_bin = shutil.which("ffmpeg") or "ffmpeg"

def get_media_duration(file_path: str) -> float:
    """Get the duration of a video or audio file using ffmpeg."""
    try:
        cmd = [ffmpeg_bin, "-i", file_path]
        res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="replace")
        for line in res.stderr.splitlines():
            if "Duration:" in line:
                parts = line.strip().split(",")[0].split("Duration:")[1].strip()
                h, m, s = parts.split(":")
                dur = float(h) * 3600 + float(m) * 60 + float(s)
                if dur > 0.1:
                    return dur
    except Exception as e:
        logger.error(f"Error getting duration for {file_path}: {e}")
    return 5.0

def pick_music_track(music_dir: str, last_played_file: Optional[str] = None) -> Optional[str]:
    """Pick a random track from the music directory, avoiding consecutive repeats."""
    if not os.path.exists(music_dir):
        return None
    valid_extensions = (".mp3", ".wav", ".m4a", ".aac", ".ogg")
    tracks = [
        os.path.join(music_dir, f)
        for f in os.listdir(music_dir)
        if f.lower().endswith(valid_extensions)
    ]
    if not tracks:
        return None
    if len(tracks) > 1 and last_played_file:
        available = [t for t in tracks if os.path.basename(t) != os.path.basename(last_played_file)]
        if available:
            return random.choice(available)
    return random.choice(tracks)

def process_video_reel(
    clip_paths: List[str],
    output_path: str,
    logo_path: Optional[str] = None,
    music_path: Optional[str] = None,
    target_duration: float = 35.0,
    title_text: Optional[str] = None,
    output_width: int = 720,
    output_height: int = 1280,
    logo_scale_width: int = 190,
) -> Tuple[bool, str]:
    """
    Merge clips into a seamless 30-40s vertical 9:16 video reel.
    Guarantees 100% ERECT (portrait) pose with proper iPhone/Android autorotation.
    Overlays the club logo in the top-right corner.
    Mixes competitive exam study background music with smooth fade-in and fade-out.
    """
    if not clip_paths:
        return False, "No clips provided."

    num_clips = len(clip_paths)
    logger.info(f"Processing {num_clips} clips with target duration {target_duration}s")

    dur_per_clip = max(2.0, target_duration / num_clips)
    temp_dir = os.path.join(os.path.dirname(output_path), f"temp_render_{int(random.random()*100000)}")
    os.makedirs(temp_dir, exist_ok=True)
    temp_segments = []

    try:
        # Phase 1: Preprocess each clip individually using simple -vf
        # In FFmpeg, simple -vf AUTOMATICALLY handles iPhone/Android rotation metadata (displaymatrix/rotate)
        # ensuring the decoded frames are physically upright/erect 720x1280 vertical video.
        for i, clip_p in enumerate(clip_paths):
            abs_clip = os.path.abspath(clip_p)
            raw_dur = get_media_duration(abs_clip)
            actual_dur = min(dur_per_clip, raw_dur)
            start_offset = 0.5 if raw_dur > actual_dur + 1.2 else 0.0

            seg_out = os.path.join(temp_dir, f"seg_{i:03d}.ts")

            # Simple -vf pipeline with automatic autorotation
            vf = (
                f"scale={output_width}:{output_height}:force_original_aspect_ratio=increase,"
                f"crop={output_width}:{output_height},"
                f"setsar=1,fps=30,format=yuv420p"
            )

            cmd = [
                ffmpeg_bin, "-y",
                "-ss", f"{start_offset:.2f}",
                "-t", f"{actual_dur:.2f}",
                "-i", abs_clip,
                "-vf", vf,
                "-c:v", "libx264",
                "-preset", "ultrafast",
                "-crf", "20",
                "-an",
                seg_out
            ]

            res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
            if res.returncode != 0 or not os.path.exists(seg_out):
                logger.error(f"Failed preprocessing clip #{i+1}: {res.stderr}")
                return False, f"Failed processing clip #{i+1}"
            temp_segments.append(seg_out)

        # Phase 2: Concatenate all upright segments
        concat_list_file = os.path.join(temp_dir, "concat_list.txt")
        with open(concat_list_file, "w") as f:
            for seg in temp_segments:
                safe_path = os.path.abspath(seg).replace("\\", "/")
                f.write(f"file '{safe_path}'\n")

        merged_raw = os.path.join(temp_dir, "merged_upright.mp4")
        concat_cmd = [
            ffmpeg_bin, "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", concat_list_file,
            "-c", "copy",
            merged_raw
        ]
        res = subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0 or not os.path.exists(merged_raw):
            return False, f"Failed concatenating upright clips: {res.stderr}"

        total_actual_dur = get_media_duration(merged_raw)

        # Phase 3: Final Composite (Add Logo, optional Title, and Background Music)
        inputs = ["-i", merged_raw]
        filter_parts = []
        current_v = "[0:v]"
        next_input_idx = 1

        # Logo overlay (Top Right)
        if logo_path and os.path.exists(logo_path):
            abs_logo = os.path.abspath(logo_path)
            inputs.extend(["-i", abs_logo])
            logo_idx = next_input_idx
            next_input_idx += 1

            filter_parts.append(
                f"[{logo_idx}:v]scale={logo_scale_width}:-1[logo_scaled];"
                f"{current_v}[logo_scaled]overlay=main_w-overlay_w-20:20[v_logo]"
            )
            current_v = "[v_logo]"

        # Optional Title overlay on the first 3.5 seconds
        if title_text and title_text.strip():
            clean_title = title_text.strip().replace(":", "\\:").replace("'", "").replace('"', "")
            font_opt = ""
            if os.path.exists("C:/Windows/Fonts/arialbd.ttf"):
                font_opt = ":fontfile='C\\:/Windows/Fonts/arialbd.ttf'"
            elif os.path.exists("C:/Windows/Fonts/arial.ttf"):
                font_opt = ":fontfile='C\\:/Windows/Fonts/arial.ttf'"

            filter_parts.append(
                f"{current_v}drawtext=text='{clean_title}'{font_opt}:fontcolor=white:fontsize=36:"
                f"box=1:boxcolor=black@0.65:boxborderw=16:x=(w-text_w)/2:y=(h-text_h)/2:"
                f"enable='between(t,0.5,4.0)'[v_titled]"
            )
            current_v = "[v_titled]"

        # Background Music
        has_custom_audio = False
        if music_path and os.path.exists(music_path):
            abs_music = os.path.abspath(music_path)
            inputs.extend(["-i", abs_music])
            music_idx = next_input_idx
            next_input_idx += 1

            fade_out_start = max(1.0, total_actual_dur - 2.0)
            filter_parts.append(
                f"[{music_idx}:a]atrim=0:{total_actual_dur:.2f},"
                f"afade=t=in:ss=0:d=1.0,"
                f"afade=t=out:st={fade_out_start:.2f}:d=2.0,"
                f"volume=0.9[a_out]"
            )
            has_custom_audio = True

        final_cmd = [ffmpeg_bin, "-y"] + inputs
        if filter_parts:
            final_cmd.extend(["-filter_complex", ";".join(filter_parts)])
            final_cmd.extend(["-map", current_v])
            if has_custom_audio:
                final_cmd.extend(["-map", "[a_out]"])
        else:
            final_cmd.extend(["-map", "0:v"])

        final_cmd.extend([
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "21",
            "-pix_fmt", "yuv420p",
            "-metadata:s:v:0", "rotate=0",  # EXPLICITLY reset rotation metadata to zero
            "-map_metadata", "-1",           # Strip any inherited rotation matrix side-data
        ])

        if has_custom_audio:
            final_cmd.extend(["-c:a", "aac", "-b:a", "192k"])
        else:
            final_cmd.extend(["-an"])

        final_cmd.extend([
            "-t", f"{total_actual_dur:.2f}",
            "-movflags", "+faststart",
            os.path.abspath(output_path)
        ])

        logger.info("Executing final composition...")
        res = subprocess.run(final_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0 or not os.path.exists(output_path):
            logger.error(f"FFmpeg error: {res.stderr}")
            return False, f"FFmpeg failed: {res.stderr[-500:] if res.stderr else 'Unknown error'}"

        return True, "Video generated successfully!"

    except Exception as e:
        logger.exception("Error during video processing")
        return False, str(e)
    finally:
        # Cleanup temporary directory
        try:
            for s in temp_segments:
                if os.path.exists(s):
                    os.remove(s)
            if os.path.exists(os.path.join(temp_dir, "concat_list.txt")):
                os.remove(os.path.join(temp_dir, "concat_list.txt"))
            if os.path.exists(os.path.join(temp_dir, "merged_upright.mp4")):
                os.remove(os.path.join(temp_dir, "merged_upright.mp4"))
            if os.path.exists(temp_dir):
                os.rmdir(temp_dir)
        except Exception:
            pass
