from PIL import ImageChops
from PIL.Image import Image, open

from constants.project_constants import CARD_PORTRAIT_PATH, ACCEPTABLE_IMAGE_DIFF
from constants.game_constants import CARDS, CardDataTypes
from card_obj import Card

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
    energy_gain = card_data[CardDataTypes.ENERGY_GAIN] if CardDataTypes.ENERGY_GAIN in card_data else None

    created_discard_cards = card_data[CardDataTypes.CREATED_DISCARD_CARDS] if CardDataTypes.CREATED_DISCARD_CARDS in card_data else []
    keywords = card_data[CardDataTypes.KEYWORDS] if CardDataTypes.KEYWORDS in card_data else []

    card_type = card_data[CardDataTypes.TYPE] if CardDataTypes.TYPE in card_data else None
    special_type = card_data[CardDataTypes.SPECIAL] if CardDataTypes.SPECIAL in card_data else None

    return Card(
        hand_position, 
        card_name, 
        energy_cost, 
        play_type, 
        hand_diff, 
        energy_gain, 
        card_type, 
        special_type, 
        keywords, 
        created_discard_cards,
    )



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