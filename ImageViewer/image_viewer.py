import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog, QListWidgetItem)
from PySide6.QtCore import Qt, Signal, Slot, QSize
from model.model import *
from ImageViewer.UI.image_viewer_ui import Ui_wg_image_viewer


class ImageViewer(QWidget, Ui_wg_image_viewer):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

    def add_image(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Images", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )

        for file_path in files:
            # Create pixmap from image
            pixmap = QPixmap(file_path)

            # Create list item and add the pixmap to it
            item = QListWidgetItem(pixmap, "")
            # Use UserRole to store the data (the file path) and retrieve it later
            item.setData(Qt.UserRole, file_path)
            # Check if the file is already in the list:
            if file_path not in model["image_path"]:
                model["image_path"].append(file_path)
                model["pixmap_original"].append(pixmap)
                self.list_viewer.addItem(item)
            item.setSelected(True)

    def clear_image_picker(self):
        self.list_viewer.clear()  # Clear image viewer
        model["image_path"].clear()  # Clear the paths list as well

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ImageViewer()
#     window.show()
#     app.exec()
