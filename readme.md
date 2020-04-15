# Blender Object Export Scripts
Various Python scripts that allow you to export characteristics of the currently loaded Blender scene file.

## Index
  - **SaveLocationsAbsJson.py**. Save the absolute world locations of all of the visible objects in the Blender scene.
  - **SaveLocationsRelJson.py**. Save the relative model locations of all of the visible objects in the Blender scene.
  - **SaveRotationsJson.py**. Save the Euler rotations (X, Y, Z) of all of the visible objects in the Blender scene.
  - **SaveScalesJson.py**. Save the 3D scales of all of the visible objects in the Blender scene.
  - **SaveTreeJson.py**. Save the outline layout of the names of the visible objects in the Blender scene.

## Using the Scripts
Each of the scripts in this folder are manually loaded into the **Text Editor** view, and executed with the **Run Script** button, after setting the **scnDataFilename** variable with path and filename.

There are not yet any user-interface elements for the scripts. If you would like to see any of these as plug-in features for Blender, please make a request or vote for that request if it has already been made.

## Data File Format
The output data from these scripts is JSON, a text-based human readable format that can be exchanged with various other software platforms.

Following are the specific formats.

| Script | Pattern |
|--------|---------|
| SaveLocationsAbsJson.py, <br />SaveLocationsRelJson.py, <br />SaveRotationsJson.py, <br />SaveScalesJson.py | \[ { "PartName": "{PartName}", "X": {X}, "Y": {Y}, "Z": {Z} } , ... \] |
| SaveTreeJson.py | \[ { "PartName": "{PartName}", "ParentName": "{ParentName}" } , ... \] |