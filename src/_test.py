import os

import mouse
from PIL import ImageChops, Image, ImageGrab
from PIL.Image import open

from constants.project_constants import CARD_PORTRAIT_PATH, ENEMY_HEALTH_CAPTURE_AREA, \
LOOT_RIBBON_CAPTURE_AREA
from constants.game_constants import CARDS, CardDataTypes, ENEMY_HEALTH_COLORS
from window_handler import WindowHandler
from stat_handler import StatHandler
from fight_handler import FightHandler
from card_helpers import card_portrait_to_card
from __file_manager import *

def main():
    stat_manager = StatHandler()
    window_manager = WindowHandler()
    fight_manager = FightHandler(stat_manager, window_manager)
    # fight_manager.set_hand_size(5)

    window_manager.grab_and_cut_window_image(LOOT_RIBBON_CAPTURE_AREA).show()
    
    # fight_manager.play_turn()

    # fight_manager.hand_to_cards()
    # for i in range(fight_manager._curr_hand_size.value):
    #     print(fight_manager)
    #     fight_manager.play_card_data(fight_manager._curr_hand[0])

    # print(fight_manager)
    # print(fight_manager.window_handler)
    # print(fight_manager.stat_handler)
    # fight_manager.hand_to_cards()
    # for card in fight_manager._curr_hand:
    #     print(card)

    # clear_temp()
    # scroll_and_gen(window_manager, stat_manager)

    # clear_temp()
    # for image in window_manager.scroll_hand(stat_manager):
    #     gen_image_file(image)


"""
TODO: 
- card playing logic
(i'm going to die edition)

- relic logic
- special card logic
(prepare to die edition)

- map navigation
(look for movement of nodes?)

- menuing
(probably a lot of image capture)
"""


main()

