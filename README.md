---
title: RSCOE CEC Video Maker
emoji: 🎬
colorFrom: green
colorTo: emerald
sdk: docker
app_port: 7860
pinned: false
---

# 🎬 CEC RSCOE • 1-Click Daily Video Maker

An automated, one-click video generator built specifically for **Competitive Exam Cell (CEC) RSCOE**.

Every day, whichever club member is on duty can simply open the link on their phone or laptop, upload 6–7 study session clips, and download a finished 30–40 second vertical reel ready for WhatsApp Status, Instagram Reels, and YouTube Shorts.

---

## ☁️ 24/7 Cloud Deployment (No Laptop Required!)

To give all club members a permanent public link that works **24/7 without needing anyone's laptop or script running**, deploy this project to **Hugging Face Spaces** (100% Free, No credit card needed).

### Quick 2-Minute Setup on Hugging Face:
1. Go to [huggingface.co](https://huggingface.co) and create a free account (or log in).
2. Click **New Space** (or go to `huggingface.co/new-space`).
3. Set:
   - **Space name**: `rscoe-cec-videomaker`
   - **License**: `mit` or `openrail`
   - **Space SDK**: Select **Docker** -> **Blank**
   - **Space Hardware**: **Free (2 vCPU · 16 GB RAM)**
   - **Visibility**: **Public**
4. Click **Create Space**.
5. Push this codebase using Git (or run the provided `deploy_to_cloud.bat`):
   ```bash
   git init
   git add .
   git commit -m "Deploy RSCOE CEC Video Maker"
   git remote add origin https://huggingface.co/spaces/<your-username>/rscoe-cec-videomaker
   git push -u origin main
   ```
6. Hugging Face will automatically build the Docker container and give you a permanent URL:
   👉 **`https://<your-username>-rscoe-cec-videomaker.hf.space`**
   Share this permanent URL in the club WhatsApp group — it will stay online 24/7!

---

## ⚡ Local Run (Optional)

If you ever want to test or run it locally on your PC:
Double-click `start.bat` or run:
```powershell
python run_server.py
```

---

## 🌟 Features

1. **Strict 100% Upright 9:16 Vertical Reel**: Automatically centers and formats iPhone and Android clips in upright portrait mode with zero tilting.
2. **Club Badge Overlay**: The official **CEC RSCOE** badge is permanently positioned at the **top-right** corner throughout the video.
3. **15+ Motivational Exam Study Tracks**: Randomly mixes uplifting, motivational exam study instrumentals (or select your favorite).
4. **Session Topic Title (Optional)**: If you enter a topic (e.g. `DLS : APTITUDE` or `DLS : ENGLISH`), it places a clean title overlay on the first clip.
5. **Instant Download & Mobile Share**: Video plays directly in the browser with a 1-tap download button.

---

## 📁 Project Structure

```
VideoMaker/
├── assets/
│   ├── logo/
│   │   └── club_logo.png         # Official CEC RSCOE badge (512x512 transparent PNG)
│   └── music/                    # 15 motivational study & focus tracks
├── core/
│   └── processor.py              # Upright portrait FFmpeg video engine
├── templates/
│   └── index.html                # Mobile-first responsive web UI
├── static/
│   ├── css/style.css
│   └── js/app.js
├── uploads/                      # Auto-cleaned temporary uploads
├── outputs/                      # Generated videos
├── app.py                        # FastAPI backend
├── Dockerfile                    # Cloud container configuration (24/7 hosting)
├── deploy_to_cloud.bat           # 1-click cloud push helper
├── run_server.py                 # Local server + Cloudflare tunnel launcher
└── requirements.txt
```
