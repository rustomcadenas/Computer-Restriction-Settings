import winreg as wrg
import ctypes, sys 
from pwinput import pwinput
import os

# ================================================================= Functions 
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

def CustomRestriction(settings):
    return True

    pass
    
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
        passkey = pwinput("\nPassword: ")  
        if passkey == "Jorarah":  
            menu = True 
            while(menu): 
                print(f"\nCurrent Values: {currentValue()}")
                print(f"Choices: \n\t[1]. ON Restrictions. \n\t[2]. Off Restrictions \n\t[C]. Custom Restrictions \n\t[R]. Restart PC \n\t[x]. Exit")
                selected = input("Choice: ")
                selected = "0" if selected == "2" else selected  
                if selected == "1" or selected == "0":  
                    print("On Restrictions") if selected == "1" else print("Off Restrictions")
                    if(changeValue(selected)):
                        print("Success! ")
                    else:   
                        print("Something went wrong") 
                elif selected == "r" or selected == "R":
                    ask = input("Restart Computer? [Y]Yes / [N]NO ")
                    if ask == "y" or ask == "Y": 
                        command = os.system(r"shutdown /r /t 0") 
                elif  selected == "c" or selected == "C":
                    print("\nCustom Restrictions: ")
                    print(f"Select Values you want to Activate! [1,2,3,5] \n\t[1]. No Control Panel. \n\t[2]. No Drive C \n\t[3]. No AutoRun \n\t[4]. No Start Menu Programs \n\t[5]. No Right Click \n\t[6]. Disable Drive D \n\t[x]. Cancel/Back")
                    custom_menu = input("Settings: ") 
                    print(custom_menu)
                else: 
                    menu = False
                    input("Exit")
        elif passkey == "ws":
            command = "start windowsdefender:"
            os.system(command)

        else:
            sys.exit() 
    else:
        rerun_as_admin()     