from __future__ import annotations

from constants.game_constants import SpecialTypes, PlayTypes, CardKeywords, CardTypes

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
        self.total_cost = total_cost

        self.card_type = card_type
        self.special_type = special_type
        self.keywords = keywords
        self.created_cards = cards_to_create

    def energy_calculation_pre_play(self, curr_energy)->int:
        if self.cost <= curr_energy:
            return curr_energy - self.cost
        return None

    def move_hand_pos(self, card: Card):
        if card.hand_position > self.hand_position:
            self.hand_position -= 1

    def __repr__(self):
        repr_str = "Card("
        for key, value in self.__dict__.items():
            if value is not None:
                repr_str += f"\n    {key}={value}"
        return repr_str + "\n)"
    
