from supervision.draw.color import ColorPalette, Color
from PIL import ImageColor
import yaml
import cv2


def hex_to_rgb(hex_colors: list):
    return [ImageColor.getcolor(color, 'RGB') for color in hex_colors]


def create_colorpalette(rgb_colors: list):
    return ColorPalette([Color(r, g, b) for r, g, b in rgb_colors])


def load_yaml_as_dict(path_to_yaml: str) -> dict:
    with open(path_to_yaml, 'r') as file:
        data = yaml.safe_load(file)
    return data


def save_file(input, target:str):
    with open(target, 'wb') as t:
        t.write(input.getbuffer())
        t.close()

    print("The file was successfully saved!")
