from uuid import uuid4
from PIL.Image import Image

import os
import shutil

def gen_image_file(img: Image)->str:
    rand_path = f"constants\\img_constants\\temp\\_{str(uuid4())[:8]}.png"
    file = open(rand_path, "w")
    img.save(rand_path)
    return rand_path

def clear_temp()->None:
    for file in os.listdir("constants\\img_constants\\temp"):
        curr_file = os.path.dirname(__file__)
        constants_path = os.path.join(curr_file, "constants\\img_constants\\temp")
        src = os.path.join(constants_path, file)
        dst = os.path.normpath(os.path.join(constants_path, "..", file))
        path = open(dst, "w")
        shutil.move(os.path.abspath(src), os.path.abspath(dst))