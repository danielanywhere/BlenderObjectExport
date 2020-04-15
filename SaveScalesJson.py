# SaveScalesJson.py
# Copyright (c). 2016 - 2020 Daniel Patterson, MCSD (danielanywhere)
# Released for public access under the MIT License.
# http://www.opensource.org/licenses/mit-license.php
# Save the scale dimension values of all of the objects in the scene
# as a JSON file with the format:
# [ { "PartName": "{PartName}", "X": {X}, "Y": {Y}, "Z": {Z} } , ... ]
# bl_info = {
#    "name": "SaveScalesJson",
#    "author": "DanielAnywhere / Daniel Patterson", 
#    "version": (1, 0, 0),
#    "blender": (2, 78, 0),
#    "location": "3D window > Tool Shelf",
#    "description": "Save the scale dimension values of all of the objects in the scene as a JSON file.",
#    "warning": "",
#    "wiki_url": "http://wiki.blender.org/index.php?title=Extensions:2.6/Py/"
#        "Scripts/Import-Export/{TopicID}",
#    "tracker_url": "https://developer.blender.org/{TrackerID}",
#    "category": "Import-Export"}
# 20200206.1224 - This script doesn't yet have a UI or registration.
import bpy
import json
import math

# Settings.
# Name of the data file to save.
scnDataFilename = "C:\\Temp\\BlenderObjectScales.json";

# Get the current scene reference.
scene = bpy.context.scene;

# Iterate through all objects, creating entries.
obs = []
objects = bpy.data.objects;
for object in objects:
	if object.hide == 0:
		ob = {
			"PartName": object.name,
			"X": round(object.dimensions[0], 6),
			"Y": round(object.dimensions[1], 6),
			"Z": round(object.dimensions[2], 6)
		}
		obs.append(ob);

# Convert the list to JSON.
print(json.dumps(obs, indent=1, sort_keys=True))

# Write the file.
with open(scnDataFilename, "w") as outfile:
	json.dump(obs, outfile, indent=1, sort_keys=True)
