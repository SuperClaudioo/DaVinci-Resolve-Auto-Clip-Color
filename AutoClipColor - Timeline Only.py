#!/usr/bin/env python

CAMERA_KEYWORDS = {
    # Sony
    "Sony": "Orange",
    
    # Canon
    "Canon": "Blue",
    
    # Panasonic / Lumix
    "Panasonic": "Purple",
    "Lumix": "Purple",
    
    # Blackmagic Design
    "Blackmagic": "Teal",
    "BMPCC": "Teal",
    "BMD": "Teal",
    
    # RED Digital Cinema
    "RED": "Chocolate",
    
    # ARRI
    "ARRI": "Yellow",
    "Alexa": "Yellow",
    
    # DJI
    "DJI": "Green",
    
    # GoPro
    "GoPro": "Navy",
    
    # Nikon
    "Nikon": "Apricot",
    
    # Fujifilm
    "Fujifilm": "Olive",
    "Fuji": "Olive",
    
    # Apple / iPhone
    "Apple": "Beige",
    "iPhone": "Beige",
    
    # Insta360
    "Insta360": "Violet"
}

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
                        # Check if any keywords exist in the file path
                        for keyword, color in CAMERA_KEYWORDS.items():
                            if keyword.lower() in file_path.lower():
                                item.SetClipColor(color)
                                print(f" ---> SUCCESS: Colored {color} for clip '{item.GetName()}'")
                                break 

    print("\n--- SCRIPT FINISHED --- CHeck my stuff on Instagram: SuperClaudioo")

if __name__ == "__main__":
    main()
