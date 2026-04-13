from os.path import dirname, join, normpath
from enum import Enum

SRC_PATH = normpath(join(dirname(__file__), ".."))
CARD_PORTRAIT_PATH = normpath(join(SRC_PATH, "constants\\img_constants\\card_portraits"))

ACCEPTABLE_IMAGE_DIFF = 20

class GameState(Enum):
    UNOPENED = "unopened",
    INIT = "init",
    CHAR_SELECT = "char_select",
    
# Hand sizes greater than 5 squish the cards closer per
# card added. This creates the need for specific calculations
# depending on how close the cards are with larger hands.

class HandSizeParameterTypes(Enum):
    BASE = "base",
    FIRST_CARD_FACTOR = "first card factor",
    INDEX_FACTOR = "index factor",

class HandSizes(Enum):
    ZERO = "zero",
    ONE = "one",
    TWO = "two",
    THREE = "three",
    FOUR = "four",
    FIVE = "five",
    SIX = "six",
    SEVEN = "seven",
    EIGHT = "eight",
    NINE = "nine",
    TEN = "ten",

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

BOTTOM_FACTOR_CONST = .05