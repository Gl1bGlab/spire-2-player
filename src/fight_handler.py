from time import sleep

from PIL import ImageChops
from PIL.Image import Image
import mouse

from constants.project_constants import FightState, BOTTOM_FACTOR_CONST, \
ACCEPTABLE_IMAGE_DIFF, HAND_SIZE_PARAMETERS, HandSizeParameterTypes, HandSizes, \
CARD_PORTRAIT_CAPTURE_AREA, MOUSE_PAUSE_TIME
from constants.game_constants import DrawRelics, CARDS, CardDataTypes
from card_obj import Card
from card_helpers import card_portrait_to_card
from game_stat_handler import StatHandler
from game_window_handler import WindowHandler

class FightHandler():
    def __init__(self, stat_handler: StatHandler, window_handler: WindowHandler):
        self.stat_handler = stat_handler
        self.window_handler = window_handler

        self._draw_relics: list[DrawRelics]|None = stat_handler.draw_relics
        self._curr_turn: int = 0
        self._curr_state: FightState = FightState.PLAY_TURN
        self._curr_hand: list[Card]|None = None
        self._curr_hand_size: HandSizes = HandSizes.FIVE

    def hand_to_cards(self)->list[Card]:
        cards: list[Card] = []
        for i, portrait in enumerate(self.scroll_hand()):
            hand_position = i + 1
            cards.append(card_portrait_to_card(portrait, hand_position))
        self._curr_hand = cards
    
    def set_hand_size(self, size)->None:
        match (size):
            case 0:
                self.hand_size = HandSizes.ZERO
                return
            case 1:
                self.hand_size = HandSizes.ONE
                return
            case 2:
                self.hand_size = HandSizes.TWO
                return
            case 3:
                self.hand_size = HandSizes.THREE
                return
            case 4:
                self.hand_size = HandSizes.FOUR
                return
            case 5:
                self.hand_size = HandSizes.FIVE
                return
            case 6:
                self.hand_size = HandSizes.SIX
                return
            case 7:
                self.hand_size = HandSizes.SEVEN
                return
            case 8:
                self.hand_size = HandSizes.EIGHT
                return
            case 9:
                self.hand_size = HandSizes.NINE
                return
            case 10:
                self.hand_size = HandSizes.TEN
                return

    def add_hand_size(self, amount: int)->None:
        self.set_hand_size(self.hand_size.value + amount)

    def get_hand_size_factor(self, i)->tuple[int, int, int, int]:
        if self.hand_size == HandSizes.ZERO:
            raise Exception("Tried to get empty hand")
        
        base = HAND_SIZE_PARAMETERS[self.hand_size][HandSizeParameterTypes.BASE]
        first_card_factor = HAND_SIZE_PARAMETERS[self.hand_size][HandSizeParameterTypes.FIRST_CARD_FACTOR]
        index_factor = HAND_SIZE_PARAMETERS[self.hand_size][HandSizeParameterTypes.INDEX_FACTOR] * i

        return (base + first_card_factor + index_factor, 0, 0, BOTTOM_FACTOR_CONST)

    def scroll_hand(self)->list[Image]:
        hand_size = self.hand_size.value
        
        images = []
        for i in range(hand_size):
            factors = self.window_handler.grab_and_cut_dimensions(self.get_hand_size_factor(i))

            self.window_handler.move_card_to_capture_site(factors)
            images.append(self.window_handler.grab_and_cut_window_image(CARD_PORTRAIT_CAPTURE_AREA))
            mouse.right_click()
            sleep(MOUSE_PAUSE_TIME)
        return images

    def play_card(self, hand_pos: int)->None:
        factors = self.window_handler.grab_and_cut_dimensions(self.get_hand_size_factor(hand_pos))
        self.window_handler.mouse_to_dimension_pos(factors, delay=0)
        sleep(MOUSE_PAUSE_TIME)
        mouse.press()
        self.window_handler.mouse_to_enemy()
        mouse.release()

    def start_turn(self):
        self._curr_turn += 1
        self._curr_hand = self.hand_to_cards()

    def __repr__(self):
        return f"""FightHandler(
    curr_turn={self._curr_turn},
    curr_state={self._curr_state},
    curr_hand={self._curr_hand},
)"""