from time import sleep

from PIL import ImageChops
from PIL.Image import Image
import mouse

from constants.project_constants import FightState, BOTTOM_FACTOR_CONST, \
ACCEPTABLE_IMAGE_DIFF, HAND_SIZE_PARAMETERS, HandSizeParameterTypes, HandSizes, \
CARD_PORTRAIT_CAPTURE_AREA, MOUSE_PAUSE_TIME
from constants.game_constants import DrawRelics, CARDS, CardDataTypes, PlayTypes, \
CardKeywords, SpecialTypes, CardTypes
from card_obj import Card
from card_helpers import card_portrait_to_card
from game_stat_handler import StatHandler
from game_window_handler import WindowHandler

class FightHandler():
    def __init__(self, stat_handler: StatHandler, window_handler: WindowHandler):
        self.stat_handler = stat_handler
        self.window_handler = window_handler
        self._draw_relics: list[DrawRelics]|None = stat_handler._draw_relics

        self._curr_deck_size: int = stat_handler._deck_size
        self._curr_discard_size: int = 0

        self._curr_turn: int = 0
        self._curr_state: FightState = FightState.PLAY_TURN

        self._curr_hand: list[Card]|None = None
        self._curr_hand_size: HandSizes = HandSizes.FIVE
        self._curr_energy: int = 3

        self._tracked_cards: dict = {}

    def hand_to_cards(self)->list[Card]:
        cards: list[Card] = []
        for i, portrait in enumerate(self.scroll_hand()):
            hand_position = i + 1
            cards.append(card_portrait_to_card(portrait, hand_position))
        self._curr_hand = cards
    
    def set_hand_size(self, size)->None:
        match (size):
            case 0:
                self._curr_hand_size = HandSizes.ZERO
                return
            case 1:
                self._curr_hand_size = HandSizes.ONE
                return
            case 2:
                self._curr_hand_size = HandSizes.TWO
                return
            case 3:
                self._curr_hand_size = HandSizes.THREE
                return
            case 4:
                self._curr_hand_size = HandSizes.FOUR
                return
            case 5:
                self._curr_hand_size = HandSizes.FIVE
                return
            case 6:
                self._curr_hand_size = HandSizes.SIX
                return
            case 7:
                self._curr_hand_size = HandSizes.SEVEN
                return
            case 8:
                self._curr_hand_size = HandSizes.EIGHT
                return
            case 9:
                self._curr_hand_size = HandSizes.NINE
                return
            case 10:
                self._curr_hand_size = HandSizes.TEN
                return

    def add_hand_size(self, amount: int)->None:
        self.set_hand_size(self._curr_hand_size.value + amount)

    def get_hand_size_factor(self, i)->tuple[int, int, int, int]:
        if self._curr_hand_size == HandSizes.ZERO:
            raise Exception("Tried to get empty hand")
        
        base = HAND_SIZE_PARAMETERS[self._curr_hand_size][HandSizeParameterTypes.BASE]
        first_card_factor = HAND_SIZE_PARAMETERS[self._curr_hand_size][HandSizeParameterTypes.FIRST_CARD_FACTOR]
        index_factor = HAND_SIZE_PARAMETERS[self._curr_hand_size][HandSizeParameterTypes.INDEX_FACTOR] * i

        return (base + first_card_factor + index_factor, 0, 0, BOTTOM_FACTOR_CONST)

    def scroll_hand(self)->list[Image]:
        hand_size = self._curr_hand_size.value
        
        images = []
        for i in range(hand_size):
            factors = self.window_handler.grab_and_cut_dimensions(self.get_hand_size_factor(i))

            self.window_handler.move_card_to_capture_site(factors)
            images.append(self.window_handler.grab_and_cut_window_image(CARD_PORTRAIT_CAPTURE_AREA))
            mouse.right_click()
            sleep(MOUSE_PAUSE_TIME)
        return images

    def mouse_to_play_position(self, card: Card):
        if card.play_type == PlayTypes.TARGET_ENEMY:
            self.window_handler.mouse_to_enemy()
        else:
            self.window_handler.mouse_to_generic_play_pos() 

    def play_card(self, card: Card)->None:
        factors = self.window_handler.grab_and_cut_dimensions(self.get_hand_size_factor(card.hand_position - 1))
        self.window_handler.mouse_to_dimension_pos(factors, delay=0)
        sleep(MOUSE_PAUSE_TIME)
        mouse.press()
        self.mouse_to_play_position(card)
        mouse.release()

    def start_turn(self):
        self._curr_turn += 1
        self._curr_hand = self.hand_to_cards()

    def can_be_played_check(self, card: Card)->bool:
        enough_energy = card.enough_energy_check(self._curr_energy)
        not_unplayable = not CardKeywords.UNPLAYABLE in card.keywords
        return not_unplayable and enough_energy
    
    """TODO!!!!"""
    def handle_special_card(self, card: Card):
        match card.special_type:
            case SpecialTypes.CONSTANT_DRAW:
                self.draw_cards(card.hand_diff)
                return
            case SpecialTypes.CREATE_CARD_DISCARD:
                self.add_cards_to_discard()
                return
            
            case SpecialTypes.SELECT_AND_EXHAUST:
                self.select_from_hand()
                return
            case SpecialTypes.SEARCH_AND_ADD:
                self.search_and_add()
                return
            
            case SpecialTypes.ENERGY_GAIN:
                self.gain_energy()
                return
            case SpecialTypes.ENERGY_GAIN_AND_DRAW:
                self.gain_energy()
                self.draw_cards()
                return
            case SpecialTypes.ENERGY_GAIN_AND_STATUS:
                self.gain_energy()
                self.add_cards_to_discard()
                return
            
            case SpecialTypes.TRACK_TIMES_PLAYED:
                self.track_card(card.name)
                return
            case SpecialTypes.UNIQUE:
                self.handle_unique_card(card)
                return
            case SpecialTypes.AVOID:
                raise NotImplementedError("card avoiding logic not made")

    def create_card(self):
        pass

    def select_from_hand(self):
        pass

    def search_and_add(self):
        pass

    def add_cards_to_discard(self, card_num: int):
        pass

    def draw_cards(self, card_num: int):
        pass

    def gain_energy(self, energy: int):
        pass

    def track_card(self, card_name: str):
        if card_name not in self._tracked_cards:
            self._tracked_cards[card_name] = 0
        self._tracked_cards[card_name] += 1

    def handle_unique_card(self, card: Card):
        pass

    def play_card_data(self, card: Card)->bool:
        if not self.can_be_played_check(card):
            return False

        self._curr_energy -= card.cost

        if card.special_type is not None:
            self.handle_special_card(card)

        if card.card_type == CardTypes.POWER:
            self.track_card(card.name)
            self.add_cards_to_discard(-1)


        self.play_card(card)
        self.add_hand_size(-1)
        self.add_cards_to_discard(1)

        self._curr_hand.remove(card)
        for i in range(self._curr_hand_size.value):
            self._curr_hand[i].move_hand_pos(card)

        return True


    def __repr__(self):
        return f"""FightHandler(
    draw_relics={self._draw_relics},
    curr_turn={self._curr_turn},
    curr_state={self._curr_state},
    curr_hand={self._curr_hand},
    curr_hand_size={self._curr_hand_size},
)"""