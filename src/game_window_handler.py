from win32 import win32gui
from PIL import ImageGrab
from PIL.Image import Image

from constants.game_constants import WINDOW_NAME

class GameWindowHandler():
    def __init__(self):
        self.window: int | None = None
        self.dimentions: tuple[int, int, int , int] | None = None
        self.curr_image: Image | None = None

        self.set_window()

    def set_window(self) -> int:
        win32gui.EnumWindows(self.find_StS2, None)
        if self.window == None:
            raise Exception("Slay the Spire 2 window not found, please open the game\nIf the game is opened, make sure the name of the window is Slay the Spire 2")
    
    # thx to Pedro Lobito from https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    def find_StS2(self, hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            if win32gui.GetWindowText(hwnd) != "Slay the Spire 2":
                return
            self.window = hwnd
            print(f"Slay the Spire 2 window found at {hex(hwnd)}")

    def game_window_still_exists_check(self)->None:
        if not win32gui.IsWindow(self.window) or win32gui.GetWindowText(self.window) != WINDOW_NAME:
            self.set_window()
            
    def game_window_foreground_check(self, game_window)->None:
        msg_printed = False
        while win32gui.GetForegroundWindow() != game_window:
            if not msg_printed:
                print("Waiting for Slay the Spire 2 to be the foreground window")
                msg_printed = True
            pass

    def game_screen_grab(self, game_window)->None:
        window_dimentions = win32gui.GetWindowRect(game_window)
        window_dimentions = self.window_size_normalizer(window_dimentions)
        game_screen = ImageGrab.grab().crop(window_dimentions)
        return game_screen
    
    def window_size_normalizer(self, window_dimentions: tuple[int, int, int, int])->None:
        W_FACTOR = 16
        H_FACTOR = 9
        WH_SCREEN_RATIO = .5625
        l, t, r, b = window_dimentions
        w = r - l
        h = b - t
        ratio = h/w
        if ratio > WH_SCREEN_RATIO:
            cut_factor = (h-(w*H_FACTOR/W_FACTOR))/2
            b, t = b-cut_factor, t+cut_factor
        else:
            cut_factor = (w-(h*W_FACTOR/H_FACTOR))/2
            r, l = r-cut_factor, l+cut_factor
        self.dimentions = (l, t, r, b)

    def check_and_grab_game_image(self, game_window)->None:
        game_window = self.game_window_still_exists_check(game_window)
        self.game_window_foreground_check(game_window)
        return self.game_screen_grab(game_window)

