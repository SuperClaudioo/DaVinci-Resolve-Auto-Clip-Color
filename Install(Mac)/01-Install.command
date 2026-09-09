#!/bin/bash
echo "Installing Auto Folder Sync and Media Bin Color..."

TARGET_DIR="$HOME/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility/Auto Folder Sync and Media Color"

mkdir -p "$TARGET_DIR"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

SOURCE_DIR="$SCRIPT_DIR/../Auto Folder Sync and Media Color"

cp "$SOURCE_DIR"/*.py "$TARGET_DIR/"
cp "$SOURCE_DIR"/Config.json "$TARGET_DIR/"

echo ""
echo "Success! The scripts have been installed."
echo "Please restart DaVinci Resolve, then look under Workspace > Scripts."
echo ""