import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog)
from PySide6.QtCore import Qt, Signal, Slot
from Watermark.UI.watermark_ui import Ui_wg_watermark

from model.model import *


class Watermark(QWidget, Ui_wg_watermark):
    sg_sendFilePath = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.bt_browse.clicked.connect(self.add_watermark)

    def add_watermark(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        self.sg_sendFilePath.emit(file)
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ConverterWidget()
#     window.show()
#     app.exec()
