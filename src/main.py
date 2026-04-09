import mouse
import sys
import pytesseract
from PIL import Image, ImageGrab
from win32 import win32api, win32gui

from constants.project_constants import GameState
from game_window_handler import GameWindowHandler
from game_stat_handler import GameStatHandler

def main():
    window_manager = GameWindowHandler()
    game_stat_manager = GameStatHandler()
    game_stat_manager.set_hand_size(6)
    curr_state = GameState.UNOPENED


    print(window_manager.scroll_hand(game_stat_manager))
    # for image in window_manager.scroll_hand(game_stat_manager):
    #     image.show()

    curr_state = GameState.INIT
    # defect_portrait = Image.open("constants\\img_constants\\defect_portrait.jpg").convert("RGB").quantize(colors=100)
    # defect_portrait.show()
    # data = defect_portrait.getcolors(maxcolors=100)
    # print(data)


main()