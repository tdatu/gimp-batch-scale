# gimp-batch-scale
## Description 
Simple Gimp plug-in to batch scale images in source folder and produced scaled images 
to output folder. 

## Installation
Batch_Scale.py should be placed in Gimp's plug-in folder. 
- In Linux Manjaro, it is in /usr/lib/gimp/2.0/plug-ins/. 
- In windows, it usually under C:\Program Files\Gimp\plugin\. 
- In Mac, /Applications/Gimp-2.10.app/Contents/Resources/lib/gimp/2.0/plug-ins/
- Set the appropriate permission to chmod 775. 

## Gimp Menu
Image > Transform > BatchScale

## To use
1. Launch Gimp, then open an image (to activate the filter submenu).
2. Filters > Render > BatchScale.
3. Set the source folder and destination folder (no trailing slash / at the end).
4. Set the minimum width and minimum height.

### Note:
The plugin supports variety of well known images such as jpeg, png, gif, tiff and others. 
