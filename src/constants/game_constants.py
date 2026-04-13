from enum import Enum
from os.path import join

from constants.project_constants import CARD_PORTRAIT_PATH

WINDOW_NAME = "Slay the Spire 2"

class DrawRelics(Enum):
    BAG_OF_PREP = "Bag of Preparation",
    CENT_PUZZLE = "Centennial Puzzle",
    PENDULUM = "Pendulum",
    GREM_HORN = "Gremlin Horn",
    JOSS_PAPER = "Joss Paper",
    GAME_PIECE = "Game Piece",
    PKTWATCH = "Pocketwatch",
    UNCEACING_T = "Unceasing Top",
    PWR_CELL = "Power Cell",
    BMING_CONCH = "Booming Conch",
    PAEL_BLOOD = "Pael's Blood",
    IRON_CLUB = "Iron Club",
    FIDDLE = "Fiddle",
    JEWEL_MASK = "Jeweled Mask",
    SNEK_EYE = "Snecko Eye",
    BIG_MUSH = "Big Mushroom",

class CardTypes(Enum):
    ATTACK = "attack"
    SKILL = "skill"
    POWER = "power"
    STATUS = "status"
    CURSE = "curse"

class SpecialTypes(Enum):
    VARIABLE_DRAW = "variable draw",
    CONSTANT_DRAW = "constant draw",
    SEARCH_AND_ADD = "search and add",
    SELECT_AND_EXHAUST = "select and exhaust",
    UNIQUE = "unique",

class CardDataTypes(Enum):
    PORTRAIT_PATH = "path",
    ENERGY_COST = "cost",
    SPECIAL = "special",
    DRAW_DIFF = "draw diff",
    TYPE = "type",
    PLAY_TYPE = "play type",

class PlayTypes(Enum):
    TARGET_ENEMY = "target enemy",
    NO_TARGET = "no target",

CARDS = {
    "Compile Driver": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Compile_Driver.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.ATTACK,

        CardDataTypes.SPECIAL: SpecialTypes.VARIABLE_DRAW,
    },
    "Coolheaded":{
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Coolheaded.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.SKILL,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.DRAW_DIFF: 1,
    },
    "Feral": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Feral.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.TYPE: CardTypes.ATTACK,
    },
    "FTL": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_FTL.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.TYPE: CardTypes.ATTACK,

        CardDataTypes.SPECIAL: SpecialTypes.VARIABLE_DRAW,
    },
    "Hologram": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Hologram.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.SKILL,

        CardDataTypes.SPECIAL: SpecialTypes.SEARCH_AND_ADD,
        CardDataTypes.DRAW_DIFF: 1,
    },
    "Iteration": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Iteration.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Neow's Fury": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Neows_Fury.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.ATTACK,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.DRAW_DIFF: 2,
    },
    "Overclock": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Overclock.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.TYPE: CardTypes.SKILL,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.DRAW_DIFF: 2,
    },
    "Rocket Punch": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Rocket_Punch.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.TYPE: CardTypes.ATTACK,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.DRAW_DIFF: 1,
    },
    "Scavenge": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Scavenge.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.SKILL,

        CardDataTypes.SPECIAL: SpecialTypes.SELECT_AND_EXHAUST,
        CardDataTypes.DRAW_DIFF: -1,
    },
    "Scrape": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Scrape.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.ATTACK,

        CardDataTypes.SPECIAL: SpecialTypes.VARIABLE_DRAW,
    },
    "Skim": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Skim.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.SKILL,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.DRAW_DIFF: 3,
    },
    "Slimed": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Slimed.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.STATUS,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.DRAW_DIFF: 1,
    },
    "Sweeping Beam": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Sweeping_Beam.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.ATTACK,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.DRAW_DIFF: 1,
    },
    "Uproar": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Uproar.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.ATTACK,

        CardDataTypes.SPECIAL: SpecialTypes.VARIABLE_DRAW,
    },
    "White Noise": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_White_Noise.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.TYPE: CardTypes.SKILL,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.DRAW_DIFF: 1,
    },
}

