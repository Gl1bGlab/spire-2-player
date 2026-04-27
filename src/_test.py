import os

import mouse
from PIL import ImageChops, Image, ImageGrab, ImageShow
from PIL.Image import open

from constants.project_constants import CARD_PORTRAIT_PATH, ENEMY_HEALTH_CAPTURE_AREA, \
LOOT_CAPTURE_AREA, MOUSE_LOCATIONS, MouLocNames
from constants.game_constants import CARDS, CardDataTypes, ENEMY_HEALTH_COLORS
from window_handler import WindowHandler
from stat_handler import StatHandler
from fight_handler import FightHandler
from card_helpers import card_portrait_to_card
from __file_manager import *

def test():
    stat_manager = StatHandler()
    window_manager = WindowHandler()
    fight_manager = FightHandler(stat_manager, window_manager)

    fight_manager.start_combat()

    # fight_manager.window_handler.mouse_to_mouse_location(MOUSE_LOCATIONS[MouLocNames.LOOT])
    "gen image of specific area"
    # fight_manager.window_handler._show_cut_image(LOOT_CAPTURE_AREA)
    # gen_factor_image(fight_manager, LOOT_CAPTURE_AREA)

    "test specific hand size"
    # fight_manager.set_hand_size(5)

    "test area to grab and mouse location"
    # window_manager.mouse_to_factor_pos(PROCEED_BUTTON_LOCATION)
    # ImageShow.show(window_manager.grab_and_cut_window_image(LOOT_CAPTURE_AREA))
    
    "test play turn"
    # fight_manager.play_turn()

    "test converting hand to cards"
    # fight_manager.hand_to_cards()
    # for i in range(fight_manager._curr_hand_size.value):
    #     print(fight_manager)
    #     fight_manager.play_card_data(fight_manager._curr_hand[0])

    "show fight manager and card details"
    # print(fight_manager)
    # print(fight_manager.window_handler)
    # print(fight_manager.stat_handler)
    # fight_manager.hand_to_cards()
    # for card in fight_manager._curr_hand:
    #     print(card)

    "generate new card portraits"
    # clear_temp()
    # scroll_and_gen(window_manager, stat_manager)

"""
TODO: 
- handle da loot screen
    -potions, pick a card
- reset on death

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

test()

