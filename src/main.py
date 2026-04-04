import mouse
import sys

from PIL import Image, ImageGrab
from win32 import win32api

from constants.project_constants import GameState, SCREEN_HEIGHT, SCREEN_WIDTH
from startup import check_if_opened


def main():
    curr_state = GameState.UNOPENED
    check_if_opened()

    curr_state = GameState.INIT
    print(SCREEN_HEIGHT/SCREEN_WIDTH)
    defect_portrait = Image.open("constants\\img_constants\\defect_portrait.jpg")
    data = defect_portrait.get_flattened_data(0)

main()