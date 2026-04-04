class Card():
    def __init__(self, name: str, energy_cost: int, hand_position: int=None, draw: int=None, enhancement: str=None):
        self.hand_position = hand_position
        self.energy_cost = energy_cost
        self.name = name
        self.enhancement = enhancement
        self.draw = draw

    def move_hand_pos(self, card) -> None:
        if card.hand_position > self.hand_position:
            self.hand_position -= 1

    def __repr__(self):
        return f"Card(name={self.name}, energy_cost={self.energy_cost}, hand_position={self.hand_position}, draw={self.draw}, enhancement={self.enhancement})"
    
class Attack(Card):
    def __init__(self, name:str, energy_cost: int, damage: int, hand_position: int=None, curr_times: int=1, draw: int=None, enhancement: str=None):
        super().__init__(name, energy_cost, hand_position)
        self.damage = damage
        self.curr_times = curr_times

    def get_total_damage(self):
        return self.damage * self.curr_times
    
    def __repr__(self) -> str:
        repr_str = super().__repr__()
        return repr_str + f"\nAttack(damage={self.damage}, curr_times={self.curr_times})"