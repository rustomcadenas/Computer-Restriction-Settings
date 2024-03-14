import winreg as wrg
import ctypes, sys


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

def main():
    try: 
        location = wrg.HKEY_CURRENT_USER
        soft = wrg.OpenKeyEx(location, r"Software\\Microsoft\Windows\\CurrentVersion\\Policies\\")
        key = wrg.CreateKey(soft, "Explorer") 
        wrg.SetValueEx(key, "NoViewOnDrive", 0, wrg.REG_DWORD, 8)  #8 
        if key:
            wrg.CloseKey(key) 
            input("Press anything to exit. ")  
    except Exception as e:
        print(e)
        x = input(" ")   


if __name__ == "__main__":   
    
    if is_admin():
        main()
    else:
        rerun_as_admin()