@echo off
chcp 65001 >nul
echo ========================================
echo   PostLoan AI Platform - Portfolio Mode
echo ========================================
echo.
echo Starting Streamlit workbench...
cd /d "E:\12-agent_finalize\贷后产品中台"
start "PostLoan-Agent" cmd /k "streamlit run app.py --server.port 8502"
echo Waiting for Streamlit to initialize...
timeout /t 5 /nobreak >nul
echo.
echo Opening portfolio site...
start "" "E:\site-redesign\final\index.html"
echo.
echo Done! Streamlit running on http://localhost:8502
echo Click "Live Lab" on the homepage to enter interactive mode.
echo.
pause
