# ![](https://img.shields.io/badge/DaVinci-E66D1E?style=for-the-badge) ![](https://img.shields.io/badge/Resolve-0B8789?style=for-the-badge) ![](https://img.shields.io/badge/Auto-725686?style=for-the-badge) ![](https://img.shields.io/badge/Folder-3B70A8?style=for-the-badge) ![](https://img.shields.io/badge/Sync-D2A42F?style=for-the-badge) ![](https://img.shields.io/badge/And-A2C327?style=for-the-badge) ![](https://img.shields.io/badge/Media-49936E?style=for-the-badge) ![](https://img.shields.io/badge/Color-BA5C94?style=for-the-badge)

# <span style="color:#E66D1E">DaVinci Resolve</span> <span style="color:#725686">Auto</span> <span style="color:#3B70A8">Folder</span> <span style="color:#D2A42F">Sync</span> and <span style="color:#49936E">Media</span> <span style="color:#BA5C94">Color</span>

A professional suite of Python scripts for DaVinci Resolve Studio that automatically syncs hard drive folders into master bins and assigns specific clip colors (and LUTs) to your footage by reading the source file paths.

By organizing your raw footage into camera-specific folders, these scripts scan the file paths and instantly apply a predefined color palette and Input LUT to your clips, saving you hours of manual organization.

