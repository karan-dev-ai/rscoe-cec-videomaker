@echo off
title Push CEC Video Maker to GitHub
color 0B
cls

echo ======================================================================
echo   Push CEC Video Maker to GitHub (for 24/7 Free Cloud Hosting)
echo ======================================================================
echo.
echo Target Repository: https://github.com/karan-dev-ai/rscoe-cec-videomaker.git
echo.
echo [1/3] Staging all code, templates, and 15 motivational study tracks...
git add .
git commit -m "Deploy RSCOE CEC Video Maker" >nul 2>&1

echo [2/3] Setting GitHub remote...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/karan-dev-ai/rscoe-cec-videomaker.git

echo [3/3] Pushing to GitHub...
echo.
echo * If a GitHub sign-in popup appears, click "Sign in with your browser" / "Authorize" *
echo.
git push -u origin main --force

echo.
echo ======================================================================
echo  Code pushed to GitHub successfully!
echo.
echo  Now switch back to your Render tab:
echo   1. In the top right corner, click "Manual Deploy"
echo   2. Click "Deploy latest commit"
echo.
echo  Render will start building your container!
echo  Within 2-3 minutes, your permanent link will be LIVE:
echo  https://rscoe-cec-videomaker.onrender.com
echo ======================================================================
pause
