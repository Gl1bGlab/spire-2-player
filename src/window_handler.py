from time import sleep

import mouse
from win32 import win32gui
from PIL import ImageGrab
from PIL.Image import Image

from constants.project_constants import WH_SCREEN_RATIO, \
W_FACTOR, H_FACTOR, \
ENEMY_HEALTH_CAPTURE_AREA, \
MOUSE_MOVE_TIME, MOUSE_PAUSE_TIME, \
GENERIC_CARD_PLAY_LOCATION, CARD_CAPTURE_MOUSE_LOCATION, END_TURN_BUTTON_LOCATION, \
MOUSE_LOOT_LOCATION

from constants.game_constants import WINDOW_NAME, ENEMY_HEALTH_COLORS, \
LOOT_BUTTONS_COLOR

class WindowHandler():
    def __init__(self):
        self.window: int|None = None
        self.absolute_dimensions: tuple[float, float, float, float]|None = None
        self.hand_dimensions: tuple[float, float, float, float]|None = None
        self.curr_image: Image|None = None

        self.set_window()
        self.check_and_grab_game_image()

    def set_window(self):
        win32gui.EnumWindows(self.find_StS2, None)
        if self.window == None:
            raise Exception(
f"""game window not found, please open the game
If the game is opened, make sure the name of the window is 'Slay the Spire 2'"""
)
    
    # thx to Pedro Lobito from https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    def find_StS2(self, hwnd:int, ctx):
        if not win32gui.IsWindowVisible(hwnd):
            pass
        if win32gui.GetWindowText(hwnd) != WINDOW_NAME:
            return
        self.window = hwnd
        print(f"{WINDOW_NAME} window found at ID {hex(hwnd)}")

    def game_window_still_exists_check(self)->None:
        if not win32gui.IsWindow(self.window) or win32gui.GetWindowText(self.window) != WINDOW_NAME:
            self.set_window()
            
    def game_window_foreground_check(self)->None:
        msg_printed = False
        while win32gui.GetForegroundWindow() != self.window:
            if not msg_printed:
                print(f"Waiting for {hex(self.window)} to be the foreground window")
                msg_printed = True
            if not win32gui.IsWindow(self.window) or (win32gui.GetWindowText(self.window) != WINDOW_NAME):
                self.window = None
                self.game_window_still_exists_check()


    def game_screen_grab(self)->None:
        self.absolute_dimensions = win32gui.GetWindowRect(self.window)
        # self.title_bar_offset()
        self.window_size_normalizer()
        self.curr_image = ImageGrab.grab().crop(self.absolute_dimensions)
    
    def window_size_normalizer(self)->None:
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


    def factors_to_dimensions(self, 
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
        xy_window_dimensions = self.factors_to_dimensions(xy_window_factor)
        abs_x, x, x, abs_y = xy_window_dimensions

        x, y = xy
        abs_x += x
        abs_y -= y
        return (abs_x, 0, 0, abs_y)


    def mouse_to_dimension_pos(self, 
            dimensions: tuple[float, float, float, float], 
            delay=MOUSE_MOVE_TIME,
        ):
        l, x, x, b = dimensions
        mouse.move(l, b, duration=delay)

    def mouse_to_factor_pos(self,
            factors: tuple[float, float, float, float],
            delay=MOUSE_MOVE_TIME,
        ):
        dimensions = self.factors_to_dimensions(factors)
        self.mouse_to_dimension_pos(dimensions)

    def move_card_to_capture_site(self, factors: tuple[float, float, float, float]):
        self.mouse_to_dimension_pos(factors)
        mouse.click()

        self.mouse_to_factor_pos(CARD_CAPTURE_MOUSE_LOCATION)
        sleep(MOUSE_PAUSE_TIME)

    def grab_and_cut_window_image(self, window_factors)->Image:
        card_dimensions = self.factors_to_dimensions(window_factors)
        card_image = ImageGrab.grab().crop(card_dimensions)
        return card_image


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

    def mouse_to_generic_play_pos(self):
        self.mouse_to_factor_pos(GENERIC_CARD_PLAY_LOCATION)

    def mouse_to_end_turn(self):
        self.mouse_to_factor_pos(END_TURN_BUTTON_LOCATION)
        
    def mouse_to_play_position(self, is_targeting_enemy):
        if is_targeting_enemy: self.mouse_to_enemy()
        else: self.mouse_to_generic_play_pos()

    def mouse_to_loot(self):
        self.mouse_to_factor_pos(MOUSE_LOOT_LOCATION)


    def is_loot_on_screen(self)->bool:
        self.check_and_grab_game_image()
        image = self.grab_and_cut_window_image(MOUSE_LOOT_LOCATION)
        xy = find_color_rel_xy(image, LOOT_BUTTONS_COLOR)
        return xy is not None
    
    def _show_cut_image(self, factors):
        self.grab_and_cut_window_image(factors).show()

    def __repr__(self)->str:
        return f"""WindowHandler(
    window={hex(self.window)},
    absolute_dimesnions={self.absolute_dimensions},
    hand_dimensions={self.hand_dimensions},
    curr_image={self.curr_image},
)"""

def find_color_rel_xy(img: Image, color: tuple[int, int, int])->tuple[int, int] | None:
    width, height = img.size

    for x in reversed(range(width)):
        for y in reversed(range(height)):
            if img.getpixel((x, y)) == color:
                return x, y
    return None

"method graveyard"
# def title_bar_offset(self)->None:
#     l, t, r, b = self.absolute_dimensions
#     t += TITLE_BAR_SIZE
#     l -= TITLE_BAR_SIZE
#     self.absolute_dimensions = l, t, r, b