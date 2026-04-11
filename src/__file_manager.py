import os
import shutil

from uuid import uuid4
from PIL.Image import Image

from constants.project_constants import CARD_PORTRAIT_PATH
from game_window_handler import GameWindowHandler
from game_stat_handler import GameStatHandler

def scroll_and_gen(window_handler: GameWindowHandler, stat_handler: GameStatHandler):
    portraits = window_handler.scroll_hand(stat_handler)
    for portrait in portraits:
        gen_image_file(portrait)

def gen_image_file(img: Image)->str:
    rand_path = f"constants\\img_constants\\temp\\_{str(uuid4())[:8]}.png"
    file = open(rand_path, "w")
    img.save(rand_path)
    return rand_path

def clear_temp()->None:
    temp_path = os.path.join(CARD_PORTRAIT_PATH, "temp")

    for file in os.listdir(temp_path):
        src = os.path.join(temp_path, file)
        dst = os.path.normpath(os.path.join(temp_path, "..", file))

        open(dst, "w")
        shutil.move(os.path.abspath(src), os.path.abspath(dst))

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