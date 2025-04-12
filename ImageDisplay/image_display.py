import sys
from PySide6.QtWidgets import (QApplication, QWidget)
from ImageDisplay.UI.image_dsplay_ui import Ui_layout_image_display


class ImageDisplay(QWidget, Ui_layout_image_display):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageDisplay()
    window.show()
    app.exec()
