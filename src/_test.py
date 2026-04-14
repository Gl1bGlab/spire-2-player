import os

from PIL import ImageChops, Image

from constants.project_constants import GameState, CARD_PORTRAIT_PATH
from constants.game_constants import CARDS, CardDataTypes
from game_window_handler import GameWindowHandler
from game_stat_handler import GameStatHandler
from card_obj import card_portrait_to_card, hand_to_cards
from __file_manager import *

from mouse import right_click

def main():
    window_manager = GameWindowHandler()
    stat_manager = GameStatHandler()
    stat_manager.set_hand_size(5)
    from PIL.Image import open
    curr_state = GameState.UNOPENED

    card_pos_order = [0,0,0,0,0]
    for i in range(5):
        print(stat_manager.hand_size.value)
        window_manager.play_card(card_pos_order[i], stat_manager)
        stat_manager.add_hand_size(-1)

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

