import os
import time

try:
    path=os.path.expanduser('~')+"/AppData/Local/Bloxstrap/Roblox/Player"
    time.sleep(3)
    os.rename(path+"/RobloxPlayerBeta.exe", path+"/Minecraft.exe")
except Exception:
    pass

