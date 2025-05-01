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

        from Watermark.watermark_label import WatermarkLabel

        # Replace the QLabel with custom label
        layout = self.lb_display.parent().layout()  # Or however it's laid out
        layout.removeWidget(self.lb_display)
        self.lb_display.deleteLater()

        self.lb_display = WatermarkLabel(self)

        layout.addWidget(self.lb_display)

        self.image_paths = model["image_paths"]
        self.current_path = ""

    def display_image(self, path):
        model["current_image_paths"] = path
        self.current_path = path
        pixmap = static.make_pixmap(path)
        model["current_pixmap"] = pixmap
        scaled_pixmap = static.scale_from_pixmap(self.lb_display.size(), pixmap)
        self.lb_display.setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        for path in model["image_paths"]:
            if path == self.current_path:
                # Display the first image in the list upon adding the images
                scaled_pixmap = static.scale_from_pixmap(self.lb_display.size(), model["current_pixmap"])
                self.lb_display.setPixmap(scaled_pixmap)

        super().resizeEvent(event)
