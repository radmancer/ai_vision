#Removes the camera and cube objects in the initial scene.
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Camera'].select = True
bpy.ops.object.delete()
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Cube'].select = True
bpy.ops.object.delete() 