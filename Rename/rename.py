import sys
import os
from PySide6.QtWidgets import (QApplication, QWidget, )
from model.model import *

from Rename.UI.rename_ui import Ui_Rename


class RenameWidget(QWidget, Ui_Rename):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements




#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = RenameWidget()
#     window.show()
#     app.exec()
