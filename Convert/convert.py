import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget,
                               QToolBox)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt
from Convert.UI.convert_ui import Ui_wg_convert


class ConvertWidget(QWidget, Ui_wg_convert):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConvertWidget()
    window.show()
    app.exec()
