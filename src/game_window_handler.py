import mouse
from time import sleep

from win32 import win32gui
from PIL import ImageGrab
from PIL.Image import Image

from card_obj import Card, Attack
from game_stat_handler import GameStatHandler
from constants.game_constants import WINDOW_NAME

class GameWindowHandler():
    def __init__(self):
        self.window: int | None = None
        self.absolute_dimensions: tuple[int, int, int , int] | None = None
        self.hand_dimensions: tuple[int, int, int , int] | None = None
        self.curr_image: Image | None = None

        self.set_window()
        self.check_and_grab_game_image()

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
        l, t, r, b = self.absolute_dimensions
        t += TITLE_BAR_SIZE
        l -= TITLE_BAR_SIZE
        self.absolute_dimensions = l, t, r, b
    
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

    
    def grab_and_cut_dimensions(self, factors: tuple[int, int, int, int]):
        self.check_and_grab_game_image()
        l_factor, t_factor, r_factor, b_factor = factors
        abs_l, abs_t, abs_r, abs_b = self.absolute_dimensions

        w, h = self.curr_image.size
        rel_l, rel_t, rel_r, rel_b = w*l_factor, h*t_factor, -w*r_factor, -h*b_factor
        return (abs_l + rel_l, abs_t + rel_t, abs_r + rel_r, abs_b + rel_b)

    def scroll_hand(self, game_stat_handler: GameStatHandler)->list[Image]:
        hand_size = game_stat_handler.hand_size

        images = []
        for i in range(hand_size):
            factors = game_stat_handler.get_hand_size_factor(i)
            l, x, x, b = self.grab_and_cut_dimensions(factors)

            self.move_card_to_capture_site(l, b)
            images.append(self.get_card_portrait_image())
            mouse.right_click()
        return images

    def move_card_to_capture_site(self, l, b):
        factors = (.1, 0, 0, .03)
        x_l, x, x, x_b = self.grab_and_cut_dimensions(factors)

        mouse.move(l, b)
        mouse.click()

        mouse.move(x_l, x_b)
        sleep(.37)

    def get_card_portrait_image(self)->Image:
        factors = (.04, .83, .84, .03)
        card_dimensions = self.grab_and_cut_dimensions(factors)
        card_image = ImageGrab.grab().crop(card_dimensions)
        return card_image