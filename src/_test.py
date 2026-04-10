import os

from PIL import ImageChops, Image

from constants.project_constants import GameState, CARD_PORTRAIT_PATH
from constants.game_constants import IMPORTANT_CARDS
from game_window_handler import GameWindowHandler
from game_stat_handler import GameStatHandler
from card_obj import card_creator
from __file_manager import *

def main():
    # window_manager = GameWindowHandler()
    # game_stat_manager = GameStatHandler()
    # game_stat_manager.set_hand_size(1)
    from PIL.Image import open
    curr_state = GameState.UNOPENED
    for card in IMPORTANT_CARDS:
        open(IMPORTANT_CARDS[card]["path"]).show(card)

    # clear_temp()
    # for image in window_manager.scroll_hand(game_stat_manager):
    #     gen_image_file(image)

    curr_state = GameState.INIT

"""
TODO: Create a dictionary of dictionaries of cards including 
the card's name, 
portrait path,
etc??? (think ab this later)
"""

main()

