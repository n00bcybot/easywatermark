import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget
                               )
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt

from Main.UI.main_ui import Ui_MainWindow
from ToolBox.toolbox import ToolBoxWidget
from ImageViewer.image_viewer import ImageViewer
from ImageDisplay.image_display import ImageDisplay


class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        # Clear the image picker
        self.action_clear.triggered.connect(self.clear_image_picker)

        # Instantiate the ToolBoxWidget
        # --------------------------------------------------------------------------------------------------
        self.toolbox = ToolBoxWidget()
        self.layout_toolbox.layout().addWidget(self.toolbox)  # Connect the toolbox to existing layout
        # --------------------------------------------------------------------------------------------------

        # Instantiate ImageDisplay
        # --------------------------------------------------------------------------------------------------
        self.image_viewer = ImageViewer()
        self.layout_image_viewer.layout().addWidget(self.image_viewer)  # Connect to layout
        self.action_add.triggered.connect(self.add_image)  # Connect to menu
        self.image_viewer.list_viewer.itemClicked.connect(self.show_image_path)
        self.image_viewer.list_viewer.itemClicked.connect(self.display_image)
        # --------------------------------------------------------------------------------------------------

        # Instantiate ImageDisplay
        # --------------------------------------------------------------------------------------------------
        self.image_display = ImageDisplay()
        self.layout_image_display.layout().addWidget(self.image_display)
        # --------------------------------------------------------------------------------------------------

    def add_image(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Images", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )

        for file in files:
            # Create pixmap from image
            pixmap = QPixmap(file)

            # Create list item and add the pixmap to it
            item = QListWidgetItem(pixmap, "")
            # Use UserRole to store the data (the file path) and retrieve it later
            item.setData(Qt.UserRole, file)
            self.image_viewer.list_viewer.addItem(item)

    def clear_image_picker(self):
        self.image_viewer.list_viewer.clear()

    def show_image_path(self, item):
        # Retrieve user data, previously acquired in add_images
        image_path = item.data(Qt.UserRole)
        self.statusbar.showMessage(image_path)
        model["image_path"] = image_path

    def display_image(self, item):
        image_path = item.data(Qt.UserRole)
        pixmap = QPixmap(image_path)

        # Adding the pixmap to the dict ensure it is cached, which prevents reading it from disc every time
        # the UI is resized
        model["image_path"] = image_path
        model["pixmap_original"] = pixmap

        # Scale to label size
        scaled_pixmap = pixmap.scaled(self.image_display.label_image_display.size(),
                               Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_display.label_image_display.setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        # Scale the pixmap to label size when the UI is resized and keep aspect ratio
        if model["pixmap_original"]: # if the pixmap_original is set properly
            label_size = self.image_display.label_image_display.size()  # Get current label size
            scaled_pixmap = model["pixmap_original"].scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # Swap the pixmap with its scaled version
            self.image_display.label_image_display.setPixmap(scaled_pixmap)

        super().resizeEvent(event)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    from Model.model import model

    window = MainWindow()
    window.show()
    app.exec()
