from os.path import dirname, join, normpath
from enum import Enum

# Paths of images (and the src dir)
SRC_PATH = normpath(join(dirname(__file__), ".."))
IMG_CONSTANTS_PATH = normpath(join(SRC_PATH, "constants\\img_constants"))
CARD_PORTRAIT_PATH = normpath(join(IMG_CONSTANTS_PATH, "card_portraits"))
BUTTONS_PATH = normpath(join(IMG_CONSTANTS_PATH, "buttons"))

# The images of the card portraits aren't always perfect, so a bit of difference
# is normal.
ACCEPTABLE_IMAGE_DIFF = 20

# The mouse should take a moment to move through different actions
# to make sure nothing's getting in the way of getting clean images
# of the game.
# ex: Moving too fast for a good shot of card portriats
MOUSE_MOVE_TIME = .5
MOUSE_PAUSE_TIME = .4

#States the game can be in
class GameState(Enum):
    UNOPENED = "unopened"
    INIT = "init"
    CHAR_SELECT = "char_select"
class FightState(Enum):
    PLAY_TURN = "play turn"
    END_TURN = "end turn"
    ENEMY_TURN = "enemy turn"
    LOOTING = "looting"
    FIGHT_WON = "fight finished"
    DEAD = "died"

# The game runs at a constant 16/9 width/height ratio. I WAS going to try
# making the game playable at any window size (within reason), so it would be important
# to cut screen images to this constant ratio. I ran into a problem
# where the image was always a bit off, so I scrapped it. FULLSCREEN ONLY!!!
W_FACTOR = 16
H_FACTOR = 9
WH_SCREEN_RATIO = .5625
TITLE_BAR_SIZE = 22

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

CARD_PORTRAIT_CAPTURE_AREA = (.04, .78, .84, .03)
ENEMY_HEALTH_CAPTURE_AREA = (.5, .6, .1, .27)
LOOT_CAPTURE_AREA = (.5, .38, .49, .61)


class MouLocNames(Enum):
    CARD_CAPTURE = "card capture"
    GENERIC_CARD_PLAY = "middle card play"
    END_TURN_BUTTON = "end turn button"
    LOOT = "loot"
    PROCEED_BUTTON = "proceed button"
    MIDDLE_CARD_CHOICE = "middle card choice"
MOUSE_LOCATIONS: dict[tuple[float, float, float, float]] = {
    MouLocNames.CARD_CAPTURE: (.1, 0, 0, .03),
    MouLocNames.GENERIC_CARD_PLAY: (.5, 0, 0, .5),
    MouLocNames.END_TURN_BUTTON: (.9, 0, 0, .17),
    MouLocNames.LOOT: (.5, 0, 0, .61),
    MouLocNames.PROCEED_BUTTON: (.9, 0, 0, .23),
    MouLocNames.MIDDLE_CARD_CHOICE: (.5, 0, 0, .5),
}
