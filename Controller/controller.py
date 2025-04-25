from PySide6.QtCore import QObject, Slot
from model.model import *


class Controller(QObject):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window  # Import MainWindow
        # self.converter = self.main_window.converter  # Import any other widget

        # Connect the signal from Converter to redirecting slot
        # self.converter.indexChanged.connect(self.receive_converter_indexChanged)

    # Redirect indexChanged signal to update MainWindow status bar
    @Slot(str)
    def receive_converter_indexChanged(self, message: str):
        self.main_window.statusbar.setText(message)

        data["extension"] = message

