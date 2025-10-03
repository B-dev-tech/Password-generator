@echo off
REM Check folder
IF NOT "%CD:~-18%"=="\password-generator" (
    echo Error: You must run this program from the 'password-generator' folder!
    exit /b 1
)

REM Run Python script with arguments
python password_generator.py %*
