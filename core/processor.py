import os
import random
import subprocess
import json
import logging
import shutil
from typing import List, Optional, Tuple
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

logger = logging.getLogger("video_processor")

# Prefer system FFmpeg (e.g. /usr/bin/ffmpeg in Docker) which is compiled with libfreetype & full filters
system_ffmpeg = shutil.which("ffmpeg")
if system_ffmpeg and os.path.exists(system_ffmpeg):
    ffmpeg_bin = system_ffmpeg
else:
    try:
        ffmpeg_bin = imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        ffmpeg_bin = "ffmpeg"

logger.info(f"Using FFmpeg: {ffmpeg_bin}")

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
    {"name": "Electric Gold", "text": (255, 215, 0, 255), "bg": (11, 25, 44, 230), "border": (255, 215, 0, 255)},
    {"name": "Cyber Cyan", "text": (0, 240, 255, 255), "bg": (10, 25, 47, 230), "border": (0, 240, 255, 255)},
    {"name": "Neon Emerald", "text": (57, 255, 20, 255), "bg": (5, 46, 22, 230), "border": (57, 255, 20, 255)},
    {"name": "Blaze Orange", "text": (255, 107, 0, 255), "bg": (26, 11, 0, 230), "border": (255, 107, 0, 255)},
    {"name": "Royal Platinum", "text": (255, 255, 255, 255), "bg": (46, 16, 101, 230), "border": (255, 215, 0, 255)},
    {"name": "Solar Yellow", "text": (255, 238, 0, 255), "bg": (24, 24, 27, 230), "border": (255, 238, 0, 255)},
    {"name": "Neon Violet", "text": (224, 86, 253, 255), "bg": (19, 15, 64, 230), "border": (224, 86, 253, 255)},
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

