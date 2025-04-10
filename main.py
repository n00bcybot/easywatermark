import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget
                               )
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt

from main_ui import Ui_MainWindow
from ToolBox.toolbox import ToolBoxWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        # Set app size
        self.window_size = QSize(1200, 700)

        # Instantiate the toolbox
        self.toolbox = ToolBoxWidget()

        # Connect the toolbox to existing layout
        self.toolbox.setParent(self.layout_toolbox)
        # self.layout_toolbox.setMaximumWidth(800)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
