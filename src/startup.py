import sys
from PIL import Image
from win32 import win32gui
from constants.project_constants import GameState

game_window = None

# thx to Pedro Lobito from https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
def find_StS2(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        if win32gui.GetWindowText(hwnd) != "Slay the Spire 2":
            return
        global game_window
        game_window = hwnd
        print(f"Slay the Spire 2 window found at {hex(hwnd)}")

def get_game_window() -> int:
    win32gui.EnumWindows(find_StS2, None)
    if game_window == None:
        raise Exception("Slay the Spire 2 window not found, please open the game\nIf the game is opened, make sure the name of the window is Slay the Spire 2")
    return game_window
        
def find_portrait():
    try:
        portrait = Image.open("constants\\img_constants\\defect_portrait.jpg")
    except:
        raise Exception("Defect portrait image not found")