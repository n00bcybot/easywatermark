import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog, QListWidgetItem)
from PySide6.QtCore import Qt, Signal, Slot, QSize
from model.model import *
from ImageViewer.UI.image_viewer_ui import Ui_wg_image_viewer


class ImageViewer(QWidget, Ui_wg_image_viewer):

    signal_set_statusbar = Signal(str)
    signal_display_pixmap = Signal(QPixmap)

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.current_path = ""
        self.label_display_size = None


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

        # Set current path to the first image in the list. At this point self.current path is still empty,
        # unless image is clicked in the picker
        self.current_path = model["image_path"][0]

        # Display the first image in the list upon adding the images
        scaled_pixmap = model["pixmap_original"][0] #.scaled(model["initial_label_display_size"], Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # Display the first image in the list upon adding images
        self.emit_display_image(scaled_pixmap)
        # Show image path in the statusbar
        self.emit_status_bar(model["image_path"][0])

    @Slot()
    def emit_status_bar(self, message):
        self.signal_set_statusbar.emit(message)

    @Slot(QPixmap)
    def emit_display_image(self, pixmap):
        self.signal_display_pixmap.emit(pixmap)


    def clear_image_picker(self):
        self.list_viewer.clear()  # Clear image viewer
        model["image_path"].clear()  # Clear the paths list as well

    def show_image_path(self, item):
        # Retrieve user data, previously acquired in add_images
        self.current_path = item.data(Qt.UserRole)
        self.statusbar.showMessage(self.current_path)


    def display_image(self):

        for path, pixmap in zip(model["image_path"], model["pixmap_original"]):
            if path == self.current_path:
                # Scale to label size
                scaled_pixmap = pixmap.scaled(self.image_display.label_image_display.size(),
                                              Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.image_display.label_image_display.setPixmap(scaled_pixmap)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ImageViewer()
#     window.show()
#     app.exec()
