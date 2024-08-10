import os
from tkinter import Tk
from tkinter.filedialog import askdirectory 

os.system("title MatterManager: Relaxed Squirrel")

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
starbound_directory = askdirectory(title="Select your Starbound directory")

## CONFIGURATION START

#starbound_directory = "C:\\Program Files (x86)\\Steam\\steamapps\common\Starbound"

## CONFIGURATION END

def main_menu():
    print("MatterManager: Relaxed Squirrel")
    print("[1] Profile Manager")
    print("[2] Start Starbound")

    choice = input()
    if choice == "1":
        print("WOAH!")
    elif choice == "2":
        os.system("\""+ starbound_directory + "/win64/starbound.exe\"")
    else:
        main_menu()

main_menu()

input()