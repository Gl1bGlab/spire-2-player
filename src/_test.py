import os

from PIL import ImageChops, Image

from constants.project_constants import GameState, CARD_PORTRAIT_PATH
from constants.game_constants import CARDS, CardDataTypes
from game_window_handler import GameWindowHandler
from game_stat_handler import GameStatHandler
from card_obj import card_portrait_to_card, hand_to_cards
from __file_manager import *

def main():
    window_manager = GameWindowHandler()
    stat_manager = GameStatHandler()
    stat_manager.set_hand_size(3)
    from PIL.Image import open
    curr_state = GameState.UNOPENED

    for card in hand_to_cards(window_manager, stat_manager):
        print(card)

    # scroll_and_gen(window_manager, stat_manager)

    # for card_name, card_dict in IMPORTANT_CARDS.items():
    #     print(card_portrait_to_card(open(card_dict[CardDataTypes.PORTRAIT_PATH]), 1))
        # open(IMPORTANT_CARDS[card]["path"]).show(card)

    # clear_temp()
    # for image in window_manager.scroll_hand(stat_manager):
    #     gen_image_file(image)

    curr_state = GameState.INIT

"""
TODO: right now, you're trying to fix an import error.
after that, make sure the refactoring you did with the hand size factors works.
after THAT, figure out playing cards.
then move on to menuing and you should be done whenever that is.
ALSO: remember to add relic logic.
"""


main()

