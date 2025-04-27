import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget,
                               QToolBox)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt, Signal, Slot
from Flicker.UI.flicker_ui import Ui_wg_flicker


class FlickerWidget(QWidget, Ui_wg_flicker):
    sg_display_next = Signal()
    sg_display_previous = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.bt_next.clicked.connect(self.on_next_clicked)
        self.bt_previous.clicked.connect(self.on_previous_clicked)

    @Slot()
    def on_next_clicked(self):
        self.sg_display_next.emit()

    @Slot()
    def on_previous_clicked(self):
        self.sg_display_previous.emit()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = FlickerWidget()
#     window.show()
#     app.exec()
