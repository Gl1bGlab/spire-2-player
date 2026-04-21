from os.path import dirname, join, normpath
from enum import Enum

SRC_PATH = normpath(join(dirname(__file__), ".."))
CARD_PORTRAIT_PATH = normpath(join(SRC_PATH, "constants\\img_constants\\card_portraits"))

ACCEPTABLE_IMAGE_DIFF = 20

MOUSE_MOVE_TIME = .5
MOUSE_PAUSE_TIME = .4

class GameState(Enum):
    UNOPENED = "unopened"
    INIT = "init"
    CHAR_SELECT = "char_select"

class FightState(Enum):
    PLAY_TURN = "play turn"
    END_TURN = "end turn"
    ENEMY_TURN = "enemy turn"
    FIGHT_END = "fight end"

# Hand sizes greater than 5 squish the cards closer per
# card added. This creates the need for specific calculations
# depending on how close the cards are with larger hands.
class HandSizeParameterTypes(Enum):
    BASE = "base"
    FIRST_CARD_FACTOR = "first card factor"
    INDEX_FACTOR = "index factor"
class HandSizes(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
HAND_SIZE_PARAMETERS = {
    HandSizes.ZERO: {
        HandSizeParameterTypes.BASE: None,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: None,
        HandSizeParameterTypes.INDEX_FACTOR: None,
    },
    HandSizes.ONE: {
        HandSizeParameterTypes.BASE: .33,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: .2,
        HandSizeParameterTypes.INDEX_FACTOR: 0,
    },
    HandSizes.TWO: {
        HandSizeParameterTypes.BASE: .33,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: .15,
        HandSizeParameterTypes.INDEX_FACTOR: .09,
    },
    HandSizes.THREE: {
        HandSizeParameterTypes.BASE: .33,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: .1,
        HandSizeParameterTypes.INDEX_FACTOR: .09,
    },
    HandSizes.FOUR: {
        HandSizeParameterTypes.BASE: .33,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: .05,
        HandSizeParameterTypes.INDEX_FACTOR: .09,
    },
    HandSizes.FIVE: {
        HandSizeParameterTypes.BASE: .33,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: 0,
        HandSizeParameterTypes.INDEX_FACTOR: .09,
    },
    HandSizes.SIX: {
        HandSizeParameterTypes.BASE: .27,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: 0,
        HandSizeParameterTypes.INDEX_FACTOR: .096,
    },
    HandSizes.SEVEN: {
        HandSizeParameterTypes.BASE: .22,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: 0,
        HandSizeParameterTypes.INDEX_FACTOR: .095,
    },
    HandSizes.EIGHT: {
        HandSizeParameterTypes.BASE: .2,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: 0,
        HandSizeParameterTypes.INDEX_FACTOR: .085,
    },
    HandSizes.NINE: {
        HandSizeParameterTypes.BASE: .18,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: 0,
        HandSizeParameterTypes.INDEX_FACTOR: .08,
    },
    HandSizes.TEN: {
        HandSizeParameterTypes.BASE: .17,
        HandSizeParameterTypes.FIRST_CARD_FACTOR: 0,
        HandSizeParameterTypes.INDEX_FACTOR: .075,
    },
}

# Game screen ratios for moving a card to a specific location
# and capturing its portriat.
BOTTOM_FACTOR_CONST = .05
CARD_CAPTURE_MOUSE_LOCATION = (.1, 0, 0, .03)
CARD_PORTRAIT_CAPTURE_AREA = (.04, .78, .84, .03)

ENEMY_HEALTH_CAPTURE_AREA = (.5, .6, .1, .27)
GENERIC_CARD_PLAY_LOCATION = (.5, 0, 0, .5)