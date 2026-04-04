from enum import Enum
from win32 import win32api

SCREEN_WIDTH = win32api.GetSystemMetrics(0)
SCREEN_HEIGHT = win32api.GetSystemMetrics(1)

class GameState(Enum):
    UNOPENED = "unopened",
    INIT = "init",
    CHAR_SELECT = "CharSelect",
    