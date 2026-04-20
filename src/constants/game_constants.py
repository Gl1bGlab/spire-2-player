from enum import Enum
from os.path import join

from constants.project_constants import CARD_PORTRAIT_PATH

WINDOW_NAME = "Slay the Spire 2"

class DrawRelics(Enum):
    BAG_OF_PREP = "Bag of Preparation"
    CENT_PUZZLE = "Centennial Puzzle"
    PENDULUM = "Pendulum"
    GREM_HORN = "Gremlin Horn"
    JOSS_PAPER = "Joss Paper"
    GAME_PIECE = "Game Piece"
    PKTWATCH = "Pocketwatch"
    UNCEACING_T = "Unceasing Top"
    PWR_CELL = "Power Cell"
    BMING_CONCH = "Booming Conch"
    PAEL_BLOOD = "Pael's Blood"
    IRON_CLUB = "Iron Club"
    FIDDLE = "Fiddle"
    JEWEL_MASK = "Jeweled Mask"
    SNEK_EYE = "Snecko Eye"
    BIG_MUSH = "Big Mushroom"

class CardTypes(Enum):
    ATTACK = "attack"
    SKILL = "skill"
    POWER = "power"
    STATUS = "status"
    CURSE = "curse"

class SpecialTypes(Enum):
    DRAW_DIFF = "variable draw"
    CONSTANT_DRAW = "constant draw"
    STATUS_TO_DISCARD = "add status to discard"
    DISCARD_OTHER_THAN_ONE = "cards to discard != 1"

    SEARCH_AND_ADD = "search and add"
    SELECT_AND_EXHAUST = "select and exhaust"

    ENERGY_DIFF = "more energy info than cost"
    ENERGY_DIFF_AND_DRAW = "constant draw + energy diff"

    TRACK_TIMES_PLAYED = "track how much the card's been played"
    UNIQUE = "unique"
    AVOID = "AVOID"

class CardDataTypes(Enum):
    PORTRAIT_PATH = "path"
    ENERGY_COST = "cost"
    TOTAL_ENERGY_COST = "energy diff"
    SPECIAL = "special"
    CARDS_ADDED_TO_HAND = "draw diff"
    DISCARD_DIFF = "discard diff"
    TYPE = "type"
    PLAY_TYPE = "play type"
    CREATED_STATUSES = "created status"
    KEYWORDS = "keywords"

class PlayTypes(Enum):
    TARGET_ENEMY = "target enemy"
    NO_TARGET = "no target"

class CardKeywords(Enum):
    ETHEREAL = "ethereal"
    EXHAUST = "exhaust"
    UNPLAYABLE = "unplayable"

