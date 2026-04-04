import mouse
import sys

from PIL import Image, ImageGrab
from win32 import win32api, win32gui

from constants.project_constants import GameState, SCREEN_HEIGHT, SCREEN_WIDTH
from startup import get_game_window
from gen_helpers import game_window_foreground_check

def main():
    curr_state = GameState.UNOPENED
    game_window = get_game_window()
    print(hex(win32gui.GetForegroundWindow()))

    game_window_foreground_check(game_window)

    curr_state = GameState.INIT
    print(SCREEN_HEIGHT/SCREEN_WIDTH)
    defect_portrait = Image.open("constants\\img_constants\\defect_portrait.jpg")
    data = defect_portrait.get_flattened_data(0)

main()