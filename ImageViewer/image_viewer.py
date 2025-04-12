import sys
from PySide6.QtWidgets import (QApplication, QListWidget)
from ImageViewer.UI.image_viewer_ui import Ui_wg_image_viewer


class ImageViewer(QListWidget, Ui_wg_image_viewer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    app.exec()
