# Import commonly used libraries

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Main.UI.Main_ui import Ui_MainWindow
from Browser.browser import BrowserWidget


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        # Close the windows from the menu
        self.action_quit.triggered.connect(self.close)

        self.browser = BrowserWidget()

        # Add the custom widget to the groupbox layout
        self.gb_layout.addWidget(self.browser)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
