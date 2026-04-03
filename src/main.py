import mouse
from PIL import Image, ImageGrab
from win32 import win32api
from constants.project_constants import GameState, SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    curr_state = GameState.INIT
    print(SCREEN_HEIGHT//SCREEN_WIDTH)
    defect_portrait = Image.open("constants\\img-constants\\defect-portrait.jpg")
    defect_portrait.show()
    while curr_state == GameState.INIT:
        break



main()