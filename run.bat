@echo off
title GenshinAssistant
mode con: cols=50 lines=10
set curdir=%~dp0
cd /d %curdir%
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Administrator permissions got.
    goto :admin
) else (
    echo Administrator permissions required. Right-click and select "Run as administrator".
    pause >nul
    exit
)

:admin

REM 检测是否已安装 Python
echo Checking......Python
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Please install Python first
    exit /b
)

:reqs
REM 检查是否安装成功
echo Checking......Installed requirements
pip freeze > installed_packages.txt
echo Checking......Needy requirements
pip install -r requirements.txt --no-warn-script-location > nul 2>&1
if %errorlevel% neq 0 (
    echo The requirements has not been installed completely. Now installing...
    pip install -r requirements.txt
    goto :reqs
)

echo Python and requirements has been installed. Now running main script...

:start
python fly2sky.py

pause
goto start