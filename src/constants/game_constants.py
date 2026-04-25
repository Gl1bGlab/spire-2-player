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
    CONSTANT_DRAW = "constant draw"
    CREATE_CARD_HAND = "create card(s) in hand"
    CREATE_CARD_DISCARD = "create card(s) in discard"

    SEARCH_AND_ADD = "search and add"
    SELECT_AND_EXHAUST = "select and exhaust"

    ENERGY_GAIN = "energy to gain"
    ENERGY_GAIN_AND_DRAW = "constant draw + energy gain"
    ENERGY_GAIN_AND_STATUS = "energy gain + create status"

    UNIQUE = "unique/track"
    AVOID = "AVOID"

class CardDataTypes(Enum):
    PORTRAIT_PATH = "path"
    ENERGY_COST = "cost"
    PLAY_TYPE = "play type"

    ENERGY_GAIN = "energy diff"
    CARDS_ADDED_TO_HAND = "draw diff"

    CREATED_DISCARD_CARDS = "cards added to discard pile"

    TYPE = "type"
    KEYWORDS = "keywords"
    SPECIAL = "special"

class PlayTypes(Enum):
    TARGET_ENEMY = True
    NO_TARGET = False

class CardKeywords(Enum):
    ETHEREAL = "ethereal"
    EXHAUST = "exhaust"
    UNPLAYABLE = "unplayable"

class UniqueCardNames(Enum):
    CHARGE_BATTERY = "Charge Battery"
    COMPACT = "Compact"
    DOUBLE_ENERGY = "Double Energy"
    FTL = "FTL"
    NEOWS_FURY = "Neow's Fury"
    REBOOT = "Reboot"
    SIGNAL_BOOST = "Signal Boost"
    SYNTHESIS = "Synthesis"

FUEL_NAME = "Fuel"

CARDS: dict[dict[CardDataTypes]] = {
    "Adaptive Strike": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Adaptive_Strike.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.CREATE_CARD_DISCARD,
        CardDataTypes.CREATED_DISCARD_CARDS: ["Adaptive Strike"],
    },
    "All for One": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_All_for_One.png"),
        CardDataTypes.ENERGY_COST: 2,
        CardDataTypes.PLAY_TYPE: PlayTypes. TARGET_ENEMY,

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

        CardDataTypes.SPECIAL: SpecialTypes.CREATE_CARD_DISCARD,
        CardDataTypes.CREATED_DISCARD_CARDS: ["Dazed"],
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

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE,
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

        CardDataTypes.SPECIAL: SpecialTypes.AVOID,
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
    "Double Energy": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Double_Energy.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE,
    },
    "Dualcast": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Dualcast.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
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

        CardDataTypes.SPECIAL: SpecialTypes.CREATE_CARD_DISCARD,
        CardDataTypes.CREATED_DISCARD_CARDS: ["Wound", "Wound"],
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

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE,
    },
    FUEL_NAME: {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Fuel.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.ENERGY_GAIN_AND_DRAW,
        CardDataTypes.ENERGY_GAIN: 1,
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

        CardDataTypes.SPECIAL: SpecialTypes.CREATE_CARD_DISCARD,
        CardDataTypes.CREATED_DISCARD_CARDS: ["Slimed"],
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

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE,
    },
    "Momentum Strike": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Momentum_Strike.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE,
    },
    "Neow's Fury": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Neows_Fury.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.UNIQUE,
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
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.POWER
    },
    "TURBO": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_TURBO.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.ENERGY_GAIN_AND_STATUS,
        CardDataTypes.CREATED_DISCARD_CARDS: ["Void"],
        CardDataTypes.ENERGY_GAIN: 2,
    },
    "Uproar": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Uproar.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.TARGET_ENEMY,

        CardDataTypes.SPECIAL: SpecialTypes.AVOID,
    },
    "White Noise": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_White_Noise.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.SPECIAL: SpecialTypes.CREATE_CARD_HAND,
        CardDataTypes.CARDS_ADDED_TO_HAND: 1,
    },
    "Wound": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Wound.png"),
        CardDataTypes.ENERGY_COST: 0,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,

        CardDataTypes.TYPE: CardTypes.STATUS,
        CardDataTypes.KEYWORDS: [CardKeywords.UNPLAYABLE]
    },
    "Zap": {
        CardDataTypes.PORTRAIT_PATH: join(CARD_PORTRAIT_PATH, "_Zap.png"),
        CardDataTypes.ENERGY_COST: 1,
        CardDataTypes.PLAY_TYPE: PlayTypes.NO_TARGET,
    },
}

ENEMY_HEALTH_COLORS: list[tuple[int, int, int]] = [(255, 245, 225), (255, 246, 226)]
LOOT_RIBBON_COLOR: tuple[int, int, int] = (164, 142, 117)
LOOT_BUTTONS_COLOR: tuple[int, int, int] = (57, 125, 130)