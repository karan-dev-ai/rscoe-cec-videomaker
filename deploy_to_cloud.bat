@echo off
title Deploy CEC Video Maker to 24/7 Cloud (Hugging Face)
color 0A
cls

echo ======================================================================
echo   Deploy CEC Video Maker to 24/7 Cloud (Free Hugging Face Space)
echo ======================================================================
echo.
echo This script connects your Video Maker to Hugging Face Spaces so it
echo stays online 24/7 without needing your laptop to be open!
echo.
echo Step 1: Create a free Space on https://huggingface.co/new-space
echo   - Name: rscoe-cec-videomaker
echo   - SDK: Docker (Blank)
echo   - Visibility: Public
echo.
echo Step 2: Paste your Space Git Repository URL below
echo   (Example: https://huggingface.co/spaces/YourUsername/rscoe-cec-videomaker)
echo.
set /p SPACE_URL="Enter your Space Git URL: "

if "%SPACE_URL%"=="" (
    echo [ERROR] No URL provided. Exiting.
    pause
    exit /b 1
)

echo.
echo [1/4] Checking Git repository...
if not exist .git (
    git init
    git branch -M main
)

echo [2/4] Staging files...
git add .

echo [3/4] Creating deployment commit...
git commit -m "Deploy RSCOE CEC Video Maker 24/7"

echo [4/4] Setting remote and pushing to Hugging Face...
git remote remove origin >nul 2>&1
git remote add origin %SPACE_URL%

echo.
echo Pushing code to Hugging Face...
echo (If prompted, enter your Hugging Face username and Access Token as password)
echo.
git push -u origin main --force

echo.
echo ======================================================================
echo  Done! Your Space is building on Hugging Face.
echo  Within 2-3 minutes, your permanent link will be LIVE:
echo  Check your Space page on Hugging Face to get your public HTTPS link!
echo ======================================================================
pause
