# # from tkinter import messagebox
# import winreg
# from pyuac import main_requires_admin

 
# def NoViewContextMenu(value):
#     values = 1 if value == 1 else 0
#     key = "NoViewContextMenu" 
# # HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer
#     try:
#         reg_key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer', 0, winreg.KEY_SET_VALUE)
#         winreg.SetValueEx(reg_key, key, 0, winreg.REG_DWORD, values)
#         return "Success"
#     except Exception as e:
#         return "Something went wrong!", e



# @main_requires_admin
# def main():
#     dagan = True
#     while dagan:
#         print("1: On | 0 : off")
#         x = input("Input: ")
#         if x == "x":
#             print("Exit")
#             dagan = False 
#         else:
#             print(NoViewContextMenu(x))



# if __name__ == "__main__": 
#     main()
    

import winreg
import os

if __name__ == "__main__":
    print("Hello WOrld")
    try:
        key_val = r"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\NoViewContextMenu"
        if not os.path.exists("keyval"):
            key = winreg.CreateKey("HKEY_CURRENT_USER", key_val)
        RegistryKey = winreg.OpenKey("HKEY_CURRENT_USER", key_val, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(RegistryKey, "NoViewContextMenu", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(RegistryKey)
        print("Success...")
    except Exception as e:
        print(e)

