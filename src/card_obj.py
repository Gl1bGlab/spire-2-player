from os import listdir
from os.path import join

from PIL.Image import Image, open
from PIL import ImageChops

from constants.project_constants import CARD_PORTRAIT_PATH, ACCEPTABLE_IMAGE_DIFF

class Card():
    def __init__(self, portrait: Image, hand_position: int=None, draw: int=None):
        self.portrait = portrait
        self.hand_position = hand_position
        self.name = NotImplemented
        self.draw = draw

    def move_hand_pos(self, card)->None:
        if card.hand_position > self.hand_position:
            self.hand_position -= 1

    def __repr__(self):
        return f"Card(name={self.name}, hand_position={self.hand_position}, draw={self.draw})"
    
class Attack(Card):
    def __init__(self, name:str, damage: int, hand_position: int=None, curr_times: int=1, draw: int=None):
        super().__init__(name, hand_position)
        self.damage = damage
        self.curr_times = curr_times

    def get_total_damage(self):
        return self.damage * self.curr_times
    
    def __repr__(self) -> str:
        repr_str = super().__repr__()
        return repr_str + f"\nAttack(damage={self.damage}, curr_times={self.curr_times})"

def card_creator(new_card_portrait: Image)->Card:
    for portrait_file in listdir(CARD_PORTRAIT_PATH):
        portrait_file = join(CARD_PORTRAIT_PATH, portrait_file)

        curr_portrait = open(portrait_file)
        count_color(ImageChops.difference(new_card_portrait, curr_portrait))


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