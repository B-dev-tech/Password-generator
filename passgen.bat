@echo off
REM Check folder (ignore case)
for %%A in ("%CD%") do set FOLDER=%%~nxA
setlocal enabledelayedexpansion
set FOLDER=!FOLDER!
set FOLDER=!FOLDER:~0,999!
IF /I NOT "!FOLDER!"=="password-generator" (
    echo Error: You must run this program from the 'password-generator' folder!
    exit /b 1
)

python password_generator.py %*
