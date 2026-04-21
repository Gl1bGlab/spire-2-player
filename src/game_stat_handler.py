from PIL import ImageChops
from PIL.Image import Image

from constants.project_constants import (GameState, BOTTOM_FACTOR_CONST,
ACCEPTABLE_IMAGE_DIFF, HAND_SIZE_PARAMETERS, HandSizeParameterTypes, HandSizes)
from constants.game_constants import DrawRelics, CARDS, CardDataTypes
from card_obj import Card, Card

class GameStatHandler():
    def __init__(self):
        self.game_state: GameState = GameState.INIT
        self.draw_relics: list[DrawRelics] = []

        self.hand_size: HandSizes = HandSizes.FIVE
        self.hand: list[Card|Card]|None = None
        self.curr_turn: int = 0

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

    def card_portrait_to_card(self, new_card_portrait: Image, card_position: int)->Card|Card:
        for card_name, card_data in CARDS.items():
            curr_portrait = open(card_data[CardDataTypes.PORTRAIT_PATH])
            image_diff = self.count_color(ImageChops.difference(new_card_portrait, curr_portrait))

            if image_diff <= ACCEPTABLE_IMAGE_DIFF:
                energy_cost = card_data[CardDataTypes.ENERGY_COST]
                special_type = card_data[CardDataTypes.SPECIAL] if CardDataTypes.SPECIAL in card_data else None
                draw_diff = card_data[CardDataTypes.CARDS_ADDED_TO_HAND] if CardDataTypes.CARDS_ADDED_TO_HAND in card_data else None
                return Card(card_position, card_name, energy_cost, draw_diff, special_type)
        return Card(card_position)

    def hand_to_cards(self, window_handler)->list[Card|Card]:
        from game_window_handler import GameWindowHandler
        cards: list[Card|None] = []
        for i, portrait in enumerate(window_handler.scroll_hand(self)):
            hand_position = i + 1
            cards.append(self.card_portrait_to_card(portrait, hand_position))
        return cards

    # thx to https://www.geeksforgeeks.org/python/find-most-used-colors-in-image-using-python/
    def count_color(img: Image)->float:
        width, height = img.size
        total = 0
        count = 0

        for x in range(0, width):
            for y in range(0, height):
                for color in img.getpixel((x, y)):
                    total += color
                count += 1
        return total/count

    def __repr__(self):
        return f"""GameStatHandler(
    game_state={self.game_state},
    hand_size={self.hand_size},
    draw_relics={self.draw_relics},
    curr_turn={self.curr_turn},
)"""
