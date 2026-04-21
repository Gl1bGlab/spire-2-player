from PIL import ImageChops
from PIL.Image import Image

from constants.project_constants import (GameState, BOTTOM_FACTOR_CONST,
ACCEPTABLE_IMAGE_DIFF, HAND_SIZE_PARAMETERS, HandSizeParameterTypes, HandSizes)
from constants.game_constants import DrawRelics, CARDS, CardDataTypes
from card_obj import Card

class StatHandler():
    def __init__(self):
        self.game_state: GameState = GameState.INIT
        self.draw_relics: list[DrawRelics] = []

        self.hand_size: HandSizes = HandSizes.FIVE
        self.hand: list[Card]|None = None
        self.curr_turn: int = 0

    def __repr__(self):
        return f"""GameStatHandler(
    game_state={self.game_state},
    hand_size={self.hand_size},
    draw_relics={self.draw_relics},
    curr_turn={self.curr_turn},
)"""
