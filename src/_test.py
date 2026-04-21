import os

import mouse
from PIL import ImageChops, Image, ImageGrab

from constants.project_constants import GameState, CARD_PORTRAIT_PATH, ENEMY_HEALTH_CAPTURE_AREA
from constants.game_constants import CARDS, CardDataTypes, ENEMY_HEALTH_COLORS
from game_window_handler import WindowHandler
from game_stat_handler import StatHandler
from fight_handler import FightHandler
from card_helpers import card_portrait_to_card
from __file_manager import *

def main():
    stat_manager = StatHandler()
    window_manager = WindowHandler()
    fight_manager = FightHandler(stat_manager, window_manager)
    fight_manager.set_hand_size(5)
    from PIL.Image import open
    curr_state = GameState.UNOPENED
    mouse.move(0,0)

    # mouse.move(0,0, duration=1)
    # window_manager.mouse_to_enemy()

    # card_pos_order = [0, 0, 0, 0, 0]
    # for i in range(5):
    #     print(stat_manager.hand_size.value)
    #     window_manager.play_card(card_pos_order[i], stat_manager)
    #     stat_manager.add_hand_size(-1)

    fight_manager.hand_to_cards()
    for card in fight_manager._curr_hand:
        print(card)

    # clear_temp()
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
- keep trucking
- out with the old...
- ensure a card knows how much energy it's giving/taking

- relic logic
- special card logic
(prepare to die edition)

- map navigation
(look for movement of nodes?)

- menuing
(probably a lot of image capture)
"""


main()

