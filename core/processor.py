import os
import random
import subprocess
import json
import logging
import shutil
from typing import List, Optional, Tuple
import imageio_ffmpeg

logger = logging.getLogger("video_processor")

try:
    ffmpeg_bin = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
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

# Smooth transitions supported by xfade
TRANSITIONS = [
    "fade",          # Smooth cross-dissolve
    "wipeleft",      # Clean wipe left
    "wiperight",     # Clean wipe right
    "slideleft",     # Dynamic slide left
    "slideright",    # Dynamic slide right
    "smoothleft",    # Accelerated pan left
    "smoothright",   # Accelerated pan right
    "fadeblack",     # Cinematic dip to black
    "circlecrop",    # Circular iris transition
    "dissolve",      # Soft dissolve
]

# Colorful, bold title styles for the first 5 seconds
TITLE_PALETTES = [
    {"color": "0xFFD700", "box": "0x0B192C@0.85", "name": "Electric Gold"},
    {"color": "0x00F0FF", "box": "0x0A192F@0.85", "name": "Cyber Cyan"},
    {"color": "0x39FF14", "box": "0x052E16@0.88", "name": "Neon Emerald"},
    {"color": "0xFF6B00", "box": "0x1A0B00@0.85", "name": "Blaze Orange"},
    {"color": "0xFFFFFF", "box": "0x2E1065@0.88", "name": "Royal Platinum"},
    {"color": "0xFFEE00", "box": "0x18181B@0.88", "name": "Solar Yellow"},
    {"color": "0xE056FD", "box": "0x130F40@0.88", "name": "Neon Violet"},
]

