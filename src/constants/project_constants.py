from enum import Enum
from win32 import win32api

class GameState(Enum):
    UNOPENED = "unopened",
    INIT = "init",
    CHAR_SELECT = "char_select",
    
class HandSizeCategories(Enum):
    ZERO = "zero hand size: 0",
    LOW = "low hand sizes: 1, 2, 3, 4, 5",
    HIGH = "high hand sizes: 6, 7, 8, 9, 10"