CARDS: dict[CardDataTypes] = {
    "Adaptive Strike": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Adaptive_Strike.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.DISCARD_OTHER_THAN_ONE,
        CardDataTypes.DISCARD_DIFF: 2,
    },
    "All for One": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_All_for_One.png"),
        CardDataTypes.SPECIAL: SpecialTypes.AVOID
    },
    "Ball Lightning": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Ball_Lightning.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "Barrage": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Barrage.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "Beam Cell": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Beam_Cell.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "Boost Away": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Boost_Away.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.STATUS_TO_DISCARD,
        CardDataTypes.DISCARD_DIFF: 2,
        CardDataTypes.CREATED_STATUSES: ["Dazed"],
    },
    "Boot Sequence": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Boot_Sequence.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.KEYWORDS: [CardKeywords.EXHAUST],
    },
    "Buffer": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Buffer.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Bulk Up": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Bulk_Up.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Capacitor": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Capacitor.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Chaos": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Chaos.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Charge Battery": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Charge_Battery.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Chill": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Chill.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.KEYWORDS: [CardKeywords.EXHAUST],
    },
    "Claw": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Claw.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "Clumsy": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Clumsy.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.KEYWORDS: [CardKeywords.UNPLAYABLE, CardKeywords.ETHEREAL],
    },
    "Cold Snap": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Cold_Snap.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "Compact": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Compact.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE,
    },
    "Compile Driver": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Compile_Driver.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.DRAW_DIFF,
    },
    "Consuming Shadow": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Consuming_Shadow.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Coolheaded":{
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Coolheaded.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.CARDS_ADDED_TO_HAND: 1,
    },
    "Creative AI": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Creative_AI.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Darkness": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Darkness.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Dazed": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Dazed.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.STATUS,
        CardDataTypes.KEYWORDS: [CardKeywords.UNPLAYABLE, CardKeywords.ETHEREAL]
    },
    "Defend": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Defend.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Defragment": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Defragment.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Feral": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Feral.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.AVOID
    },
    "Fight Through": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Fight_Through.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.STATUS_TO_DISCARD,
        CardDataTypes.CREATED_STATUSES: ["Wound", "Wound"],
    },
    "Focused Strike": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Focused_Strike.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "FTL": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_FTL.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.DRAW_DIFF,
    },
    "Fuel": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Fuel.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.ENERGY_DIFF_AND_DRAW,
        CardDataTypes.TOTAL_ENERGY_COST: -1,
        CardDataTypes.CARDS_ADDED_TO_HAND: 1,
    },
    "Fusion": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Fusion.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Genetic Algorithm": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Genetic_Algorithm.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.KEYWORDS: [CardKeywords.EXHAUST],
    },
    "Glacier": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Glacier.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Glasswork": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Glasswork.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Go for the Eyes": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Go_for_the_Eyes.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "Gunk Up": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Gunk_Up.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.STATUS_TO_DISCARD,
        CardDataTypes.CREATED_STATUSES: ["Slimed"],
    },
    "Hailstorm": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Hailstorm.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Hologram": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Hologram.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.SEARCH_AND_ADD,
        CardDataTypes.CARDS_ADDED_TO_HAND: 1,
    },
    "Hotfix": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Hotfix.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.KEYWORDS: [CardKeywords.EXHAUST],
    },
    "Hyperbeam": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Hyperbeam.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Infection": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Infection.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.STATUS,
        CardDataTypes.KEYWORDS: [CardKeywords.UNPLAYABLE],
    },
    "Injury": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Injury.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.KEYWORDS: [CardKeywords.UNPLAYABLE],
    },
    "Iteration": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Iteration.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER
    },
    "Leap": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Leap.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Lightning Rod": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Lightning_Rod.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Loop": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Loop.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER
    },
    "Machine Learning": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Machine_Learning.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER
    },
    "Modded": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Modded.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.TRACK_TIMES_PLAYED,
    },
    "Momentum Strike": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Momentum_Strike.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.TRACK_TIMES_PLAYED,
    },
    "Neow's Fury": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Neows_Fury.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.CARDS_ADDED_TO_HAND: 2,
    },
    "Null": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Null.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY, 
    },
    "Overclock": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Overclock.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.CARDS_ADDED_TO_HAND: 2,
    },
    "Rainbow": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Rainbow.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.KEYWORDS: [CardKeywords.EXHAUST]
    },
    "Reboot": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Reboot.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE
    },
    "Rocket Punch": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Rocket_Punch.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.AVOID,
        CardDataTypes.CARDS_ADDED_TO_HAND: 1,
    },
    "Scavenge": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Scavenge.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.SELECT_AND_EXHAUST,
        CardDataTypes.CARDS_ADDED_TO_HAND: -1,
    },
    "Scrape": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Scrape.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.AVOID,
    },
    "Shadow Sheild": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Shadow_Sheild.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
    "Signal Boost": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Signal_Boost.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE,
        CardDataTypes.KEYWORDS: [CardKeywords.EXHAUST]
    },
    "Skim": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Skim.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.CARDS_ADDED_TO_HAND: 3,
    },
    "Slimed": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Slimed.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.STATUS,
        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.CARDS_ADDED_TO_HAND: 1,
    },
    "Smokestack": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Smokestack.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Soot": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Soot.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.STATUS,
        CardDataTypes.KEYWORDS: [CardKeywords.UNPLAYABLE]
    },
    "Storm": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Storm.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Strike": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Strike.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "Subroutine": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Subroutine.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER,
    },
    "Sunder": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Sunder.png"),
        CardDataTypes.ENERGY_COST: 3,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.AVOID,
    },
    "Sweeping Beam": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Sweeping_Beam.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.CARDS_ADDED_TO_HAND: 1,
    },
    "Synchronize": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Synchronize.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.KEYWORDS: [CardKeywords.EXHAUST]
    },
    "Synthesis": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Synthesis.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE
    },
    "Tempest": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Tempest.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER
    },
    "Tesla Coil": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Tesla_Coil.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,
    },
    "Thunder": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Thunder.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.TYPE: CardTypes.POWER
    },
    "TURBO": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_TURBO.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.TYPE: CardTypes.POWER
    },
    "Uproar": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Uproar.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.DRAW_DIFF,
    },
    "White Noise": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_White_Noise.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.CONSTANT_DRAW,
        CardDataTypes.CARDS_ADDED_TO_HAND: 1,
    },
}

ENEMY_HEALTH_COLORS: list[tuple] = [(255, 245, 225), (255, 246, 226)]