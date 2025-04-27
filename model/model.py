from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize

model = {
    "image_path": [],
    "pixmap_original": [],
    "output_folder": "",
    "initial_label_display_size": QSize,
    "current_image_path": ""
}

process = {
    "watermark": {

    },

    "resize": {
        "custom_size": {
            "width": int,
            "height": int
        },
        "predefined_size": {
            "width": int,
            "height": int
        },
        "percent": {
            "width": int,
            "height": int
        }

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
