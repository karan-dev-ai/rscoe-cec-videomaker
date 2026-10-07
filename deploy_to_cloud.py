"""
Deploy CEC Video Maker to 24/7 Cloud (Hugging Face Spaces)
"""
import os
import subprocess
import sys

def run_cmd(cmd):
    print(f">> {cmd}")
    res = subprocess.run(cmd, shell=True)
    if res.returncode != 0:
        print(f"Warning/Error running: {cmd}")
    return res.returncode

def main():
    print("=" * 70)
    print("  🚀 DEPLOY CEC VIDEO MAKER TO 24/7 CLOUD (HUGGING FACE SPACES)")
    print("=" * 70)
    print("\nThis deploys your app to Hugging Face Spaces for 100% FREE 24/7 hosting.")
    print("No credit card required. Once deployed, anyone in your club can use the link")
    print("even when your laptop is completely turned off!\n")
    print("Instructions:")
    print("1. Go to https://huggingface.co/new-space")
    print("2. Enter Space Name: rscoe-cec-videomaker")
    print("3. Space SDK: Select 'Docker' -> 'Blank'")
    print("4. Visibility: 'Public'")
    print("5. Click 'Create Space'")
    print("-" * 70)

    url = input("\nEnter your Hugging Face Space Git URL\n(e.g. https://huggingface.co/spaces/USERNAME/rscoe-cec-videomaker): ").strip()
    if not url:
        print("No URL provided. Exiting.")
        sys.exit(1)

    print("\n[1/4] Initializing Git...")
    if not os.path.exists(".git"):
        run_cmd("git init")
        run_cmd("git branch -M main")

    print("\n[2/4] Staging files (excluding large sample videos)...")
    run_cmd("git add .")

    print("\n[3/4] Committing changes...")
    run_cmd('git commit -m "Deploy RSCOE CEC Video Maker 24/7"')

    print("\n[4/4] Setting remote and pushing to Hugging Face...")
    run_cmd("git remote remove origin")
    run_cmd(f"git remote add origin {url}")
    print("\nPushing to Hugging Face...")
    print("Note: If prompted for password, use your Hugging Face Access Token (from huggingface.co/settings/tokens with write permission).")
    run_cmd("git push -u origin main --force")

    print("\n" + "=" * 70)
    print("🎉 DEPLOYMENT STARTED!")
    print("Visit your space on Hugging Face to see the live build.")
    print("In ~2 minutes, your permanent standalone 24/7 link will be online!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
