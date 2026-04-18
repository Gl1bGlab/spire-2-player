import mouse
from time import sleep
from math import floor

from win32 import win32gui
from PIL import ImageGrab
from PIL.Image import Image

from game_stat_handler import GameStatHandler
from constants.project_constants import ENEMY_HEALTH_CAPTURE_AREA, CARD_CAPTURE_MOUSE_LOCATION, \
                                        MOUSE_MOVE_TIME, CARD_PORTRAIT_CAPTURE_AREA, MOUSE_PAUSE_TIME
from constants.game_constants import WINDOW_NAME, ENEMY_HEALTH_COLORS

class GameWindowHandler():
    def __init__(self):
        self.window: int|None = None
        self.absolute_dimensions: tuple[float, float, float, float]|None = None
        self.hand_dimensions: tuple[float, float, float, float]|None = None
        self.curr_image: Image|None = None

        self.set_window()
        self.check_and_grab_game_image()

    def set_window(self) -> int:
        win32gui.EnumWindows(self.find_StS2, None)
        if self.window == None:
            raise Exception(f"{WINDOW_NAME} window not found, please open the game\nIf the game is opened, make sure the name of the window is {WINDOW_NAME}")
    
    # thx to Pedro Lobito from https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    def find_StS2(self, hwnd:int, ctx):
        if win32gui.IsWindowVisible(hwnd):
            if win32gui.GetWindowText(hwnd) != WINDOW_NAME:
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

    
    def grab_and_cut_dimensions(self, 
                                factors: tuple[float, float, float, float]
                            )->tuple[float, float, float, float]:
        self.check_and_grab_game_image()
        l_factor, t_factor, r_factor, b_factor = factors
        abs_l, abs_t, abs_r, abs_b = self.absolute_dimensions

        w, h = self.curr_image.size
        rel_l, rel_t, rel_r, rel_b = w*l_factor, h*t_factor, -w*r_factor, -h*b_factor
        return (abs_l + rel_l, abs_t + rel_t, abs_r + rel_r, abs_b + rel_b)
    
    def find_xy_dimensions(self, 
                       xy_window_factor: tuple[float, float, float, float], 
                       xy: tuple[int, int],
                    )->tuple[float, float, float, float]:
        xy_window_dimensions = self.grab_and_cut_dimensions(xy_window_factor)
        abs_x, x, x, abs_y = xy_window_dimensions

        x, y = xy
        abs_x += x
        abs_y -= y
        return (abs_x, 0, 0, abs_y)


    def mouse_to_dimension_pos(self, 
                            factors: tuple[float, float, float, float], 
                            delay=MOUSE_MOVE_TIME
                        )->None:
        l, x, x, b = factors
        mouse.move(l, b, duration=delay)

    def scroll_hand(self, game_stat_handler: GameStatHandler)->list[Image]:
        hand_size = game_stat_handler.hand_size.value
        
        images = []
        for i in range(hand_size):
            factors = self.grab_and_cut_dimensions(game_stat_handler.get_hand_size_factor(i))

            self.move_card_to_capture_site(factors)
            images.append(self.grab_and_cut_window_image(CARD_PORTRAIT_CAPTURE_AREA))
            mouse.right_click()
            sleep(MOUSE_PAUSE_TIME)
        return images

    def move_card_to_capture_site(self, factors: tuple[float, float, float, float]):
        card_capture_factors = self.grab_and_cut_dimensions(CARD_CAPTURE_MOUSE_LOCATION)

        self.mouse_to_dimension_pos(factors)
        mouse.click()

        self.mouse_to_dimension_pos(card_capture_factors)
        sleep(MOUSE_PAUSE_TIME)

    def grab_and_cut_window_image(self, window_factors)->Image:
        card_dimensions = self.grab_and_cut_dimensions(window_factors)
        card_image = ImageGrab.grab().crop(card_dimensions)
        return card_image
    
    def play_card(self, hand_pos: int, game_stat_handler: GameStatHandler)->None:
        factors = self.grab_and_cut_dimensions(game_stat_handler.get_hand_size_factor(hand_pos))
        self.mouse_to_dimension_pos(factors, delay=0)
        sleep(MOUSE_PAUSE_TIME)
        mouse.press()
        self.mouse_to_enemy()
        mouse.release()


    def mouse_to_enemy(self):
        self.check_and_grab_game_image()
        image = self.grab_and_cut_window_image(ENEMY_HEALTH_CAPTURE_AREA)
        for color in ENEMY_HEALTH_COLORS:
            xy = find_color_rel_xy(image, color)
            if xy != None:
                break
        if xy == None:
            raise Exception("Enemy health bar not found")

        xy_factor = self.find_xy_dimensions(ENEMY_HEALTH_CAPTURE_AREA, xy)
        self.mouse_to_dimension_pos(xy_factor)

def find_color_rel_xy(img: Image, color: tuple[int, int, int])->tuple[int, int] | None:
    width, height = img.size

    for x in reversed(range(width)):
        for y in reversed(range(height)):
            if img.getpixel((x, y)) == color:
                return x, y
    return None