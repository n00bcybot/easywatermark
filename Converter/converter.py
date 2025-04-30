import sys
from PySide6.QtWidgets import (QApplication, QWidget)
from PySide6.QtCore import Qt, Signal, Slot
from Converter.UI.converter_ui import Ui_wg_convert

from model.model import *


class ConverterWidget(QWidget, Ui_wg_convert):

    # Create the signal
    sg_indexChanged = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.cb_convert.currentIndexChanged.connect(self.on_index_change)

    # Emit signal when different item is selected in the combobox
    @Slot()
    def on_index_change(self):
        extension = self.cb_convert.currentText()
        self.sg_indexChanged.emit(extension)




# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ConverterWidget()
#     window.show()
#     app.exec()
