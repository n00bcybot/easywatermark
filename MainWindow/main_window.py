import sys
import os
from PIL import Image
from PySide6.QtWidgets import (QMainWindow, QApplication, QFileDialog, QMessageBox, QListWidgetItem)

from PySide6.QtCore import Qt
from functions import static

from model.model import *
from PySide6.QtCore import Signal, Slot
from ToolBox.toolbox import ToolBoxWidget
from ImageViewer.image_viewer import ImageViewer
from ImageDisplay.image_display import ImageDisplay
from Flicker.flicker import FlickerWidget
from Process.process import ProcessDialog

from MainWindow.UI.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current_image_path = ""

        # Import ImageDisplay
        # --------------------------------------------------------------------------------------------------
        self.image_viewer = ImageViewer()
        self.layout_viewer.layout().addWidget(self.image_viewer)  # Connect to layout
        # --------------------------------------------------------------------------------------------------

        # Import ImageDisplay
        # --------------------------------------------------------------------------------------------------
        self.image_display = ImageDisplay()
        self.layout_display.layout().addWidget(self.image_display)

        # --------------------------------------------------------------------------------------------------

        # Import Flicker
        # --------------------------------------------------------------------------------------------------
        self.image_flicker = FlickerWidget()
        self.layout_flick.layout().addWidget(self.image_flicker)
        # --------------------------------------------------------------------------------------------------

        # Import ToolBoxWidget
        # --------------------------------------------------------------------------------------------------
        self.toolbox = ToolBoxWidget()
        self.layout_toolbox.layout().addWidget(self.toolbox)  # Connect to layout
        # --------------------------------------------------------------------------------------------------

        # Import Process dialog
        # --------------------------------------------------------------------------------------------------
        self.process_dialog = ProcessDialog()
        # --------------------------------------------------------------------------------------------------

    def set_statusbar(self, message):
        self.statusbar.showMessage(message)
