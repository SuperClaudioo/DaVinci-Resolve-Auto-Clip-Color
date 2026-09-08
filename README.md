# ![](https://img.shields.io/badge/DaVinci-E66D1E?style=for-the-badge) ![](https://img.shields.io/badge/Resolve-0B8789?style=for-the-badge) ![](https://img.shields.io/badge/Auto-725686?style=for-the-badge) ![](https://img.shields.io/badge/Clip-49936E?style=for-the-badge) ![](https://img.shields.io/badge/Colorizer-D2A42F?style=for-the-badge)

A collection of Python scripts for DaVinci Resolve Studio that automatically assign specific clip colors to your footage by reading the source file paths.

By organizing your raw footage into camera-specific folders (e.g., `Day 1/Pocket 3/`), these scripts scan the file paths and instantly apply a predefined color palette to your clips, saving you a lot of time.

## Included Scripts
* **[AutoClipColor - All Bins](AutoClipColor%20-%20All%20Bins.py)**<br/>
`Scans your entire Media Pool from the root folder down and applies colors to every matching clip.`
* **[AutoClipColor - Selected Bin](AutoClipColor%20-%20Selected%20Bin.py)**<br/>
`Targets only the currently open bin within the Media Pool.`
* **[AutoClipColor - Timeline Only](AutoClipColor%20-%20Timeline%20Only.py)**<br/>
`Scans your currently active timeline and applies colors directly to the items placed on your video tracks.`
<img width="228" height="625" alt="Screenshot 2026-09-08 124139" src="https://github.com/user-attachments/assets/dac7dc0c-8ade-43e6-b542-8f3a0a21a41b" />

I did 3 different scripts because sometimes you just want to:
   - Color one bin/camera
   - Color only the timeline
   - Color all bins (which is a slower process, it can take several seconds when you have thousands of clips).

## Requirements
* <b>DaVinci Resolve Studio</b> (The free version does not support external Python scripting).
* Python 3 installed on your system and linked in Resolve's preferences (`Preferences > System > General`).

## Preparing the files and folders
- Before using it, make sure that your files are on the correct folders.
   - For example if you have a Sony camera the clips should be inside the Sony camera folder, if you have a DJI Pocket 3 camera, the clips should be inside a Pocket 3 folder, etc...
   - You can have multiple folders with the same name.
   - The script will search all clip files inside the folders to match the correct color.
<img width="544" height="333" alt="Screenshot 2026-09-08 124859" src="https://github.com/user-attachments/assets/d3d5f37d-bfef-409c-8a43-ca4f9fd3e96e" />

## Installation & Usage
   1. Open DaVinci Resolve.
   2. Go to the top menu bar and select **Workspace** > **Scripts** > **Open Scripts Folder**.

   - On windows it's in:
      `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Utility`
   - On MacOS is' in:
      `/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Utility`
   3. Drop the `.py` files into this `Utility` folder.
   4. In Resolve, run your desired script from the **Workspace** > **Scripts** menu.
<img width="707" height="1168" alt="Screenshot 2026-09-08 125401" src="https://github.com/user-attachments/assets/17cf0db1-5480-4a66-859d-44e32d3aaed2" />


## Customization
You can easily modify the script to match your specific cameras and preferred colors.
Open any of the `.py` files in a text editor and update the `CAMERA_KEYWORDS` dictionary at the top. 
You can add several lines/folders for the same camera ("Sony A7SIII", "Sony A7S3", etc...).

<img width="424" height="1387" alt="Screenshot 2026-09-08 130857" src="https://github.com/user-attachments/assets/01ef16ac-ae4b-4f73-a1d1-a57f11905a73" />!<img width="382" height="708" alt="Screenshot 2026-09-08 124559" src="https://github.com/user-attachments/assets/56772fc2-dbd1-4ac5-b35e-6efd6f4e20bc" />

   Just use any notepad editor to edit the file(s) and costumize it to your prefered outlook.

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
