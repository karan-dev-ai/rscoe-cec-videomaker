import os
import sys
import re
import time
import subprocess
import threading
import socket
import uvicorn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUDFLARED_EXE = os.path.join(BASE_DIR, "cloudflared.exe")

def get_local_ip():
    """Get LAN IP address for local Wi-Fi testing."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def start_uvicorn(port=8000):
    uvicorn.run("app:app", host="0.0.0.0", port=port, log_level="warning")

def monitor_tunnel(proc):
    """Monitor cloudflared tunnel logs and extract the public trycloudflare.com URL."""
    url_pattern = re.compile(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com")
    found_url = False

    for line in iter(proc.stderr.readline, ""):
        if not line:
            break
        match = url_pattern.search(line)
        if match and not found_url:
            public_url = match.group(0)
            found_url = True
            print("\n" + "═" * 74)
            print("  🌟 PUBLIC LINK READY FOR ALL CLUB MEMBERS! 🌟")
            print("═" * 74)
            print(f"  👉  {public_url}")
            print("═" * 74)
            print("  📱 Share this link on WhatsApp! Any member on phone or laptop")
            print("     can open it, upload today's clips, and get the video in 1 click.")
            print("═" * 74 + "\n")

def main():
    port = 8000
    local_ip = get_local_ip()

    print("\n" + "═" * 74)
    print(" 🚀 STARTING CEC RSCOE 1-CLICK VIDEO MAKER...")
    print("═" * 74)
    print(f" • Local PC link:    http://localhost:{port}")
    print(f" • Local Wi-Fi link: http://{local_ip}:{port}")
    print(" • Starting secure public tunnel for club members...")
    print("═" * 74)

    # 1. Start FastAPI server in background thread
    server_thread = threading.Thread(target=start_uvicorn, args=(port,), daemon=True)
    server_thread.start()
    time.sleep(1.0)

    # 2. Start Cloudflare Tunnel
    tunnel_proc = None
    if os.path.exists(CLOUDFLARED_EXE):
        cmd = [CLOUDFLARED_EXE, "tunnel", "--url", f"http://127.0.0.1:{port}"]
        try:
            tunnel_proc = subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
                errors="replace",
                bufsize=1
            )
            # Monitor in thread
            t_thread = threading.Thread(target=monitor_tunnel, args=(tunnel_proc,), daemon=True)
            t_thread.start()
        except Exception as e:
            print(f"Notice: Could not start cloudflared tunnel: {e}")

    print("\nPress Ctrl+C anytime to stop.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping Video Maker server...")
        if tunnel_proc:
            tunnel_proc.terminate()
        sys.exit(0)

if __name__ == "__main__":
    main()
