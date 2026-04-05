import mouse
import sys
from PIL import Image, ImageGrab
from win32 import win32api, win32gui

from constants.project_constants import GameState
from startup import get_game_window
from src.window_stuff import check_and_grab_game_image

def main():
    curr_state = GameState.UNOPENED
    game_window = get_game_window()
    print(hex(win32gui.GetForegroundWindow()))

    image = check_and_grab_game_image(game_window)
    image.show()

    curr_state = GameState.INIT
    # defect_portrait = Image.open("constants\\img_constants\\defect_portrait.jpg")
    # data = defect_portrait.get_flattened_data(0)

main()