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

    def resizeEvent(self, event):
        # Scale the pixmap to label size when the UI is resized and keep aspect ratio
        for path, pixmap in zip(model["image_path"], model["pixmap_original"]):
            if path == model["current_image_path"]:
                label_size = self.lb_display.size()  # Get current label size
                scaled_pixmap = static.scale_pixmap(label_size, pixmap)
                # Swap the pixmap with its scaled version
                self.lb_display.setPixmap(scaled_pixmap)

        super().resizeEvent(event)
