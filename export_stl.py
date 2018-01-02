#This script will export all objects in the scene as an STL file.
#In order for this script to properly function, Blender must be
#opened via the terminal with ./Applications/blender.app/Content/MacOS/blender
#NOTE: It is not known yet if this script will work in Blender headless mode.
import bpy
import os

# get the current path and make a new folder for the exported meshes
path = bpy.path.abspath('/Users/jamesmcdowell/Desktop/')

if not os.path.exists(path):
    os.makedirs(path)

for object in bpy.context.selected_objects:

    # deselect all meshes
    bpy.ops.object.select_all(action='DESELECT')

    # select the object
    object.select = True

    # export object with its name as file name
    fPath = str((path + object.name + '.stl'))

    #bpy.context.active_object = object
    bpy.ops.export_mesh.stl(filepath=fPath)