from win32 import win32gui
from PIL import Image, ImageGrab

from startup import get_game_window
from constants.game_constants import WINDOW_NAME
from constants.project_constants import WH_SCREEN_RATIO

def game_window_still_exists_check(game_window):
    if win32gui.GetWindowText(game_window) == WINDOW_NAME:
        return game_window
    else:
        return get_game_window()
def game_window_foreground_check(game_window) -> None:
    msg_printed = False
    while win32gui.GetForegroundWindow() != game_window:
        if not msg_printed:
            print("Waiting for Slay the Spire 2 to be the foreground window")
            msg_printed = True
        pass
def game_screen_grab(game_window) -> Image:
    window_dimentions = win32gui.GetWindowRect(game_window)
    left, top, right, bottom = window_dimentions
    height =  bottom - top
    width = right - left

    if width/height != WH_SCREEN_RATIO:
        # ???
    game_screen = ImageGrab.grab().crop(window_dimentions)
    return game_screen

def check_and_grab_game_image(game_window) -> Image:
    game_window = game_window_still_exists_check(game_window)
    game_window_foreground_check(game_window)
    return game_screen_grab(game_window)

