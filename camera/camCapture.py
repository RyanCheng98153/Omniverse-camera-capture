from pxr import Usd, UsdGeom, Sdf
import omni.usd
import omni.kit
from omni.kit.viewport.utility import get_active_viewport
import time

stage: Usd.Stage = omni.usd.get_context().get_stage() 

# Create an in-memory Stage with /World Xform prim as the default prim
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())
# Write the path you want to assign your camera on stage
camera_path = "/World/Camera" 
# Create your UsdGeom Camera
camera: UsdGeom.Camera = UsdGeom.Camera.Define(stage, camera_path)
# Set the time code, here Default(), which is considered less than any numeric TimeCode
timeCode = Usd.TimeCode.Default()
# camXform: Gf.Matrix4d = camera.ComputeLocalToWorldTransform(time)

prim = camera.GetPrim()
# print(prim.GetAttribute("xformOp:translate").Get())

viewport = get_active_viewport()

if not viewport:
    raise RuntimeError("No active Viewport")

# Set the Viewport's active camera to camera prim path you want
viewport.camera_path = camera_path

def capture_and_save_image(picNum:int = 1, freqTime: float=1.0):
    for _ in range(0, picNum):
        time.sleep(freqTime)
        omni.kit.actions.core.execute_action("omni.kit.menu.edit", "capture_screenshot")
        
    print("Image saved successfully to somewhere like 'C:\\Users\\User\\Documents\\Kit\\shared\\screenshots'")
    
capture_and_save_image(1, 1)

print("done")