from enum import Enum
from win32 import win32api

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