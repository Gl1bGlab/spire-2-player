from __future__ import annotations

from constants.game_constants import SpecialTypes, PlayTypes, CardKeywords, CardTypes

class Card():
    def __init__(self, 
            hand_position: int, 
            name: str, 
            cost: int,
            play_type: PlayTypes,

            hand_diff: int|None,
            energy_gain: int|None,

            card_type: CardTypes|None,
            special_type: SpecialTypes|None,
            keywords: list[CardKeywords]|list,
            discard_cards_to_create: list[Card]|list,
        ):
        self.name = name
        self.hand_position = hand_position
        self.cost = cost
        self.play_type = play_type

        self.hand_diff = hand_diff
        self.energy_gain = energy_gain

        self.card_type = card_type
        self.special_type = special_type
        self.keywords = keywords
        self.discard_cards_to_create = discard_cards_to_create

    def get_discard_num(self)->int:
        return len(self.discard_cards_to_create)

    def enough_energy_check(self, curr_energy)->bool:
        return self.cost <= curr_energy

    def move_hand_pos(self, card: Card):
        if card.hand_position < self.hand_position:
            self.hand_position -= 1

    def __repr__(self):
        repr_str = "Card("
        for key, value in self.__dict__.items():
            if value is not None:
                repr_str += f"\n    {key}={value}"
        return repr_str + "\n)"
    
