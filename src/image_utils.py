from PIL.Image import Image
from PIL.Image import open as open_img
from PIL import ImageChops

from constants.project_constants import ACCEPTABLE_IMAGE_DIFF

def does_image_match_path(captured_image: Image, image_constant_path: str)->bool:
    constant_image = open_img(image_constant_path)
    image_diff = count_color(ImageChops.difference(captured_image, constant_image))
    return image_diff <= ACCEPTABLE_IMAGE_DIFF

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