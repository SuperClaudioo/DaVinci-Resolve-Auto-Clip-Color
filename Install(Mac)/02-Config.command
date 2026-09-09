#!/bin/bash
CONFIG_FILE="$HOME/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility/Auto Folder Sync and Media Color/Config.json"

if [ -f "$CONFIG_FILE" ]; then
    open "$CONFIG_FILE"
else
    echo "Config.json not found. Please run 01-Install.command first."
    sleep 3
fi