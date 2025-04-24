import sys

from PySide6.QtWidgets import QApplication

from MainWindow.main_window import MainWindow
from Controller.controller import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    controller = Controller(window)

    window.show()
    sys.exit(app.exec())
