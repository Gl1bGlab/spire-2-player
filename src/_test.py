import uuid

from PIL import ImageChops, Image
import PIL

from constants.project_constants import GameState
from game_window_handler import GameWindowHandler
from game_stat_handler import GameStatHandler
from __file_manager import *

# thx to https://www.geeksforgeeks.org/python/find-most-used-colors-in-image-using-python/
def count_color(img: Image)->float:
    width, height = img.size
    total = 0
    count = 0

    for x in range(0, width):
        for y in range(0, height):
            for color in img.getpixel((x, y)):
                total += color
            count += 1
    return total/count



def main():
    window_manager = GameWindowHandler()
    game_stat_manager = GameStatHandler()
    game_stat_manager.set_hand_size(1)
    curr_state = GameState.UNOPENED
    # first_card = window_manager.scroll_hand(game_stat_manager)[0]
    # for img1 in range(3):
    #     for img2 in os.listdir("constants\\img_constants"):
    #         image1 = Image.open(img1)
    #         image2 = Image.open(img2)

    #         print(count_color(ImageChops.difference(image1, image2)))

    # clear_temp()
    # for image in window_manager.scroll_hand(game_stat_manager):
    #     gen_image_file(image)

    curr_state = GameState.INIT


main()