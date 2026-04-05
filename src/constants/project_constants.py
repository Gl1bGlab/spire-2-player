from enum import Enum
from win32 import win32api

WH_SCREEN_RATIO = .5625

class GameState(Enum):
    UNOPENED = "unopened",
    INIT = "init",
    CHAR_SELECT = "char_select",
    