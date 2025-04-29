import sys
from PySide6.QtWidgets import (QApplication, QWidget)
from PySide6.QtCore import Qt, Signal, Slot, QSize
from model.model import *
from functions import static
from ImageDisplay.UI.image_dsplay_ui import Ui_layout_image_display


class ImageDisplay(QWidget, Ui_layout_image_display):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.image_paths = model["image_paths"]
        self.current_path = ""

    def display_image(self, path):
        model["current_image_paths"] = path
        self.current_path = path
        model["current_pixmap"] = static.make_pixmap(self.current_path)
        scaled_pixmap = static.scale_from_pixmap(self.lb_display.size(), model["current_pixmap"])
        self.lb_display.setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        for path in model["image_paths"]:
            if path == self.current_path:
                # Display the first image in the list upon adding the images
                scaled_pixmap = static.scale_from_pixmap(self.lb_display.size(), model["current_pixmap"])
                self.lb_display.setPixmap(scaled_pixmap)

        super().resizeEvent(event)
