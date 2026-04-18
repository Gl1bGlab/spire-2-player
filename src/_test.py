import os

import mouse
from PIL import ImageChops, Image, ImageGrab

from constants.project_constants import GameState, CARD_PORTRAIT_PATH, ENEMY_HEALTH_CAPTURE_AREA
from constants.game_constants import CARDS, CardDataTypes
from game_window_handler import GameWindowHandler
from game_stat_handler import GameStatHandler
from card_obj import card_portrait_to_card, hand_to_cards
from __file_manager import *

def find_color_rel_xy(img: Image, color: tuple[int, int, int])->tuple[int, int] | None:
    width, height = img.size

    for x in range(width):
        for y in range(height):
            if img.getpixel((x, y)) == color:
                return x, y
    return None



def main():
    window_manager = GameWindowHandler()
    stat_manager = GameStatHandler()
    stat_manager.set_hand_size(5)
    from PIL.Image import open
    curr_state = GameState.UNOPENED

    window_manager.check_and_grab_game_image()
    image = window_manager._cut_and_show_enemy_health()
    color = (255, 245, 225)
    #Y, X = numpy.where()
    xy = find_color_rel_xy(image, color)

    xy_factor = window_manager.find_xy_dimensions(ENEMY_HEALTH_CAPTURE_AREA, xy)
    # window_manager.mouse_to_factor_pos()
    print(xy_factor)

    # card_pos_order = [0, 0, 0, 0, 0]
    # for i in range(5):
    #     print(stat_manager.hand_size.value)
    #     window_manager.play_card(card_pos_order[i], stat_manager)
    #     stat_manager.add_hand_size(-1)

    # for card in hand_to_cards(window_manager, stat_manager):
    #     print(card)

    # scroll_and_gen(window_manager, stat_manager)

    # for card_name, card_dict in IMPORTANT_CARDS.items():
    #     print(card_portrait_to_card(open(card_dict[CardDataTypes.PORTRAIT_PATH]), 1))
        # open(IMPORTANT_CARDS[card]["path"]).show(card)

    # clear_temp()
    # for image in window_manager.scroll_hand(stat_manager):
    #     gen_image_file(image)

    curr_state = GameState.INIT

"""
TODO: 
- find location of enemy via health bar.
- play card on enemy.

- relic logic
- special card logic
(prepare to die edition)

- map navigation
(look for movement of nodes?)

- menuing
(probably a lot of image capture)
"""


main()

