import mouse
import sys
from PIL import Image, ImageGrab
from win32 import win32api, win32gui

from constants.project_constants import GameState
from game_window_handler import GameWindowHandler

def main():
    window_manager = GameWindowHandler()
    curr_state = GameState.UNOPENED

    window_manager.curr_image.show()

    curr_state = GameState.INIT
    # defect_portrait = Image.open("constants\\img_constants\\defect_portrait.jpg")
    # data = defect_portrait.get_flattened_data(0)

main()