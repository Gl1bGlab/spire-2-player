import psutil
import sys
from PIL import Image
from constants.project_constants import GameState

def check_if_opened() -> None:
    if "SlayTheSpire2.exe" in (p.name() for p in psutil.process_iter()):
        print("SlayTheSpire2.exe process found")
        return
    ans = input("SlayTheSpire2.exe not opened. Please either open the game or exit the program.\nExit the program? [y/n] ")
    if ans == "y":
        sys.exit()
    else:
        check_if_opened()

def find_portrait():
    try:
        portrait = Image.open("constants\\img_constants\\defect_portrait.jpg")
    except:
        raise Exception("Defect portrait image not found")