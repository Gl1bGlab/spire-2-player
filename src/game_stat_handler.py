from PIL import ImageChops
from PIL.Image import Image

from constants.project_constants import (GameState, BOTTOM_FACTOR_CONST,
ACCEPTABLE_IMAGE_DIFF, HAND_SIZE_PARAMETERS, HandSizeParameterTypes, HandSizes)
from constants.game_constants import DrawRelics, CARDS, CardDataTypes
from card_obj import Card

class StatHandler():
    def __init__(self):
        self._game_state: GameState = GameState.INIT
        self._draw_relics: list[DrawRelics] = []
        self._deck_size: int = 10

    def __repr__(self):
        return f"""GameStatHandler(
    game_state={self._game_state},
    draw_relics={self._draw_relics},
    deck_size={self._deck_size}
)"""
