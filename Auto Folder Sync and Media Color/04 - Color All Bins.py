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

def color_media_pool(folder):
    clips = folder.GetClipList()
    if clips:
        for clip in clips:
            file_path = clip.GetClipProperty("File Path")
            if file_path:
                camera_luts = config.get("CAMERA_LUTS", {})
                sorted_keywords = sorted(config["CAMERA_KEYWORDS"].items(), key=lambda k: len(k[0]), reverse=True)
                clean_path = file_path.lower().replace("-", "").replace("_", "").replace(" ", "")
                
                for keyword, color in sorted_keywords:
                    clean_keyword = keyword.lower().replace("-", "").replace("_", "").replace(" ", "")
                    
                    if clean_keyword in clean_path:
                        clip.SetClipColor(color)
                        
                        if keyword in camera_luts and camera_luts[keyword]:
                            clip.SetClipProperty("Input LUT", camera_luts[keyword])
                            
                        break
    
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

    print("--- STARTING MEDIA POOL SCAN ---")

    media_pool = project.GetMediaPool()
    root_folder = media_pool.GetRootFolder()
    
    color_media_pool(root_folder)
    
    print("\n--- SCRIPT FINISHED --- CHeck my stuff on Instagram: SuperClaudioo")

if __name__ == "__main__":
    main()