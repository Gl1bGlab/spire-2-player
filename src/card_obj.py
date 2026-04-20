from os import listdir
from os.path import join

from PIL.Image import Image, open
from PIL import ImageChops

from constants.game_constants import CARDS, CardDataTypes, SpecialTypes, PlayTypes
from constants.project_constants import CARD_PORTRAIT_PATH, ACCEPTABLE_IMAGE_DIFF
# from game_window_handler import GameWindowHandler
# from game_stat_handler import GameStatHandler

class Card():
    def __init__(self, hand_position: int,):
        self.hand_position = hand_position

    def move_hand_pos(self, card)->None:
        if card.hand_position > self.hand_position:
            self.hand_position -= 1

    def __repr__(self):
        return f"""Card(
    hand_position={self.hand_position},
)"""
    
class SpecialCard(Card):
    def __init__(self, hand_position: int, name: str, cost: int,
                 draw: int|None, special_type: SpecialTypes|None,):
        super().__init__(hand_position)
        self.name = name
        self.cost = cost
        self.draw = draw
        self.special_type = special_type

    def move_hand_pos(self, card):
        return super().move_hand_pos(card)

    def __repr__(self):
        return f"""SpecialCard(
    hand_position={self.hand_position},
    name={self.name},
    draw={self.draw},
    cost={self.cost},
    special_type={self.special_type},
)"""
    
def card_portrait_to_card(new_card_portrait: Image, card_position: int)->Card|SpecialCard:
    for card_name, card_data in CARDS.items():
        curr_portrait = open(card_data[CardDataTypes.PORTRAIT_PATH])
        image_diff = count_color(ImageChops.difference(new_card_portrait, curr_portrait))

        if image_diff <= ACCEPTABLE_IMAGE_DIFF:
            energy_cost = card_data[CardDataTypes.ENERGY_COST]
            special_type = card_data[CardDataTypes.SPECIAL] if CardDataTypes.SPECIAL in card_data else None
            draw_diff = card_data[CardDataTypes.DRAW_DIFF] if CardDataTypes.DRAW_DIFF in card_data else None
            return SpecialCard(card_position, card_name, energy_cost, draw_diff, special_type)
    return Card(card_position)

def hand_to_cards(window_handler, stat_handler)->list[Card|SpecialCard]:
    from game_stat_handler import GameStatHandler
    from game_window_handler import GameWindowHandler
    cards: list[Card|None] = []
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