import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget,
                               QToolBox)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt
from ToolBox.UI.toolbox_ui import Ui_wg_toolbox
from Resize.resize import ResizeWidget
from Convert.convert import ConvertWidget


class ToolBoxWidget(QWidget, Ui_wg_toolbox, ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.resize_widget = ResizeWidget()
        self.page_2.layout().addWidget(self.resize_widget)

        # -------------------------------------------------------------------------------------------
        self.convert_widget = ConvertWidget()
        self.page_4.layout().addWidget(self.convert_widget)
        #


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToolBoxWidget()
    window.show()
    app.exec()
