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
        self.check_and_grab_game_image()

    def set_window(self) -> int:
        win32gui.EnumWindows(self.find_StS2, None)
        if self.window == None:
            raise Exception(f"{WINDOW_NAME} window not found, please open the game\nIf the game is opened, make sure the name of the window is {WINDOW_NAME}")
    
    # thx to Pedro Lobito from https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    def find_StS2(self, hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            if win32gui.GetWindowText(hwnd) != f"{WINDOW_NAME}" or self.window != None:
                return
            self.window = hwnd
            print(f"{WINDOW_NAME} window found at {hex(hwnd)}")

    def game_window_still_exists_check(self)->None:
        if not win32gui.IsWindow(self.window) or win32gui.GetWindowText(self.window) != WINDOW_NAME:
            self.set_window()
            
    def game_window_foreground_check(self)->None:
        msg_printed = False
        while win32gui.GetForegroundWindow() != self.window:
            if not msg_printed:
                print(f"Waiting for {WINDOW_NAME} to be the foreground window")
                msg_printed = True
            pass

    def game_screen_grab(self)->None:
        self.dimentions = win32gui.GetWindowRect(self.window)
        self.window_size_normalizer()
        self.curr_image = ImageGrab.grab().crop(self.dimentions)
    
    def window_size_normalizer(self)->None:
        W_FACTOR = 16
        H_FACTOR = 9
        WH_SCREEN_RATIO = .5625
        TITLE_BAR_SIZE = 22
        l, t, r, b = self.dimentions
        t += TITLE_BAR_SIZE
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

    def check_and_grab_game_image(self)->None:
        self.game_window_still_exists_check()
        self.game_window_foreground_check()
        self.game_screen_grab()

