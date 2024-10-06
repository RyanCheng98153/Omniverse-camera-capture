import omni
# from omni.isaac.core.objects import DynamicCuboid

# Get the stage
stage = omni.usd.get_context().get_stage()

position = (0, 65, 130)
rotate = (8, 180, 0)


# Define the camera and the target object paths
camera_path = "/World/Camera"
object_path = "/World/MyObject"

# Get the camera and the object prims
camera_prim = stage.GetPrimAtPath(camera_path)
object_prim = stage.GetPrimAtPath(object_path)

# Define a function to update the camera position
def follow_object():
    object_position = object_prim.GetAttribute("xformOp:translate").Get()
    camera_position = [object_position[0], object_position[1], object_position[2] + 10]
    camera_prim.GetAttribute("xformOp:translate").Set(camera_position)

# Connect the function to the update event
omni.kit.app.get_app().get_update_event().add(follow_object)
