# Read Registry Key
# import winreg as wrg 
# if __name__ == "__main__": 
#     location = wrg.HKEY_CURRENT_USER
#     soft = wrg.OpenKeyEx(location, r"Software\\Microsoft\Windows\\CurrentVersion\\Policies\\Explorer")
#     value = wrg.QueryValueEx(soft, "NoViewContextMenu")
#     if soft:
#         wrg.CloseKey(soft)
#     print(value)
# create Registry Key

import winreg as wrg  
import ctypes, sys
 
if __name__ == "__main__":   
    ctypes.windll.ShellExecuteW(None, 'runas', sys.executable, 'reg.exe', None, 1)
    try:
        
        location = wrg.HKEY_CURRENT_USER
        soft = wrg.OpenKeyEx(location, r"Software\\Microsoft\Windows\\CurrentVersion\\Policies\\")
        key = wrg.CreateKey(soft, "Explorer")
        # wrg.SetValueEx(key, "NoControlPanel", 0, wrg.REG_DWORD, 1)  #1
        # wrg.SetValueEx(key, "NoDrives", 0, wrg.REG_DWORD, 4) #4
        # wrg.SetValueEx(key, "NoDriveTypeAutoRun", 0, wrg.REG_DWORD, 145) #145
        # wrg.SetValueEx(key, "NoStartMenuMorePrograms", 0, wrg.REG_DWORD, 1) #1
        # wrg.SetValueEx(key, "NoViewContextMenu", 0, wrg.REG_DWORD, 1) #1
        # wrg.SetValueEx(key, "NoViewOnDrive", 0, wrg.REG_DWORD, 8)  #8

        # wrg.SetValueEx(key, "NoControlPanel", 0, wrg.REG_DWORD, 0)  #1
        # wrg.SetValueEx(key, "NoDrives", 0, wrg.REG_DWORD, 0) #4
        # wrg.SetValueEx(key, "NoDriveTypeAutoRun", 0, wrg.REG_DWORD, 0) #145
        # wrg.SetValueEx(key, "NoStartMenuMorePrograms", 0, wrg.REG_DWORD, 0) #1
        # wrg.SetValueEx(key, "NoViewContextMenu", 0, wrg.REG_DWORD, 0) #1
        wrg.SetValueEx(key, "NoViewOnDrive", 0, wrg.REG_DWORD, 1)  #8

        if key:
            wrg.CloseKey(key) 
            input("Press anything to exit. ")


    except Exception as e:
        print(e)
        x = input(" ") 
 