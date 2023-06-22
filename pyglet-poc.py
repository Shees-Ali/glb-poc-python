import trimesh

# Load the .glb file as a Trimesh scene
tri_scene = trimesh.load('source/Scene_OSR.glb')

# Using trimesh function generate random transformation co-ordinates and transform position
tri_scene = tri_scene.apply_transform(
    trimesh.transformations.random_rotation_matrix())

# Trimesh uses pyglet window to whow the 3D Model
tri_scene.show()

# Using the builtin function to get image bytes
png = tri_scene.save_image()

# Write the bytes to file
with open('res/new_pose.png', "wb") as f:
    f.write(png)
    f.close()
