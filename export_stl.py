#This script will export all objects in the scene as an STL file.
#In order for this script to properly function, Blender must be
#opened via the terminal with ./Applications/blender.app/Contents/MacOS/blender
#NOTE: It is not known yet if this script will work in Blender headless mode.
import bpy
import bmesh
import os

#Removes the camera and cube objects in the initial scene.
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Camera'].select = True
bpy.ops.object.delete()
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Cube'].select = True
bpy.ops.object.delete()

#[start] make custom geometry
verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),  (0, 0, -1), (1, 0, -1), (1, 1, -1), (0, 1, -1)]  # 2 verts made with XYZ coords
mesh = bpy.data.meshes.new("mesh")  # add a new mesh
obj = bpy.data.objects.new("MyObject", mesh)  # add a new object using the mesh

scene = bpy.context.scene
scene.objects.link(obj)  # put the object into the scene (link)
scene.objects.active = obj  # set as the active object in the scene
obj.select = True  # select object

mesh = bpy.context.object.data
bm = bmesh.new()

for v in verts:
    bm.verts.new(v)  # add a new vert

#front face    
v1 = bm.verts.new(verts[0])
v2 = bm.verts.new(verts[1])
v3 = bm.verts.new(verts[2])
bm.faces.new((v1, v2, v3))
v1 = bm.verts.new(verts[2])
v2 = bm.verts.new(verts[3])
v3 = bm.verts.new(verts[0])
bm.faces.new((v1, v2, v3))

#back face    
v1 = bm.verts.new(verts[4])
v2 = bm.verts.new(verts[5])
v3 = bm.verts.new(verts[6])
bm.faces.new((v1, v2, v3))
v1 = bm.verts.new(verts[6])
v2 = bm.verts.new(verts[7])
v3 = bm.verts.new(verts[4])
bm.faces.new((v1, v2, v3))

#left face    
v1 = bm.verts.new(verts[0])
v2 = bm.verts.new(verts[3])
v3 = bm.verts.new(verts[7])
bm.faces.new((v1, v2, v3))
v1 = bm.verts.new(verts[7])
v2 = bm.verts.new(verts[4])
v3 = bm.verts.new(verts[0])
bm.faces.new((v1, v2, v3))

#right face    
v1 = bm.verts.new(verts[1])
v2 = bm.verts.new(verts[5])
v3 = bm.verts.new(verts[6])
bm.faces.new((v1, v2, v3))
v1 = bm.verts.new(verts[6])
v2 = bm.verts.new(verts[2])
v3 = bm.verts.new(verts[1])
bm.faces.new((v1, v2, v3))

#bottom face    
v1 = bm.verts.new(verts[0])
v2 = bm.verts.new(verts[1])
v3 = bm.verts.new(verts[5])
bm.faces.new((v1, v2, v3))
v1 = bm.verts.new(verts[5])
v2 = bm.verts.new(verts[4])
v3 = bm.verts.new(verts[0])
bm.faces.new((v1, v2, v3))

#top face    
v1 = bm.verts.new(verts[3])
v2 = bm.verts.new(verts[7])
v3 = bm.verts.new(verts[6])
bm.faces.new((v1, v2, v3))
v1 = bm.verts.new(verts[6])
v2 = bm.verts.new(verts[2])
v3 = bm.verts.new(verts[3])
bm.faces.new((v1, v2, v3))

# make the bmesh the object's mesh
bm.to_mesh(mesh)  
bm.free()  # always do this when finished
#[end] make custom geometry

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