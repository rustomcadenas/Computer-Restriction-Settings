import winreg as wrg
import ctypes, sys 
from pwinput import pwinput

def currentValue():
    location = wrg.HKEY_CURRENT_USER
    soft = wrg.OpenKeyEx(location, r"Software\\Microsoft\Windows\\CurrentVersion\\Policies\\Explorer")
    value = wrg.QueryValueEx(soft, "NoViewContextMenu")
    if soft:
        wrg.CloseKey(soft)
    return value[0]

def changeValue(value):  
    value = 1 if value=="1" else 0
    
    try:   
        location = wrg.HKEY_CURRENT_USER
        soft = wrg.OpenKeyEx(location, r"Software\\Microsoft\Windows\\CurrentVersion\\Policies\\")
        key = wrg.CreateKey(soft, "Explorer") 
        if value == 1: 
            wrg.SetValueEx(key, "NoControlPanel", 0, wrg.REG_DWORD, 1)  #1
            wrg.SetValueEx(key, "NoDrives", 0, wrg.REG_DWORD, 4) #4
            wrg.SetValueEx(key, "NoDriveTypeAutoRun", 0, wrg.REG_DWORD, 145) #145
            wrg.SetValueEx(key, "NoStartMenuMorePrograms", 0, wrg.REG_DWORD, 1) #1
            wrg.SetValueEx(key, "NoViewContextMenu", 0, wrg.REG_DWORD, 1) #1
            wrg.SetValueEx(key, "NoViewOnDrive", 0, wrg.REG_DWORD, 8)  #8
        else: 
            wrg.SetValueEx(key, "NoControlPanel", 0, wrg.REG_DWORD, 0)  #1
            wrg.SetValueEx(key, "NoDrives", 0, wrg.REG_DWORD, 0) #4
            wrg.SetValueEx(key, "NoDriveTypeAutoRun", 0, wrg.REG_DWORD, 0) #145
            wrg.SetValueEx(key, "NoStartMenuMorePrograms", 0, wrg.REG_DWORD, 0) #1
            wrg.SetValueEx(key, "NoViewContextMenu", 0, wrg.REG_DWORD, 0) #1
            wrg.SetValueEx(key, "NoViewOnDrive", 0, wrg.REG_DWORD, 0)  #8
        if key:
            wrg.CloseKey(key) 
            return True        
    except Exception as e:
        return False 
    

# ================================================================================== IS ADMIN
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def rerun_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        'reg.exe',
        None,
        1
    ) 

# ======================================================================================= MAIN
if __name__ == "__main__": 
    if is_admin():  
        passkey = pwinput("Password: ")
        if passkey != "tomasgwapo":
            sys.exit() 
        menu = True 
        while(menu): 
            print(f"\nCurrent Values: {currentValue()}")
            print(f"Choices: \n\t[1]. ON Restrictions. \n\t[2]. Off Restrictions \n\t[any]. Exit")
            selected = input("Choice: ")
            selected = "0" if selected == "2" else selected  
            if selected == "1" or selected == "0":
                if(changeValue(selected)):
                    print("Success! ")
                else:
                    print("Something went wrong") 
            else: 
                menu = False
                input("Exit")
    else:
        rerun_as_admin()     