from PIL import ImageChops
from PIL.Image import Image

from constants.project_constants import (GameState, BOTTOM_FACTOR_CONST,
ACCEPTABLE_IMAGE_DIFF, HAND_SIZE_PARAMETERS, HandSizeParameterTypes, HandSizes)
from constants.game_constants import DrawRelics, CARDS, CardDataTypes
from card_obj import Card

class StatHandler():
    def __init__(self):
        self.game_state: GameState = GameState.INIT
        self.draw_relics: list[DrawRelics]|list = []
        self.default_draw: int = 5
        self.deck_size: int = 10
        self.default_energy: int = 3

    def __repr__(self):
        return f"""GameStatHandler(
    game_state={self.game_state},
    draw_relics={self.draw_relics},
    deck_size={self.deck_size},
    starting_energy={self.default_energy},
)"""
