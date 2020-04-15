# SaveTreeJson.py
# Copyright (c). 2016 - 2020 Daniel Patterson, MCSD (danielanywhere)
# Released for public access under the MIT License.
# http://www.opensource.org/licenses/mit-license.php
# Save the tree of trackable properties, including parent names of all
# of the objects in the scene, as a JSON file with the format:
# [ { "PartName": "{PartName}", "ParentName": "{ParentName}" } , ... ]
# bl_info = {
#    "name": "SaveTreeJson",
#    "author": "DanielAnywhere / Daniel Patterson", 
#    "version": (1, 0, 0),
#    "blender": (2, 78, 0),
#    "location": "3D window > Tool Shelf",
#    "description": "Save the tree of trackable properties, including parent names of all of the objects in the scene, as a JSON file.",
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
scnDataFilename = "C:\\Temp\\BlenderObjectTree.json";

# Get the current scene reference.
scene = bpy.context.scene;

# Iterate through all objects, creating entries.
obs = [];
parentName = "";
rArm = "";
rAxis = "";
rEffect = "";

objects = bpy.data.objects;
for object in objects:
	if object.hide == 0:
		# Item is visible and therefore, active.
		if object.parent != None:
			parentName = object.parent.name;
		else:
			parentName = "(None)";
		rAxis = "";
		try:
			rAxis = object["RotationAxis"];
		except:
			pass;
		rEffect = "";
		try:
			rEffect = object["RotationEffect"];
		except:
			pass;
		rArm = "";
		try:
			rArm = object["Armature"];
		except:
			pass;

		ob = {
			"PartName": object.name,
			"ParentName": parentName
			# "RotationAxis": rAxis,
			# "RotationEffect": rEffect,
			# "Armature": rArm
		}
		if len(rAxis) > 0:
			ob.update({"RotationAxis": rAxis});
		if len(rEffect) > 0:
			ob.update({"RotationEffect": rEffect});
		if len(rArm) > 0:
			ob.update({"Armature": rArm});

		obs.append(ob);

# Convert the list to JSON.
print(json.dumps(obs, indent=1, sort_keys=True))

# Write the file.
with open(scnDataFilename, "w") as outfile:
	json.dump(obs, outfile, indent=1, sort_keys=True)
