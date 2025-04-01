# Import commonly used libraries

import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Browser.UI.browser_ui import Ui_Dialog


class BrowserWidget(qtw.QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        # Create file system model
        self.model = qtw.QFileSystemModel()
        self.model.setRootPath(qtc.QDir.homePath())  # Root directory


        # Connect model to the QTreeView
        self.tv_browser.setModel(self.model)
        # self.model.index(qtc.QDir.homePath())  # Default to home directory

        # Hide unwanted columns
        self.tv_browser.setColumnHidden(1, 1)
        self.tv_browser.setColumnHidden(2, 1)
        self.tv_browser.setColumnHidden(3, 1)
        self.tv_browser.expand(self.model.index(qtc.QDir.rootPath()))

        # Handle selection change
        self.tv_browser.selectionModel().selectionChanged.connect(self.display_selected_path)

    def display_selected_path(self):
        index = self.tv_browser.currentIndex()
        file_path = self.model.filePath(index)
        self.lb_browser.setText(file_path)  # Assuming your UI has a QLineEdit for displaying paths


if __name__ == "__main__":
    app = qtw.QApplication()
    window = BrowserWidget()
    window.show()
    app.exec()
