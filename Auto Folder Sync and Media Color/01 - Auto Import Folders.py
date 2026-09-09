import json
import os
import inspect

# Automatically find the script's folder even when run inside DaVinci Resolve
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

config_path = os.path.join(script_dir, "Config.json")

with open(config_path, "r") as f:
    config = json.load(f)

def get_resolve():
    try:
        import DaVinciResolveScript as bmd
        return bmd.scriptapp("Resolve")
    except ImportError:
        return resolve

def get_or_create_bin(media_pool, parent_bin, bin_name):
    """Finds an existing bin or creates a new one if it doesn't exist."""
    subfolders = parent_bin.GetSubFolderList()
    for folder in subfolders:
        if folder.GetName() == bin_name:
            return folder
    media_pool.SetCurrentFolder(parent_bin)
    return media_pool.AddSubFolder(parent_bin, bin_name)

def sync_directory(media_pool, media_storage, current_bin, current_os_path):
    """Recursively mirrors OS folders into Resolve bins."""
    if not os.path.exists(current_os_path):
        return

    existing_clips = []
    clips_in_bin = current_bin.GetClipList()
    if clips_in_bin:
        existing_clips = [clip.GetClipProperty("File Path") for clip in clips_in_bin]

    files_to_import = []
    folders_to_scan = []

    for item in os.listdir(current_os_path):
        item_path = os.path.join(current_os_path, item)
        if os.path.isfile(item_path):
            if item_path not in existing_clips:
                files_to_import.append(item_path)
        elif os.path.isdir(item_path):
            folders_to_scan.append((item, item_path))

    if files_to_import:
        media_pool.SetCurrentFolder(current_bin)
        imported_clips = media_storage.AddItemListToMediaPool(files_to_import)
        
        if imported_clips:
            print(f" ---> Imported {len(imported_clips)} files into bin: '{current_bin.GetName()}'")

    for folder_name, folder_path in folders_to_scan:
        if folder_name.lower() in ["proxy", "proxies"]:
            continue
        child_bin = get_or_create_bin(media_pool, current_bin, folder_name)
        sync_directory(media_pool, media_storage, child_bin, folder_path)

def main():
    resolve_app = get_resolve()
    if not resolve_app:
        print("Could not connect to DaVinci Resolve. Make sure a project is open.")
        return

    project = resolve_app.GetProjectManager().GetCurrentProject()
    if not project:
        print("No active project found in DaVinci Resolve.")
        return

    media_pool = project.GetMediaPool()
    media_storage = resolve_app.GetMediaStorage()
    root_bin = media_pool.GetRootFolder()

    print("--- STARTING FOLDER SYNC ---")
    for folder_path in config["FOLDERS_TO_SYNC"]:
        if os.path.exists(folder_path):
            folder_name = os.path.basename(os.path.normpath(folder_path))
            print(f"\nSyncing folder path: {folder_path} -> Master Bin: [{folder_name}]")
            target_bin = get_or_create_bin(media_pool, root_bin, folder_name)
            sync_directory(media_pool, media_storage, target_bin, folder_path)
        else:
            print(f"\nSkipping (Path not found on computer): {folder_path}")

    print("\n--- SCRIPT FINISHED --- Check my stuff on Instagram: SuperClaudioo")

if __name__ == "__main__":
    main()