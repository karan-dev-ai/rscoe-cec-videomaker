@echo off
title Push CEC Video Maker to GitHub
color 0B
cls

echo ======================================================================
echo   Push CEC Video Maker to GitHub (for 24/7 Free Cloud Hosting)
echo ======================================================================
echo.
echo Step 1: Create a new repository on https://github.com/new
echo   - Name: rscoe-cec-videomaker
echo   - Choose: Public or Private
echo   - DO NOT check "Add a README" or ".gitignore" (already created)
echo   - Click "Create repository"
echo.
echo Step 2: Copy your GitHub repository URL
echo   (Example: https://github.com/YourUsername/rscoe-cec-videomaker.git)
echo.
set /p REPO_URL="Enter your GitHub Repository URL: "

if "%REPO_URL%"=="" (
    echo [ERROR] No URL provided. Exiting.
    pause
    exit /b 1
)

echo.
echo [1/3] Adding files to Git...
git add .
git commit -m "Update for 24/7 cloud hosting on Render" >nul 2>&1

echo [2/3] Setting remote...
git remote remove origin >nul 2>&1
git remote add origin %REPO_URL%

echo [3/3] Pushing to GitHub...
echo (If prompted by GitHub, sign in to authorize)
echo.
git push -u origin main --force

echo.
echo ======================================================================
echo  Code pushed to GitHub successfully!
echo.
echo  Now open https://render.com (100%% Free, No Credit Card):
echo   1. Sign in with GitHub
echo   2. Click "New +" -> "Web Service"
echo   3. Select your "rscoe-cec-videomaker" repository
echo   4. Click "Deploy Web Service"
echo.
echo  You will get your permanent 24/7 link (e.g. https://...onrender.com)!
echo ======================================================================
pause
