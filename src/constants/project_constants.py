from os.path import dirname, join, normpath
from enum import Enum

SRC_PATH = normpath(join(dirname(__file__), ".."))
CARD_PORTRAIT_PATH = normpath(join(SRC_PATH, "constants\\img_constants\\card_portraits"))

ACCEPTABLE_IMAGE_DIFF = 15

class GameState(Enum):
    UNOPENED = "unopened",
    INIT = "init",
    CHAR_SELECT = "char_select",
    
# Hand sizes greater than 5 squish the cards closer per
# card added. This creates the need for specific calculations
# depending on how close the cards are with larger hands.
class HandSizeCategories(Enum):
    ZERO = "hand size: 0",
    LOW = "low hand sizes: 1, 2, 3, 4, 5",
    SIX = "hand size: 6",
    SEVEN = "hand size: 7",
    EIGHT = "hand size: 8",
    NINE = "hand size: 9",
    TEN = "hand size: 10",