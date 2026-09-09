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

    timeline = project.GetCurrentTimeline()
    
    if not timeline:
        print("No timeline is currently open. Please open a timeline and try again.")
        return

    print(f"Scanning Timeline: '{timeline.GetName()}'...")

    # Loop through all video tracks (1-indexed in Resolve API)
    track_count = timeline.GetTrackCount("video")
    
    for track_index in range(1, track_count + 1):
        items = timeline.GetItemListInTrack("video", track_index)
        
        if items:
            for item in items:
                # Retrieve the underlying media pool item to access file properties
                mp_item = item.GetMediaPoolItem()
                
                if mp_item:
                    file_path = mp_item.GetClipProperty("File Path")
                    
                    if file_path:
                        camera_luts = config.get("CAMERA_LUTS", {})
                        sorted_keywords = sorted(config["CAMERA_KEYWORDS"].items(), key=lambda k: len(k[0]), reverse=True)
                        clean_path = file_path.lower().replace("-", "").replace("_", "").replace(" ", "")
                        
                        for keyword, color in sorted_keywords:
                            clean_keyword = keyword.lower().replace("-", "").replace("_", "").replace(" ", "")
                            
                            if clean_keyword in clean_path:
                                item.SetClipColor(color)
                                
                                if keyword in camera_luts and camera_luts[keyword]:
                                    item.SetLUT(1, camera_luts[keyword])
                                    
                                print(f" ---> SUCCESS: Colored {color} & Checked LUT for clip '{item.GetName()}'")
                                break 

    print("\n--- SCRIPT FINISHED --- Check my stuff on Instagram: SuperClaudioo")

if __name__ == "__main__":
    main()