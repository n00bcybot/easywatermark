from PySide6.QtGui import QPixmap

model = {
    "image_path": [],
    "pixmap_original": [],
    "output_folder": ""
}

process_settings = {
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