def generate_title_card_image(
    title_text: str,
    output_png_path: str,
    width: int = 720,
    height: int = 1280
) -> bool:
    """Generate a crisp, centered, transparent PNG badge overlay for the starting title using Pillow."""
    try:
        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        palette = random.choice(TITLE_PALETTES)
        text_color = palette["text"]
        bg_color = palette["bg"]
        border_color = palette["border"]

        font_file = pick_font_file()
        font_size = 48
        font = None
        if font_file and os.path.exists(font_file):
            try:
                font = ImageFont.truetype(font_file, font_size)
            except Exception:
                pass
        if font is None:
            font = ImageFont.load_default()

        # Clean title text
        display_text = title_text.strip()
        if len(display_text) > 36:
            display_text = display_text[:33] + "..."

        bbox = draw.textbbox((0, 0), display_text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        cx = width // 2
        cy = height // 2
        pad_x = 36
        pad_y = 22

        box_left = max(24, cx - text_w // 2 - pad_x)
        box_top = cy - text_h // 2 - pad_y
        box_right = min(width - 24, cx + text_w // 2 + pad_x)
        box_bottom = cy + text_h // 2 + pad_y

        # Draw smooth rounded badge
        draw.rounded_rectangle(
            [box_left, box_top, box_right, box_bottom],
            radius=18,
            fill=bg_color,
            outline=border_color,
            width=3
        )

        # Draw centered text
        text_x = cx - text_w // 2
        text_y = cy - text_h // 2
        draw.text((text_x, text_y), display_text, font=font, fill=text_color)

        img.save(output_png_path, "PNG")
        logger.info(f"Generated title card PNG overlay: {output_png_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to generate title card PNG: {e}")
        return False

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
    progress_callback: Optional[callable] = None,
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

    def update_progress(pct: int, msg: str):
        if progress_callback:
            try:
                progress_callback(pct, msg)
            except Exception:
                pass

    num_clips = len(clip_paths)
    logger.info(f"Processing {num_clips} clips with target duration {target_duration}s")

    # Transition duration between clips
    trans_dur = 0.65 if num_clips > 1 else 0.0
    if num_clips > 1:
        dur_per_clip = (target_duration + (num_clips - 1) * trans_dur) / num_clips
    else:
        dur_per_clip = target_duration

    dur_per_clip = max(2.5, dur_per_clip)

    temp_dir = os.path.join(os.path.dirname(output_path), f"temp_render_{int(random.random()*100000)}")
    os.makedirs(temp_dir, exist_ok=True)
    temp_segments = []
    segment_durations = []

    try:
        # Step 1: Preprocess each clip individually to 720x1280 MP4
        # Single-pass scale+crop auto-rotates phone orientation and ensures lightweight memory consumption
        for i, clip_p in enumerate(clip_paths):
            pct_val = 55 + int((i / num_clips) * 30)
            update_progress(pct_val, f"Formatting clip {i+1} of {num_clips} (vertical 9:16)...")

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
                "-threads", "2",
                "-ss", f"{start_offset:.2f}",
                "-t", f"{actual_dur:.2f}",
                "-i", abs_clip,
                "-vf", vf,
                "-c:v", "libx264",
                "-preset", "ultrafast",
                "-tune", "fastdecode",
                "-crf", "23",
                "-an",
                seg_out
            ]

            res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
            if res.returncode != 0 or not os.path.exists(seg_out):
                err_snip = res.stderr[-300:].strip() if res.stderr else f"Exit code {res.returncode}"
                logger.error(f"Failed preprocessing clip #{i+1}: {err_snip}")
                return False, f"Failed processing clip #{i+1}: {err_snip}"
            
            measured_dur = get_media_duration(seg_out)
            if measured_dur <= 0.2:
                measured_dur = actual_dur
            segment_durations.append(measured_dur)
            temp_segments.append(seg_out)

        # Step 2: Build the unified composition filtergraph
        update_progress(88, "Applying smooth transitions & CEC badge...")
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
            actual_total_video_dur = segment_durations[0]
        else:
            curr_tag = "[0:v]"
            curr_len = segment_durations[0]
            for idx in range(1, len(temp_segments)):
                seg_dur = segment_durations[idx]
                t_dur = min(0.65, curr_len * 0.35, seg_dur * 0.35)
                offset = max(0.2, curr_len - t_dur)
                next_tag = f"[xf_{idx}]"
                filter_parts.append(
                    f"{curr_tag}[{idx}:v]xfade=transition={chosen_trans}:duration={t_dur:.2f}:offset={offset:.2f}{next_tag}"
                )
                curr_tag = next_tag
                curr_len = offset + seg_dur
            current_v = curr_tag
            actual_total_video_dur = curr_len

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

        # Overlay Title: Starting 5 seconds, BIGGER, BOLD, and COLOURFUL via Pillow PNG overlay
        has_title_overlay = False
        title_png = os.path.join(temp_dir, "title_card.png")
        if title_text and title_text.strip() and generate_title_card_image(title_text.strip(), title_png, width=output_width, height=output_height):
            inputs.extend(["-i", title_png])
            title_input_idx = next_input_idx
            next_input_idx += 1

            title_end = min(5.0, actual_total_video_dur - 0.5)
            if title_end > 1.0:
                filter_parts.append(
                    f"{current_v}[{title_input_idx}:v]overlay=0:0:enable='between(t,0.5,{title_end:.2f})'[v_titled]"
                )
                current_v = "[v_titled]"
                has_title_overlay = True

        # Mix Background Music with Fade-In & Fade-Out
        update_progress(93, "Mixing background study music...")
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
        final_cmd = [
            ffmpeg_bin, "-y",
            "-threads", "2",
        ] + inputs
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

        update_progress(96, "Finalizing high-definition reel encoding...")
        logger.info(f"Executing final composition ({actual_total_video_dur:.1f}s)...")
        res = subprocess.run(final_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)

        # Fallback 1: If xfade somehow fails, fall back to standard concat filter
        if res.returncode != 0 or not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            update_progress(97, "Finalizing with high-compatibility engine...")
            logger.warning("Primary composition failed, attempting concat filter fallback...")

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

            total_dur_fb = sum(segment_durations) if segment_durations else dur_per_clip * len(temp_segments)

            if has_title_overlay and os.path.exists(title_png):
                cmd_inputs.extend(["-i", title_png])
                title_end_fb = min(5.0, total_dur_fb - 0.5)
                filter_parts_fb.append(
                    f"{curr_v}[{fb_input_idx}:v]overlay=0:0:enable='between(t,0.5,{title_end_fb:.2f})'[v_titled]"
                )
                curr_v = "[v_titled]"
                fb_input_idx += 1

            fb_has_audio = False
            if music_path and os.path.exists(music_path):
                cmd_inputs.extend(["-i", os.path.abspath(music_path)])
                filter_parts_fb.append(
                    f"[{fb_input_idx}:a]atrim=0:{total_dur_fb:.2f},afade=t=in:ss=0:d=1.0,afade=t=out:st={max(1.0, total_dur_fb-2.0):.2f}:d=2.0,volume=0.9[a_out]"
                )
                fb_has_audio = True

            cmd_fb = [ffmpeg_bin, "-y", "-threads", "2"] + cmd_inputs + [
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

        # Fallback 2: Fail-safe minimal composition (guaranteed success)
        if res.returncode != 0 or not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            logger.warning("Attempting safe minimal composition...")
            update_progress(98, "Finalizing minimal reel composition...")
            cmd_safe = [ffmpeg_bin, "-y", "-threads", "2"]
            for s in temp_segments:
                cmd_safe.extend(["-i", os.path.abspath(s)])

            filter_safe = []
            concat_tags = "".join([f"[{k}:v]" for k in range(len(temp_segments))])
            filter_safe.append(f"{concat_tags}concat=n={len(temp_segments)}:v=1:a=0[v_safe]")
            safe_v = "[v_safe]"
            safe_idx = len(temp_segments)

            if logo_path and os.path.exists(logo_path):
                cmd_safe.extend(["-i", os.path.abspath(logo_path)])
                filter_safe.append(f"[{safe_idx}:v]scale={logo_scale_width}:-1[l_s];{safe_v}[l_s]overlay=main_w-overlay_w-24:24[v_with_logo]")
                safe_v = "[v_with_logo]"
                safe_idx += 1

            total_dur_safe = sum(segment_durations) if segment_durations else dur_per_clip * len(temp_segments)
            safe_has_audio = False
            if music_path and os.path.exists(music_path):
                cmd_safe.extend(["-i", os.path.abspath(music_path)])
                filter_safe.append(f"[{safe_idx}:a]atrim=0:{total_dur_safe:.2f},afade=t=in:ss=0:d=1.0,afade=t=out:st={max(1.0, total_dur_safe-2.0):.2f}:d=2.0,volume=0.9[a_safe]")
                safe_has_audio = True

            cmd_safe.extend(["-filter_complex", ";".join(filter_safe), "-map", safe_v])
            if safe_has_audio:
                cmd_safe.extend(["-map", "[a_safe]", "-c:a", "aac", "-b:a", "192k"])
            else:
                cmd_safe.append("-an")

            cmd_safe.extend([
                "-c:v", "libx264", "-preset", "ultrafast", "-crf", "22", "-pix_fmt", "yuv420p",
                "-t", f"{total_dur_safe:.2f}", "-movflags", "+faststart",
                os.path.abspath(output_path)
            ])
            res = subprocess.run(cmd_safe, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)

        if res.returncode != 0 or not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            err_snip = res.stderr[-600:].strip() if res.stderr else f"Exit code {res.returncode}"
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
