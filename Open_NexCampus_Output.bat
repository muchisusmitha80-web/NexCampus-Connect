@echo off
title NexCampus - DIET Platform Launcher
echo ============================================================
echo   NexCampus - Dhanekula Institute of Engineering & Technology
echo   Launching Standalone Offline Portal...
echo ============================================================
echo.
cd /d "%~dp0\standalone_site"
start index.html
echo Opened index.html in your default web browser!
echo.
pause
