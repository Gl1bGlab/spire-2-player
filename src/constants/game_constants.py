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

IMPORTANT_CARDS = {
    "Compile Driver": {
        "path": join(CARD_PORTRAIT_PATH, "_Compile_Driver.png"),
        "cost": 1,
    },
    "Coolheaded":{
        "path": join(CARD_PORTRAIT_PATH, "_Coolheaded.png"),
        "cost": 1,
    },
    "Feral": {
        "path": join(CARD_PORTRAIT_PATH, "_Feral.png"),
        "cost": 2,
    },
    "FTL": {
        "path": join(CARD_PORTRAIT_PATH, "_FTL.png"),
        "cost": 0,
    },
    "Hologram": {
        "path": join(CARD_PORTRAIT_PATH, "_Hologram.png"),
        "cost": 1,
    },
    "Iteration": {
        "path": join(CARD_PORTRAIT_PATH, "_Iteration.png"),
        "cost": 1,
    },
    "Overclock": {
        "path": join(CARD_PORTRAIT_PATH, "_Overclock.png"),
        "cost": 0,
    },
    "Scavenge": {
        "path": join(CARD_PORTRAIT_PATH, "_Scavenge.png"),
        "cost": 1,
    },
    "Scrape": {
        "path": join(CARD_PORTRAIT_PATH, "_Scrape.png"),
        "cost": 1,
    },
    "Skim": {
        "path": join(CARD_PORTRAIT_PATH, "_Skim.png"),
        "cost": 1,
    },
    "Slimed": {
        "path": join(CARD_PORTRAIT_PATH, "_Slimed.png"),
        "cost": 1,
    },
    "Sweeping Beam": {
        "path": join(CARD_PORTRAIT_PATH, "_Sweeping_Beam.png"),
        "cost": 1,
    },
    "Uproar": {
        "path": join(CARD_PORTRAIT_PATH, "_Uproar.png"),
        "cost": 1,
    },
    "White Noise": {
        "path": join(CARD_PORTRAIT_PATH, "_White_Noise.png"),
        "cost": 1,
    },
}