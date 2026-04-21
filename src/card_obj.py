from __future__ import annotations
from os import listdir
from os.path import join

from PIL.Image import Image, open
from PIL import ImageChops

from constants.game_constants import CARDS, CardDataTypes, SpecialTypes, PlayTypes, CardKeywords, CardTypes
from constants.project_constants import CARD_PORTRAIT_PATH, ACCEPTABLE_IMAGE_DIFF
# from game_window_handler import GameWindowHandler
# from game_stat_handler import GameStatHandler


class Card():
    def __init__(self, 
            hand_position: int, 
            name: str, 
            cost: int,
            play_type: PlayTypes,

            hand_diff: int|None,
            deck_diff: int|None,
            discard_diff: int|None,
            total_cost: int|None,

            card_type: CardTypes|None,
            special_type: SpecialTypes|None,
            keywords: list[CardKeywords]|None,
            cards_to_create: list[Card]|None,
        ):
        self.name = name
        self.hand_position = hand_position
        self.cost = cost
        self.play_type = play_type

        self.hand_diff = hand_diff
        self.deck_diff = deck_diff
        self.discard_diff = discard_diff
        self.card_type = card_type
        self.special_type = special_type
        self.keywords = keywords
        self.created_cards = cards_to_create

    def move_hand_pos(self, card: Card):
        if card.hand_position > self.hand_position:
            self.hand_position -= 1

    def __repr__(self):
        repr_str = "Card("
        for key, value in self.__dict__.items():
            if value is not None:
                repr_str += f"\n    {key}={value}"
        return repr_str + "\n)"
    
def card_portrait_to_card(new_card_portrait: Image, card_position: int)->Card:
    for card_name, card_data in CARDS.items():
        curr_portrait = open(card_data[CardDataTypes.PORTRAIT_PATH])
        image_diff = count_color(ImageChops.difference(new_card_portrait, curr_portrait))

        if image_diff <= ACCEPTABLE_IMAGE_DIFF:
            return build_card(card_position, card_name, card_data)
        
    new_card_portrait.show()
    raise Exception("Card portrait not found")

def build_card(hand_position: int, card_name: str, card_data: dict[CardDataTypes])->Card:
    energy_cost = card_data[CardDataTypes.ENERGY_COST]
    play_type = card_data[CardDataTypes.PLAY_TYPE]

    hand_diff = card_data[CardDataTypes.CARDS_ADDED_TO_HAND] if CardDataTypes.CARDS_ADDED_TO_HAND in card_data else None
    deck_diff = card_data[CardDataTypes.DECK_DIFF] if CardDataTypes.DECK_DIFF in card_data else None
    discard_diff = card_data[CardDataTypes.DISCARD_DIFF] if CardDataTypes.DISCARD_DIFF in card_data else None
    total_energy_cost = card_data[CardDataTypes.TOTAL_ENERGY_COST] if CardDataTypes.TOTAL_ENERGY_COST in card_data else None

    created_statuses = card_data[CardDataTypes.CREATED_STATUSES] if CardDataTypes.CREATED_STATUSES in card_data else None

    card_type = card_data[CardDataTypes.TYPE] if CardDataTypes.TYPE in card_data else None
    keywords = card_data[CardDataTypes.KEYWORDS] if CardDataTypes.KEYWORDS in card_data else None
    special_type = card_data[CardDataTypes.SPECIAL] if CardDataTypes.SPECIAL in card_data else None

    return Card(
        hand_position, 
        card_name, 
        energy_cost, 
        play_type, 
        hand_diff, 
        deck_diff, 
        discard_diff, 
        total_energy_cost, 
        card_type, 
        special_type, 
        keywords, 
        created_statuses,
    )

def hand_to_cards(window_handler, stat_handler)->list[Card]:
    from game_stat_handler import GameStatHandler
    from game_window_handler import GameWindowHandler
    cards: list[Card] = []
    for i, portrait in enumerate(window_handler.scroll_hand(stat_handler)):
        hand_position = i + 1
        cards.append(card_portrait_to_card(portrait, hand_position))
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


"""
TODO: do something with these at some point????
"""

# class Attack(Card):
#     def __init__(self, hand_position: int, name: str, cost: int,
#                  draw: int|None, special_type: SpecialTypes|None,
#                  damage: int, times: int):
#         super().__init__(hand_position, name, cost, draw, special_type)
#         self.damage = damage
#         self.times = times

#     def get_total_damage(self):
#         return self.damage * self.times
    
#     def move_hand_pos(self, card):
#         return super().move_hand_pos(card)
    
#     def __repr__(self) -> str:
#         repr_str = super().__repr__()
#         return repr_str.replace("Card", "Attack").replace(")", f"\n\tdamage={self.damage},\n\ttimes={self.times},\n)")

# class Skill(Card):
#     def __init__(self, hand_position: int, name: str, cost: int,
#                  draw: int|None, special_type: SpecialTypes|None,
#                  block: int|None):
#         super().__init__(hand_position, name, cost, draw, special_type)
#         self.block = block
    
#     def move_hand_pos(self, card):
#         return super().move_hand_pos(card)

#     def __repr__(self) -> str:
#         repr_str = super().__repr__()
#         return repr_str.replace("Card", "Skill").replace(")", f"\n\tblock={self.block},\n)")

# class Power(Card):
#     def __init__(self, hand_position: int, name: str, cost: int,
#                  draw: int|None, special_type: SpecialTypes|None,):
#         super().__init__(hand_position, name, cost, draw, special_type)
    
#     def move_hand_pos(self, card):
#         return super().move_hand_pos(card)

#     def __repr__(self) -> str:
#         repr_str = super().__repr__()
#         return repr_str.replace("Card", "Power")

# class Status(Card):
#     def __init__(self, hand_position: int, name: str, cost: int,
#                  draw: int|None, special_type: SpecialTypes|None,):
#         super().__init__(hand_position, name, cost, draw, special_type)
    
#     def move_hand_pos(self, card):
#         return super().move_hand_pos(card)

#     def __repr__(self) -> str:
#         repr_str = super().__repr__()
#         return repr_str.replace("Card", "Status")

# class Curse(Card):
    # def __init__(self, hand_position: int, name: str, cost: int,
    #              draw: int|None, special_type: SpecialTypes|None,):
    #     super().__init__(hand_position, name, cost, draw, special_type)
    
    # def move_hand_pos(self, card):
    #     return super().move_hand_pos(card)

    # def __repr__(self) -> str:
    #     repr_str = super().__repr__()
    #     return repr_str.replace("Card", "Curse")