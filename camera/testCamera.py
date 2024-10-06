import omni.usd
from pxr import Usd, Sdf, UsdGeom, Gf

stage: Usd.Stage = omni.usd.get_context().get_stage() 

# Create an in-memory Stage with /World Xform prim as the default prim
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))

stage.SetDefaultPrim(default_prim.GetPrim())

# Create the perspective camera at /World/MyPerspCam
camera_path = default_prim.GetPath().AppendPath("Camera")

camera: UsdGeom.Camera = UsdGeom.Camera.Define(stage, camera_path)

# Check that the camera was created
prim = camera.GetPrim()
projection = camera.GetProjectionAttr().Get()

print(prim)
print(projection)
print(prim.GetAttribute("xformOp:translate").Get())

alldata = prim.GetProperties()
print(alldata)

# for key in alldata.keys():
#     print(f"[{key}]: {alldata[key]}")
