@echo off
title GenshinHolder
mode con: cols=50 lines=10
set curdir=%~dp0
cd /d %curdir%
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :admin
) else (
    echo Administrator permissions required. Right-click and select "Run as administrator".
    pause >nul
    exit
)
:admin
:start
python fly2sky.py

pause
goto start