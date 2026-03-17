from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, QPoint
from PySide6.QtWidgets import QListWidgetItem

model = {
    "image_paths": [],
    "pixmap_original": [],
    "output_folder": "",
    "initial_label_display_size": QSize,
    "current_image_path": "",
    "current_pixmap": QPixmap,
    "list_viewer_items": []
}

process = {
    "watermark_path": "",
    "watermark_pos": QPoint,
    "watermark_current_width": int,
    "watermark_current_height": int,
    "current_image_width": QSize.width,
    "current_image_height": QSize.height,

    "resize": {
        "custom_size": {
            "width": int,
            "height": int
        },
        "predefined_size": {
            "width": int,
            "height": int
        },
        "percent": int

    },
    "rename": {

    },
    "convert": {

    }
}

delimiter = {
    "dot": ".",
    "dash": "-",
    "underscore": "_"
}

data = {
    "directory": "",
    "file_name": "",
    "base_name": "",
    "path_no_ext": "",
    "extension": "",
    "replace_name": "",
    "remove_string": "",
    "remove_first": "",
    "remove_last": "",
    "prefix": "",
    "suffix": "",
    "delimiter": "",
    "counter": "",
    "new_name": ""
}

images = {
        "name": "",
        "path": "",
        "pixmap": QPixmap,
        "list_widget_item": QListWidgetItem
}