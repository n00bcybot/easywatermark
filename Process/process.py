import sys
from PySide6.QtWidgets import (QApplication, QWidget, QDialog)
from Process.UI.process_ui import Ui_process_dialog


class ProcessDialog(QDialog, Ui_process_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProcessDialog()
    window.show()
    app.exec()
