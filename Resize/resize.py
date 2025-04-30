import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget,
                               QToolBox)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt
from Resize.UI.resize_ui import Ui_wg_resize

from functions import static
from model import model


class ResizeWidget(QWidget, Ui_wg_resize):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

    def set_resize_data(self):
        model.process["resize"]["custom_size"]["width"] = self.le_width.text()
        model.process["resize"]["custom_size"]["height"] = self.le_height.text()

        model.process["resize"]["predefined_size"]["width"], _ = static.predefined_size(self.comb_presize.text)
        _, model.process["resize"]["predefined_size"]["height"] = static.predefined_size(self.comb_presize.text)

        model.process["resize"]["percent"] = self.le_percent.text()




# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ResizeWidget()
#     window.show()
#     app.exec()
