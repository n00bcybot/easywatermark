import os
from model.model import *
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Qt


def make_pixmap(path):
    pixmap = QPixmap(path)
    return pixmap


def scale_pixmap(size, path):
    pixmap = make_pixmap(path)
    scaled_pixmap = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    return scaled_pixmap


def scale_from_pixmap(size, pixmap):
    scaled_pixmap = pixmap.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
    return scaled_pixmap


def list_widget_item(image_path):
    item = QListWidgetItem(QPixmap(image_path), "")
    return item


def image_format(_format):
    match _format:
        case "JPG":
            return ".jpg"
        case "PNG":
            return ".png"
        case "TIFF":
            return ".tiff"


def set_delimiter(text):
    match text:
        case ". (dot)":
            return "."
        case "- (dash)":
            return "-"
        case "_ (underscore)":
            return "_"


def get_digit(selection):
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


def remove_string(name, string):
    if str(string) in name:
        new_name = name.replace(str(string), "")
        return new_name


def remove_first(name, number):
    if number:
        if int(number) < len(name):
            new_name = name[int(number):]
            return str(new_name)
    else:
        return name


def remove_last(name, number):
    if number:
        if int(number) < len(name):
            new_name = name[:-int(number)]
            return str(new_name)
    else:
        return name


def predefined_size(selection):
    match selection:
        case "1920 x 1080 (Full HD)":
            width = 1920
            height = 1080
            return width, height
        case "800 x 600":
            width = 800
            height = 600
            return width, height


def set_image_data(image_path):
    data["directory"], data["file_name"] = os.path.split(image_path)
    data["path_no_ext"], data["extension"] = os.path.splitext(image_path)
    data["base_name"] = data["file_name"].replace(data["extension"], "")


def reduce_by_percent(percent, width, height):
    reduce_by = (100 - percent) / 100
    new_width = width * reduce_by
    new_height = height * reduce_by
    return round(new_width), round(new_height)


def keep_ratio(image_width, image_height, new_width, new_height):
    if image_width > image_height:
        ratio = image_width / new_width
        new_height = round(image_height / ratio)
        return new_width, new_height

    else:
        ratio = image_height / new_height
        new_width = round(image_width / ratio)
        return new_width, new_height
