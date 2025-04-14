import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget,
                               QToolBox)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt
from Flicker.UI.flicker_ui import Ui_wg_flicker


class FlickerWidget(QWidget, Ui_wg_flicker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlickerWidget()
    window.show()
    app.exec()
