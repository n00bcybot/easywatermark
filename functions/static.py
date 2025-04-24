import os
from model.model import *


def image_format(self, _format):
    match _format:
        case "JPG":
            return ".jpg"
        case "PNG":
            return ".png"
        case "TIFF":
            return ".tiff"


def set_delimiter(self, text):
    match text:
        case ". (dot)":
            return "."
        case "- (dash)":
            return "-"
        case "_ (underscore)":
            return "_"


def get_digit(self, selection):
    match selection:
        case "1 digit":
            return 1
        case "2 digits":
            return 2
        case "3 digits":
            return 3
        case "4 digits":
            return 4
        case "5 digits":
            return 5
        case "6 digits":
            return 6


def remove_string(self, name, string):
    if str(string) in name:
        new_name = name.replace(str(string), "")
        return new_name


def remove_first(self, name, number):
    if number:
        if int(number) < len(name):
            new_name = name[int(number):]
            return str(new_name)
    else:
        return name


def remove_last(self, name, number):
    if number:
        if int(number) < len(name):
            new_name = name[:-int(number)]
            return str(new_name)
    else:
        return name


def predefined_size(self, selection):
    match selection:
        case "1920 x 1080 (Full HD)":
            width = 1920
            height = 1080
            return width, height
        case "800 x 600":
            width = 800
            height = 600
            return width, height


def set_image_data(self, image_path):
    data["directory"], data["file_name"] = os.path.split(image_path)
    data["path_no_ext"], data["extension"] = os.path.splitext(image_path)
    data["base_name"] = data["file_name"].replace(data["extension"], "")
