#This script will export all objects in the scene as an STL file.
#In order for this script to properly function, Blender must be
#opened via the terminal with ./Applications/blender.app/Contents/MacOS/blender
#NOTE: It is not known yet if this script will work in Blender headless mode.
import bpy
import os

#[start] make a cube
#bpy.ops.mesh.primitive_cube_add()
#bpy.ops.mesh.primitive_cube_add(location=(5,0,10))
#[end] make a cube

#[start] make a sphere
def makeMaterial(name, diffuse, specular, alpha):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = diffuse
    mat.diffuse_shader = 'LAMBERT'
    mat.diffuse_intensity = 1.0
    mat.specular_color = specular
    mat.specular_shader = 'COOKTORR'
    mat.specular_intensity = 0.5
    mat.alpha = alpha
    mat.ambient = 1
    return mat
def setMaterial(ob, mat):
    me = ob.data
    me.materials.append(mat)
#cleaning the scene from http://wiki.blender.org/index.php/Dev:2.5/Py/Scripts/Cookbook/Code_snippets/Interface
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()
red = makeMaterial('Red',(1,0,0),(1,1,1),1)
origin = (0,0,0)
bpy.ops.mesh.primitive_uv_sphere_add(location=origin)
bpy.ops.transform.translate(value=(1,0,0))
setMaterial(bpy.context.object, red)
#[end] make a sphere

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