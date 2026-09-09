@echo off
echo Installing Auto Folder Sync and Media Bin Color...

set "TARGET_DIR=%AppData%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\Auto Folder Sync and Media Color"
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"

copy "%~dp0..\Auto Folder Sync and Media Color\*.py" "%TARGET_DIR%" >nul
copy "%~dp0..\Auto Folder Sync and Media Color\Config.json" "%TARGET_DIR%" >nul

echo.
echo Success! The scripts have been installed.
echo Please restart DaVinci Resolve, then look under Workspace > Scripts.
echo.
pause