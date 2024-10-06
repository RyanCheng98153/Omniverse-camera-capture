from pxr import Usd, Gf
import omni.usd

PATH_OF_YOUR_PRIM = "/World/Cube" # HERE PUT THE VALUE WANTED
POSITION = Gf.Vec3d(0,50,0)
ROTATION = Gf.Vec3d(0,0,0)
SCALE = Gf.Vec3d(1,1,1)

stage: Usd.Stage = omni.usd.get_context().get_stage() 

if stage.GetPrimAtPath(PATH_OF_YOUR_PRIM).IsValid(): 
    prim = stage.GetPrimAtPath(PATH_OF_YOUR_PRIM)
    success= prim.GetAttribute("xformOp:translate").Set(Gf.Vec3d(POSITION), 0)
    print("Changed the position of the prim: ", success)
    success = prim.GetAttribute("xformOp:rotateXYZ").Set(Gf.Vec3d(ROTATION), 0)
    print("Changed the rotation of the prim: ", success)
    success = prim.GetAttribute("xformOp:scale").Set(Gf.Vec3d(SCALE), 0)
    print("Changed the scale of the prim: ", success)
else:
 	print("invalid")