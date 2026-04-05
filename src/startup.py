import sys
from PIL import Image
from win32 import win32gui
from constants.project_constants import GameState

game_window = None




        
def find_portrait():
    try:
        portrait = Image.open("constants\\img_constants\\defect_portrait.jpg")
    except:
        raise Exception("Defect portrait image not found")