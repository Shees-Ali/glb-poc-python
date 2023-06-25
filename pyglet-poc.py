import trimesh
from trimesh.viewer import SceneViewer
import numpy as np

# Load the .glb file as a Trimesh scene
tri_scene = trimesh.load('source/PaintingAsset.glb')


# Using trimesh function generate random transformation co-ordinates and transform position
tri_scene = tri_scene.apply_transform(
    trimesh.transformations.random_rotation_matrix())


# Get all the geometries in the current scene
scene_geometries = tri_scene.geometry_identifiers.values()
print(scene_geometries)
# Delete one more multiple geometries from the scene and also remove any node in the transform graph which references it.
# "Mesh.001_1", "Mesh.001"
tri_scene.delete_geometry(["PaintBrush3_PaintBrush3_0.001"])

# Generate lights for the scene
# lights, transforms = trimesh.scene.lighting.autolight(tri_scene)

# # Print the generated lights
# for light in lights:
#     print(light)

# Strip visuals from every Trimesh geometry and set them to an empty ColorVisuals.
# tri_scene.strip_visuals()

# Sets the camera resolution
tri_scene.camera.resolution = (2000, 2000)

# Generate transform for a camera to keep a list of points in the camera’s field of view.
# points = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
# tri_scene.camera_transform = tri_scene.camera.look_at(
#     points=points,
#     rotation=trimesh.transformations.euler_matrix(np.pi / 6, 0, np.pi / 2))

# Return a copy of the current scene, with meshes and scene transforms scaled to the requested factor.
# tri_scene = tri_scene.scaled([2,1,2])


# Trimesh uses pyglet window to whow the 3D Model
# tri_scene.show()

# Using the builtin function to get image bytes
png = tri_scene.save_image()

# Write the bytes to file
with open('res/new_pose.png', "wb") as f:
    f.write(png)
    f.close()