def pick_font_file() -> Optional[str]:
    """Pick one of the bundled bold fonts, with fallback to system fonts."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fonts_dir = os.path.join(base_dir, "assets", "fonts")

    candidate_names = ["impact.ttf", "ariblk.ttf", "arialbd.ttf", "trebucbd.ttf", "font.ttf"]
    available = []
    if os.path.exists(fonts_dir):
        for c in candidate_names:
            p = os.path.join(fonts_dir, c)
            if os.path.exists(p):
                available.append(p)
    if available:
        return random.choice(available)

    # Fallbacks for Linux / Windows systems
    for sys_f in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/impact.ttf",
        "C:/Windows/Fonts/ariblk.ttf",
        "C:/Windows/Fonts/arialbd.ttf"
    ]:
        if os.path.exists(sys_f):
            return sys_f
    return None

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
    Merge clips into a seamless 30-40s vertical 9:16 video reel with smooth transitions.
    Guarantees:
      1. 100% ERECT (portrait) pose with proper iPhone/Android autorotation.
      2. Permanent CEC badge at top-right intact until the very end.
      3. Smooth randomized transitions (xfade) between clips.
      4. Bold, colorful, bigger starting 5-second title card with dynamic fonts & palettes.
      5. Uplifting competitive exam study background audio with smooth fade-in/out.
    """
    if not clip_paths:
        return False, "No clips provided."

    num_clips = len(clip_paths)
    logger.info(f"Processing {num_clips} clips with target duration {target_duration}s")

    # Transition duration between clips
    trans_dur = 0.70 if num_clips > 1 else 0.0
    if num_clips > 1:
        dur_per_clip = (target_duration + (num_clips - 1) * trans_dur) / num_clips
    else:
        dur_per_clip = target_duration

    dur_per_clip = max(2.5, dur_per_clip)

    temp_dir = os.path.join(os.path.dirname(output_path), f"temp_render_{int(random.random()*100000)}")
    os.makedirs(temp_dir, exist_ok=True)
    temp_segments = []

    try:
        # Step 1: Preprocess each clip individually to 720x1280 MP4
        # Single-pass scale+crop auto-rotates phone orientation and ensures lightweight memory consumption
        for i, clip_p in enumerate(clip_paths):
            abs_clip = os.path.abspath(clip_p)
            raw_dur = get_media_duration(abs_clip)
            actual_dur = min(dur_per_clip, raw_dur)
            start_offset = 0.5 if raw_dur > actual_dur + 1.2 else 0.0

            seg_out = os.path.join(temp_dir, f"seg_{i:03d}.mp4")

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
                err_snip = res.stderr[-300:].strip() if res.stderr else f"Exit code {res.returncode}"
                logger.error(f"Failed preprocessing clip #{i+1}: {err_snip}")
                return False, f"Failed processing clip #{i+1}: {err_snip}"
            temp_segments.append(seg_out)

        # Step 2: Build the unified composition filtergraph
        inputs = []
        for s in temp_segments:
            inputs.extend(["-i", os.path.abspath(s)])

        filter_parts = []
        next_input_idx = len(temp_segments)

        # Apply randomized smooth transition between clips
        chosen_trans = random.choice(TRANSITIONS)
        logger.info(f"Applying transition: {chosen_trans}")

        if len(temp_segments) == 1:
            current_v = "[0:v]"
            actual_total_video_dur = dur_per_clip
        else:
            curr_tag = "[0:v]"
            accum_offset = dur_per_clip
            for idx in range(1, len(temp_segments)):
                offset = max(0.5, accum_offset - trans_dur)
                next_tag = f"[xf_{idx}]"
                filter_parts.append(
                    f"{curr_tag}[{idx}:v]xfade=transition={chosen_trans}:duration={trans_dur:.2f}:offset={offset:.2f}{next_tag}"
                )
                curr_tag = next_tag
                accum_offset = offset + dur_per_clip
            current_v = curr_tag
            actual_total_video_dur = accum_offset

        # Overlay Logo: PERMANENT (intact from second 0 to the very end of video)
        if logo_path and os.path.exists(logo_path):
            abs_logo = os.path.abspath(logo_path)
            inputs.extend(["-i", abs_logo])
            logo_idx = next_input_idx
            next_input_idx += 1

            filter_parts.append(
                f"[{logo_idx}:v]scale={logo_scale_width}:-1[logo_scaled];"
                f"{current_v}[logo_scaled]overlay=main_w-overlay_w-24:24[v_with_logo]"
            )
            current_v = "[v_with_logo]"

        # Overlay Title: Starting 5 seconds, BIGGER (size 52), BOLD, and COLOURFUL
        if title_text and title_text.strip():
            clean_title = title_text.strip().replace(":", "\\:").replace("'", "").replace('"', "")
            palette = random.choice(TITLE_PALETTES)
            font_file = pick_font_file()
            font_arg = ""
            if font_file:
                safe_font = os.path.abspath(font_file).replace("\\", "/").replace(":", "\\:")
                font_arg = f":fontfile='{safe_font}'"

            # 5-second duration: 0.5s to 5.0s, fontsize=52, rich colored box with padding
            filter_parts.append(
                f"{current_v}drawtext=text='{clean_title}'{font_arg}:fontcolor={palette['color']}:fontsize=52:"
                f"box=1:boxcolor={palette['box']}:boxborderw=20:x=(w-text_w)/2:y=(h-text_h)/2:"
                f"enable='between(t,0.5,5.0)'[v_titled]"
            )
            current_v = "[v_titled]"

        # Mix Background Music with Fade-In & Fade-Out
        has_audio = False
        if music_path and os.path.exists(music_path):
            abs_music = os.path.abspath(music_path)
            inputs.extend(["-i", abs_music])
            music_idx = next_input_idx
            next_input_idx += 1

            fade_out_start = max(1.0, actual_total_video_dur - 2.0)
            filter_parts.append(
                f"[{music_idx}:a]atrim=0:{actual_total_video_dur:.2f},"
                f"afade=t=in:ss=0:d=1.0,"
                f"afade=t=out:st={fade_out_start:.2f}:d=2.0,"
                f"volume=0.9[a_out]"
            )
            has_audio = True

        # Build final command
        final_cmd = [ffmpeg_bin, "-y"] + inputs
        if filter_parts:
            final_cmd.extend(["-filter_complex", ";".join(filter_parts)])
            final_cmd.extend(["-map", current_v])
            if has_audio:
                final_cmd.extend(["-map", "[a_out]"])
        else:
            final_cmd.extend(["-map", "0:v"])

        final_cmd.extend([
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-crf", "22",
            "-pix_fmt", "yuv420p",
            "-metadata:s:v:0", "rotate=0",
            "-map_metadata", "-1",
        ])

        if has_audio:
            final_cmd.extend(["-c:a", "aac", "-b:a", "192k"])
        else:
            final_cmd.extend(["-an"])

        final_cmd.extend([
            "-t", f"{actual_total_video_dur:.2f}",
            "-movflags", "+faststart",
            os.path.abspath(output_path)
        ])

        logger.info(f"Executing final composition ({actual_total_video_dur:.1f}s)...")
        res = subprocess.run(final_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)

        # Fallback: If xfade somehow fails, fall back to standard concat filter
        if res.returncode != 0 or not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            logger.warning(f"xfade failed, attempting concat filter fallback...")

            filter_parts_fb = []
            concat_tags = "".join([f"[{k}:v]" for k in range(len(temp_segments))])
            filter_parts_fb.append(f"{concat_tags}concat=n={len(temp_segments)}:v=1:a=0[v_cat]")
            curr_v = "[v_cat]"

            fb_input_idx = len(temp_segments)
            cmd_inputs = []
            for s in temp_segments:
                cmd_inputs.extend(["-i", os.path.abspath(s)])

            if logo_path and os.path.exists(logo_path):
                cmd_inputs.extend(["-i", os.path.abspath(logo_path)])
                filter_parts_fb.append(
                    f"[{fb_input_idx}:v]scale={logo_scale_width}:-1[logo_s];"
                    f"{curr_v}[logo_s]overlay=main_w-overlay_w-24:24[v_logo]"
                )
                curr_v = "[v_logo]"
                fb_input_idx += 1

            if title_text and title_text.strip():
                clean_title = title_text.strip().replace(":", "\\:").replace("'", "").replace('"', "")
                font_file = pick_font_file()
                font_arg = f":fontfile='{os.path.abspath(font_file).replace('\\', '/').replace(':', '\\:')}'" if font_file else ""
                filter_parts_fb.append(
                    f"{curr_v}drawtext=text='{clean_title}'{font_arg}:fontcolor=0xFFD700:fontsize=52:"
                    f"box=1:boxcolor=0x0B192C@0.85:boxborderw=20:x=(w-text_w)/2:y=(h-text_h)/2:"
                    f"enable='between(t,0.5,5.0)'[v_titled]"
                )
                curr_v = "[v_titled]"

            fb_has_audio = False
            total_dur_fb = dur_per_clip * len(temp_segments)
            if music_path and os.path.exists(music_path):
                cmd_inputs.extend(["-i", os.path.abspath(music_path)])
                filter_parts_fb.append(
                    f"[{fb_input_idx}:a]atrim=0:{total_dur_fb:.2f},afade=t=in:ss=0:d=1.0,afade=t=out:st={total_dur_fb-2.0:.2f}:d=2.0,volume=0.9[a_out]"
                )
                fb_has_audio = True

            cmd_fb = [ffmpeg_bin, "-y"] + cmd_inputs + [
                "-filter_complex", ";".join(filter_parts_fb),
                "-map", curr_v,
            ]
            if fb_has_audio:
                cmd_fb.extend(["-map", "[a_out]", "-c:a", "aac", "-b:a", "192k"])
            else:
                cmd_fb.append("-an")

            cmd_fb.extend([
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22", "-pix_fmt", "yuv420p",
                "-metadata:s:v:0", "rotate=0", "-map_metadata", "-1",
                "-t", f"{total_dur_fb:.2f}", "-movflags", "+faststart",
                os.path.abspath(output_path)
            ])
            res = subprocess.run(cmd_fb, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)

        if res.returncode != 0 or not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            err_snip = res.stderr[-300:].strip() if res.stderr else f"Exit code {res.returncode}"
            logger.error(f"FFmpeg composition error: {err_snip}")
            return False, f"FFmpeg failed: {err_snip}"

        return True, "Video generated successfully!"

    except Exception as e:
        logger.exception("Error during video processing")
        return False, str(e)
    finally:
        # Cleanup temporary preprocessed segments and directory
        try:
            for s in temp_segments:
                if os.path.exists(s):
                    os.remove(s)
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)
        except Exception:
            pass
