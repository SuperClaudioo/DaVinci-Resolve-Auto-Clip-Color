#!/usr/bin/env python

CAMERA_KEYWORDS = {
    # Sony
    "A7SIII": "Orange",
    "A7S3": "Orange",
    "A7S 3": "Orange",
    
    # Insta360
    "Insta360": "Yellow",
    "X5": "Yellow",
    
    # Samsung
    "S25 Ultra": "Chocolate",
    "S25U": "Chocolate",
    "S25_Ultra": "Chocolate",
    
    # DJI Aerial
    "Air 2S": "Teal",
    "Air2S": "Teal",
    "Air_2S": "Teal",
    
    # DJI Gimbals
    "Pocket 3": "Blue",
    "Pocket3": "Blue",
    "Pocket 4P": "Purple",
    "Pocket4P": "Purple",
    
    # DJI 360
    "DJI 360": "Pink",
    "DJI360": "Pink",
    "360": "Pink",
}

def get_resolve():
    try:
        import DaVinciResolveScript as bmd
        return bmd.scriptapp("Resolve")
    except ImportError:
        return resolve

def color_media_pool(folder):
    # Color the clips inside the folder based on their File Path
    clips = folder.GetClipList()
    if clips:
        for clip in clips:
            file_path = clip.GetClipProperty("File Path")
            if file_path:
                for keyword, color in CAMERA_KEYWORDS.items():
                    if keyword.lower() in file_path.lower():
                        clip.SetClipColor(color)
                        break 
    
    # Recursively scan sub-bins of the selected bin
    subfolders = folder.GetSubFolderList()
    if subfolders:
        for subfolder in subfolders:
            color_media_pool(subfolder)

def main():
    resolve_app = get_resolve()
    if not resolve_app:
        print("Could not connect to DaVinci Resolve.")
        return

    project_manager = resolve_app.GetProjectManager()
    project = project_manager.GetCurrentProject()
    
    if not project:
        print("No project is currently open.")
        return

    media_pool = project.GetMediaPool()
    
    # Target the currently open/selected bin instead of the entire project
    current_folder = media_pool.GetCurrentFolder()
    
    if not current_folder:
        print("No bin is currently selected.")
        return

    print(f"--- STARTING SCAN ON BIN: '{current_folder.GetName()}' ---")
    color_media_pool(current_folder)
    print("\n--- SCRIPT FINISHED --- CHeck my stuff on Instagram: SuperClaudioo")

if __name__ == "__main__":
    main()