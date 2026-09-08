# ![](https://img.shields.io/badge/DaVinci-E66D1E?style=for-the-badge) ![](https://img.shields.io/badge/Resolve-0B8789?style=for-the-badge) ![](https://img.shields.io/badge/Auto-725686?style=for-the-badge) ![](https://img.shields.io/badge/Folder-3B70A8?style=for-the-badge) ![](https://img.shields.io/badge/And-D2A42F?style=for-the-badge) ![](https://img.shields.io/badge/Clip-49936E?style=for-the-badge) ![](https://img.shields.io/badge/Color-BA5C94?style=for-the-badge)

# <span style="color:#E66D1E">DaVinci</span> <span style="color:#3B70A8">Resolve</span> <span style="color:#D2A42F">Auto</span> <span style="color:#49936E">Folder</span> <span style="color:#0B8789">and</span> <span style="color:#725686">Clip</span> <span style="color:#BA5C94">Color</span>

A collection of Python scripts for DaVinci Resolve Studio that automatically syncs hard drive folders into master bins and assigns specific clip colors to your footage by reading the source file paths.

By organizing your raw footage into camera-specific folders, these scripts scan the file paths and instantly apply a predefined color palette to your clips, saving you a lot of time.

## Included Scripts & Files
* **[Auto Import Folders](Auto%20Import%20Folders.py)**<br/>
`Automatically syncs root hard drive directories into DaVinci Resolve master bins and colors matching clips on import.`
* **[AutoClipColor - All Bins](AutoClipColor%20-%20All%20Bins.py)**<br/>
`Scans your entire Media Pool from the root folder down and applies colors to every matching clip.`
* **[AutoClipColor - Selected Bin](AutoClipColor%20-%20Selected%20Bin.py)**<br/>
`Targets only the currently open bin within the Media Pool.`
* **[AutoClipColor - Timeline Only](AutoClipColor%20-%20Timeline%20Only.py)**<br/>
`Scans your currently active timeline and applies colors directly to the items placed on your video tracks.`
* **[AutoClip Config](AutoClip%20Config.json)**<br/>
`A centralized configuration file where you manage your sync paths and camera keyword color rules in one place.`
* **[Download All Scripts](https://github.com/SuperClaudioo/DaVinci-Resolve-Auto-Clip-Color/releases/download/v1.0/AutoClipColor.zip)**<br/>
`Download the full script suite and configuration template.`

<img width="714" height="1144" alt="Screenshot 2026-09-08 172916" src="https://github.com/user-attachments/assets/83273ffd-7fe6-4171-ad5d-d0e44e2ab8d6" />

I built multiple scripts because sometimes you just want to:
   - Auto-sync external directories into bins
   - Color one specific bin or camera
   - Color only active timeline clips
   - Color all bins globally

## Requirements
* **DaVinci Resolve Studio** (The free version does not support external Python scripting).
* Python 3 installed on your system and linked in Resolve's preferences (`Preferences > System > General`).

## Preparing the Files and Folders
- Make sure your hard drive source directories contain your raw footage separated logically.
- Configure your target paths and camera keywords inside the `AutoClip Config.json` file.
- The script checks file paths dynamically to match your established rules.

<img width="544" height="333" alt="Screenshot 2026-09-08 124859" src="https://github.com/user-attachments/assets/727ebf1e-eaf6-4fef-8d27-676a01b97375" />

## Installation & Usage
   1. Open DaVinci Resolve.
   2. Go to the top menu bar and select **Workspace** > **Scripts** > **Open Scripts Folder**.

   - On Windows it is located at:
      `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Utility`
   - On macOS it is located at:
      `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility`
   3. Drop all the `.py` script files and the `AutoClip Config.json` file into this `Utility` folder.
      - `You might have to restart DaVinci Resolve Studio for changes to appear.`
   4. In Resolve, run your desired script from the **Workspace** > **Scripts** menu.

<img width="707" height="1168" alt="Screenshot 2026-09-08 125401" src="https://github.com/user-attachments/assets/731135f7-8562-47da-91f2-9fafdeca0a67" />

## Customization
Instead of editing multiple scripts, you only need to modify **`AutoClip Config.json`** in a text editor to update your folder paths or camera keyword preferences. 

```json
{
    "_comment_folders": "1. Add any root hard drive folders you want to sync into DaVinci Resolve.",
    "FOLDERS_TO_SYNC": [
        "D:\\RAW",
        "G:\\360"
    ],
    "_comment_keywords": "Match your camera names or keywords to your preferred DaVinci Resolve colors. Specific models go at the top, generic words go at the bottom.",
    "CAMERA_KEYWORDS": {
        "insta360": "Yellow",
        "pocket 4p": "Violet",
        "dji pocket 3": "Purple",
        "air 2s": "Tan",
        "s25 ultra": "Chocolate",
        "a7siii": "Orange",
        "360": "Pink",
        "sony": "Orange",
        "canon": "Blue",
        "gopro": "Navy"
    }
}
```

Note:
   - Put specific camera models (like "insta360") at the top, and generic or short words (like "360") at the bottom. The script reads top-to-bottom and halts on the first matched keyword.
   
   - Just use any notepad editor to edit the file(s) and customize it to your preferred look.

---
**Supported Resolve Colors:**

Orange, Apricot, Yellow, Lime, Olive, Green, Teal, Navy, Blue, Purple, Violet, Pink, Tan, Beige, Brown, Chocolate.

![](https://img.shields.io/badge/-Orange-E66D1E) ![](https://img.shields.io/badge/-Apricot-EFA037) ![](https://img.shields.io/badge/-Yellow-D2A42F) ![](https://img.shields.io/badge/-Lime-A2C327) ![](https://img.shields.io/badge/-Olive-608430) ![](https://img.shields.io/badge/-Green-49936E) ![](https://img.shields.io/badge/-Teal-0B8789) ![](https://img.shields.io/badge/-Navy-194D70) ![](https://img.shields.io/badge/-Blue-3B70A8) ![](https://img.shields.io/badge/-Purple-725686) ![](https://img.shields.io/badge/-Violet-BA5C94) ![](https://img.shields.io/badge/-Pink-DB90A5) ![](https://img.shields.io/badge/-Tan-AD9A7E) ![](https://img.shields.io/badge/-Beige-CEAA8A) ![](https://img.shields.io/badge/-Brown-7B5628) ![](https://img.shields.io/badge/-Chocolate-754830)

 <img width="895" height="696" alt="Screenshot 2026-09-08 124217" src="https://github.com/user-attachments/assets/0a40a4ef-9eac-4886-8cbd-0ae30df5dc63" />
 
---
**Troubleshooting Section:**

   If scripts don't run, ensure Python 3 is installed on your system and linked in Resolve under <b>Preferences > System > General</b>

---
**Author:**
[@SuperClaudioo](https://instagram.com/SuperClaudioo)
