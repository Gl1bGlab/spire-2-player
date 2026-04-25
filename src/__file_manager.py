import os
from os.path import join, normpath, abspath
import shutil

from uuid import uuid4
from PIL.Image import Image

from constants.project_constants import CARD_PORTRAIT_PATH
from fight_handler import FightHandler

def scroll_and_gen(fight_handler: FightHandler):
    portraits = fight_handler.scroll_hand()
    for portrait in portraits:
        gen_image_file(portrait)

def gen_factor_image(
        fight_handler: FightHandler, 
        factors: tuple[float, float, float, float],
    ):
    gen_image_file(fight_handler.window_handler.window_factors_to_image(factors))


def gen_image_file(img: Image)->str:
    rand_path = normpath(join(CARD_PORTRAIT_PATH, f"..\\temp\\_{str(uuid4())[:8]}.png"))
    file = open(rand_path, "w")
    img.save(rand_path)
    return rand_path

def clear_temp()->None:
    temp_path = normpath(join(CARD_PORTRAIT_PATH, "..\\temp"))

    for file in os.listdir(temp_path):
        src = join(temp_path, file)
        dst = normpath(join(temp_path, "..\\card_portraits", file))

        open(dst, "w")
        shutil.move(abspath(src), abspath(dst))

# def move_portraits()->None:
#     constants_path = os.path.join(CARD_PORTRAIT_PATH)

#     for file in os.listdir(CARD_PORTRAIT_PATH):
#         if file[0] != "_":
#             continue

#         src = os.path.join(CARD_PORTRAIT_PATH, file)
#         dst = os.path.normpath(os.path.join(CARD_PORTRAIT_PATH, "card_portraits", file))

#         open(dst, "w")
#         shutil.move(os.path.abspath(src), os.path.abspath(dst))

def ensure_clean_images()->None:
    raise NotImplementedError("ensure clean images doesn't exist idiot")