## Included Scripts & Files
* **[01 - Auto Import Folders.py](Auto%20Folder%20Sync%20and%20Media%20Color/01%20-%20Auto%20Import%20Folders.py)**<br/>
`Mirrors your hard drive directory structures (including new sub-folders) into Resolve master bins without applying any clip colors.`
* **[02 - Auto Import and Bin Color.py](Auto%20Folder%20Sync%20and%20Media%20Color/02%20-%20Auto%20Import%20and%20Bin%20Color.py)**<br/>
`Automatically syncs root hard drive directories into DaVinci Resolve master bins, colors matching clips, and applies LUTs on import.`
* **[03 - Color Selected Bin.py](Auto%20Folder%20Sync%20and%20Media%20Color/03%20-%20Color%20Selected%20Bin.py)**<br/>
`Targets only the currently open bin within the Media Pool to apply colors and LUTs.`
* **[04 - Color All Bins.py](Auto%20Folder%20Sync%20and%20Media%20Color/04%20-%20Color%20All%20Bins.py)**<br/>
`Scans your entire Media Pool from the root folder down and applies colors and LUTs to every matching clip.`
* **[05 - Color Timeline Media.py](Auto%20Folder%20Sync%20and%20Media%20Color/05%20-%20Color%20Timeline%20Media.py)**<br/>
`Scans your currently active timeline and applies colors directly to the items placed on your video tracks.`
* **[Config.json](Auto%20Folder%20Sync%20and%20Media%20Color/Config.json)**<br/>
`A centralized configuration file where you manage your sync paths, LUTs, and camera keyword color rules in one place.`
* **[Download All Scripts](https://github.com/SuperClaudioo/DaVinci-Resolve-Auto-Folder-Sync-and-Media-Color/archive/refs/tags/v1.0.zip)**<br/>
`Download the full script suite and configuration template.`

<img width="600" height="338" alt="Demo1" src="https://github.com/user-attachments/assets/28cf1a0c-1197-4d40-83f1-170433a9800b" />

I built multiple scripts because sometimes you just want to:
   - Auto-sync external directories into bins (with or without automatic coloring)
   - Color one specific bin or camera
   - Color only active timeline clips
   - Color all bins globally
<img width="1109" height="332" alt="Screenshot 2026-09-09 144744" src="https://github.com/user-attachments/assets/1a3bc8e0-1da7-4d51-9ef5-a3b92e4db369" />

## Requirements
* **DaVinci Resolve Studio** (The free version does not support external Python scripting).
* Python 3 installed on your system and linked in Resolve's preferences (`Preferences > System > General`).

## Installation & Usage

### Recommended (Automated)
Unzip the downloaded package and open the install folder for your operating system:
* **Windows:** Open the `Install(Win)` folder and double-click `01-Install.bat`.
* **Mac:** Open the `Install(Mac)` folder, right-click `01-Install.command`, select **Open**, and run it in Terminal.

Restart DaVinci Resolve. The scripts will appear in the top menu bar under **Workspace > Scripts > Sync and Label Suite**.

On the newer versions, it might not be necessary to restart Resolve.

<img width="383" height="167" alt="Screenshot 2026-09-09 145016" src="https://github.com/user-attachments/assets/80b67ecd-2b01-4e16-ac35-e52fce0afd69" />

### Manual Installation
Copy the `Auto Folder Sync and Media Color` folder to your user-specific Resolve scripts directory:
* **Windows:** `%AppData%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Scripts\Utility\`
* **Mac:** `~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility/`

## Customization
Instead of editing multiple scripts, you only need to use the **`02-Config`** shortcut to update your folder paths, camera keyword preferences, or LUTs. 

```json
{
    "_comment_folders": "Add any root hard drive folders you want to sync into DaVinci Resolve. Use double backslashes (\\)",
    "FOLDERS_TO_SYNC": [
        "D:\\RAW\\2026\\Morocco",
        "D:\\YOUR FOLDER HERE"
    ],
    "_comment_keywords": "Match your camera names or keywords to your preferred DaVinci Resolve colors. Specific models go at the top, generic words go at the bottom.",
    "CAMERA_KEYWORDS": {
        "fx3": "Orange",
        "fx6": "Orange",
        "a7siii": "Orange",
        "a7iv": "Orange",
        
        "c70": "Blue",
        "eos r5": "Blue",
        "eos r6": "Blue",
        
        "pocket 6k": "Navy",
        "pocket 4k": "Navy",
        "ursa mini": "Navy",
        
        "gh6": "Teal",
        "s5iix": "Teal",
        
        "z8": "Yellow",
        "z9": "Yellow",
        
        "x-h2s": "Tan",
        "x-t5": "Tan",
        
        "v-raptor": "Chocolate",
        "komodo": "Chocolate",
        
        "alexa mini": "Olive",
        "alexa 35": "Olive",
        
        "iphone 15 pro": "Apricot",
        "iphone 14 pro": "Apricot",
        
        "s25 ultra": "Lime",
        "s24 ultra": "Lime",
        
        "dji pocket 3": "Purple",
        "mavic 3": "Purple",
        
        "mini 4 pro": "Violet",
        "air 2s": "Violet",
        
        "hero12": "Green",
        "hero11": "Green",
        
        "insta360 x4": "Pink",
        "insta360 x3": "Pink",
        
        "leica sl3": "Beige",
        
        "fpv drone": "Brown",
        
        "sony": "Orange",
        "canon": "Blue",
        "blackmagic": "Navy",
        "bmpcc": "Navy",
        "lumix": "Teal",
        "panasonic": "Teal",
        "nikon": "Yellow",
        "fujifilm": "Tan",
        "fuji": "Tan",
        "red": "Chocolate",
        "arri": "Olive",
        "iphone": "Apricot",
        "apple": "Apricot",
        "samsung": "Lime",
        "galaxy": "Lime",
        "dji": "Purple",
        "gopro": "Green",
        "insta360": "Pink",
        "360": "Pink",
        "leica": "Beige",
        "drone": "Brown"
    },
    "_comment_luts": "Assign exact internal LUT paths to your keywords. Use double backslashes (\\). Leave out any cameras that don't need a LUT.",
    "CAMERA_LUTS": {
        "fx3": "Sony\\SLog3SGamut3.CineToCine+709",
        "a7siii": "Sony\\SLog3SGamut3.CineToCine+709",
        "sony": "Sony\\SLog3SGamut3.CineToCine+709",
		"red": "RED\\RWG_Log3G10_to_REC709_BT1886_with_LOW_CONTRAST_and_R_3_Soft_size_33"
    }
}
```

### Important Formatting Notes:
   - Smart Matching: The script automatically prioritizes longer, specific keywords (like "dji pocket 3") over generic ones (like "dji"). You do not need to worry about the top-to-bottom order.

   - Double Slashes: When adding folder paths or LUT paths on Windows, you must use double backslashes (\\) so the code reads it correctly.

   - Commas: Ensure every line inside a list or group ends with a comma, except for the very last item in that group.

### **Finding Your Exact LUT Path:**
   - To find the exact internal LUT string to paste into your config file, apply the LUT manually to just one clip in your current bin. Open Workspace > Console, click Py3 to switch to Python, and paste this exact code:
```json
clips = resolve.GetProjectManager().GetCurrentProject().GetMediaPool().GetCurrentFolder().GetClipList()
for clip in clips:
    lut = clip.GetClipProperty("Input LUT")
    if lut:
        print(f"\nLUT PATH TO COPY:\n{lut}\n")
        break
```

---
### **Supported Resolve Colors:**

Orange, Apricot, Yellow, Lime, Olive, Green, Teal, Navy, Blue, Purple, Violet, Pink, Tan, Beige, Brown, Chocolate.

![](https://img.shields.io/badge/-Orange-E66D1E) ![](https://img.shields.io/badge/-Apricot-EFA037) ![](https://img.shields.io/badge/-Yellow-D2A42F) ![](https://img.shields.io/badge/-Lime-A2C327) ![](https://img.shields.io/badge/-Olive-608430) ![](https://img.shields.io/badge/-Green-49936E) ![](https://img.shields.io/badge/-Teal-0B8789) ![](https://img.shields.io/badge/-Navy-194D70) ![](https://img.shields.io/badge/-Blue-3B70A8) ![](https://img.shields.io/badge/-Purple-725686) ![](https://img.shields.io/badge/-Violet-BA5C94) ![](https://img.shields.io/badge/-Pink-DB90A5) ![](https://img.shields.io/badge/-Tan-AD9A7E) ![](https://img.shields.io/badge/-Beige-CEAA8A) ![](https://img.shields.io/badge/-Brown-7B5628) ![](https://img.shields.io/badge/-Chocolate-754830)

 <img width="895" height="696" alt="Screenshot 2026-09-08 124217" src="https://github.com/user-attachments/assets/0a40a4ef-9eac-4886-8cbd-0ae30df5dc63" />
 
---
### **Troubleshooting Section:**

   If scripts don't run, ensure Python 3 is installed on your system and linked in Resolve under <b>Preferences > System > General</b>

---
**Author:**
[@SuperClaudioo](https://instagram.com/SuperClaudioo)
