import mouse

from win32 import win32gui
from PIL import ImageGrab
from PIL.Image import Image

from card_obj import Card, Attack
from constants.game_constants import WINDOW_NAME

class GameWindowHandler():
    def __init__(self):
        self.window: int | None = None
        self.absolute_dimensions: tuple[int, int, int , int] | None = None
        self.hand_dimensions: tuple[int, int, int , int] | None = None
        self.curr_image: Image | None = None

        self.set_window()

    def set_window(self) -> int:
        win32gui.EnumWindows(self.find_StS2, None)
        if self.window == None:
            raise Exception(f"{WINDOW_NAME} window not found, please open the game\nIf the game is opened, make sure the name of the window is {WINDOW_NAME}")
    
    # thx to Pedro Lobito from https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    def find_StS2(self, hwnd:int, ctx):
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
        self.absolute_dimensions = win32gui.GetWindowRect(self.window)
        self.title_bar_offset()
        self.window_size_normalizer()
        self.curr_image = ImageGrab.grab().crop(self.absolute_dimensions)

    def title_bar_offset(self)->None:
        TITLE_BAR_SIZE = 22
        x1, t, x2, x3 = self.absolute_dimensions
        t += TITLE_BAR_SIZE
        self.absolute_dimensions = x1, t, x2, x3
    
    def window_size_normalizer(self)->None:
        # calculations to correctly crop the raw image of the screen
        # to get a clean (enough) image of the game window
        W_FACTOR = 16
        H_FACTOR = 9
        WH_SCREEN_RATIO = .5625
        l, t, r, b = self.absolute_dimensions
        w = r - l
        h = b - t
        ratio = h/w
        if ratio > WH_SCREEN_RATIO:
            cut_factor = (h-(w*H_FACTOR/W_FACTOR))/2
            b, t = b-cut_factor, t+cut_factor
        else:
            cut_factor = (w-(h*W_FACTOR/H_FACTOR))/2
            r, l = r-cut_factor, l+cut_factor
        self.absolute_dimensions = (l, t, r, b)

    def check_and_grab_game_image(self)->None:
        self.game_window_still_exists_check()
        self.game_window_foreground_check()
        self.game_screen_grab()

    def get_hand_image(self)->Image:
        # factors representing how much the screen should be cropped to get
        # a good image of the current hand
        LEFT_FACTOR = .05
        TOP_FACTOR = .8
        RIGHT_FACTOR = .95

        self.check_and_grab_game_image()
        w, h = self.curr_image.size
        l, t, r, b = w*LEFT_FACTOR, h*TOP_FACTOR, w*RIGHT_FACTOR, h

        self.hand_dimensions = (l, t, r, b)
        return self.curr_image.crop(self.hand_dimensions)

    def scroll_hand(self)->list[Image]:
        LEFT_FACTOR = .05
        l, t, r, b = self.absolute_dimensions
        w_tenth = (r - l) / 10
        mouse.move(l+(l*LEFT_FACTOR), b-(b*.05))
        #mouse.move(r, b-(b*.05), duration=10)
        for i in range(10):
            mouse.move(l+((i + 1)*w_tenth), b-(b*.05), duration=1)
            card_dimensions = mouse.get_position()
            ImageGrab.grab().crop()