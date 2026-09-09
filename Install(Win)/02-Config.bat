@echo off
set "CONFIG_FILE=%AppData%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\Auto Folder Sync and Media Color\Config.json"

if exist "%CONFIG_FILE%" (
    start "" "%CONFIG_FILE%"
) else (
    echo Config.json not found. Please run 01-Install.bat first.
    pause
)