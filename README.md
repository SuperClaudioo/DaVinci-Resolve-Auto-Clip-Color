# DaVinci Resolve Auto Clip Colorizer

A collection of Python scripts for DaVinci Resolve Studio that automatically assign specific clip colors to your footage by reading the source file paths. 

By organizing your raw footage into camera-specific folders (e.g., `Day 1/Pocket 3/`), these scripts scan the file paths and instantly apply a predefined color palette to your clips, saving you a lot of time.

## Included Scripts

* **AutoClipColor - All Bins.py**: Scans your entire Media Pool from the root folder down and applies colors to every matching clip.
* **AutoClipColor - Selected Bin.py**: Targets only the currently open bin within the Media Pool.
* **AutoClipColor - Timeline Only.py**: Scans your currently active timeline and applies colors directly to the items placed on your video tracks.

## Requirements
* DaVinci Resolve Studio (The free version does not support external Python scripting).
* Python 3 installed on your system and linked in Resolve's preferences (`Preferences > System > General`).

## Installation & Usage
1. Open DaVinci Resolve.
2. Go to the top menu bar and select **Workspace** > **Scripts** > **Open Scripts Folder**.

   On windows it's usually:
    `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Utility`
4. Navigate into the **Utility** subfolder.
5. Drop the `.py` files into this `Utility` folder.
6. In Resolve, run your desired script from the **Workspace** > **Scripts** menu.

## Customization
You can easily modify the script to match your specific cameras and preferred colors. Open any of the `.py` files in a text editor and update the `CAMERA_KEYWORDS` dictionary at the top[cite: 1, 2, 3]. 
You can add several lines for the same camera ("Sony A7SIII", "Sony A7S3", etc...).

**Supported Resolve Colors:** Orange, Apricot, Yellow, Green, Teal, Navy, Blue, Purple, Pink, Brown, Chocolate, Mango, Tan, Olive, Mint.

---
**Author:** Check out my work on Instagram: [@SuperClaudioo](https://instagram.com/SuperClaudioo).
