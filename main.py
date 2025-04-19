import sys
import os
from PIL import Image
from PySide6.QtWidgets import (QMainWindow, QApplication, QListWidgetItem, QPushButton, QFileDialog, QListView,
                               QListWidgetItem, QListWidget, QDialog, QMessageBox)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt

from Main.UI.main_ui import Ui_MainWindow
from ToolBox.toolbox import ToolBoxWidget
from ImageViewer.image_viewer import ImageViewer
from ImageDisplay.image_display import ImageDisplay
from Flicker.flicker import FlickerWidget
from Process.process import ProcessDialog


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.current_path = ""

        # Clear the image picker
        self.action_clear.triggered.connect(self.clear_image_picker)

        # Import ToolBoxWidget
        # --------------------------------------------------------------------------------------------------
        self.toolbox = ToolBoxWidget()
        self.layout_toolbox.layout().addWidget(self.toolbox)  # Connect the toolbox to existing layout
        # --------------------------------------------------------------------------------------------------

        # Import ImageDisplay
        # --------------------------------------------------------------------------------------------------
        self.image_viewer = ImageViewer()
        self.layout_viewer.layout().addWidget(self.image_viewer)  # Connect to layout
        self.action_add.triggered.connect(self.add_image)  # Connect to menu
        self.image_viewer.list_viewer.itemClicked.connect(self.show_image_path)
        self.image_viewer.list_viewer.itemClicked.connect(self.display_image)

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
        self.image_flicker.bt_next.clicked.connect(self.show_next_image)
        self.image_flicker.bt_previous.clicked.connect(self.show_previous_image)

        # Import Process dialog
        # --------------------------------------------------------------------------------------------------
        self.process_dialog = ProcessDialog()
        # Connect menubar to open process dialog
        self.action_process.triggered.connect(self.process_show_dialog)
        self.process_dialog.pb_select_folder.clicked.connect(self.process_select_folder)
        self.process_dialog.pb_process.clicked.connect(self.process_batch)
        # --------------------------------------------------------------------------------------------------

    def image_format(self, image_format):
        match image_format:
            case "JPG":
                return ".jpg"
            case "PNG":
                return ".png"
            case "TIFF":
                return ".tiff"

    def process_batch(self):
        if model["output_folder"] == "":
            QMessageBox.information(self, "Output Folder Not Selected", "Please select an output folder!")

        else:
            resized = False
            # Get selected format from the format dropdown in "Save As"
            selected_format = self.toolbox.convert_widget.cb_convert.currentText()
            # selected_format = self.image_converter.cb_convert.currentText()
            for image_path in model["image_path"]:
                extension = os.path.splitext(image_path)[1]
                full_name = os.path.split(image_path)[1]
                new_name = str(full_name).replace(extension, "")

                # Change format
                extension = self.image_format(selected_format)
                # Create image object
                image = Image.open(image_path)

                if resized:
                    image_resized = image.resize((300, 300), Image.Resampling.LANCZOS)  # Resize
                    image_resized.save(model["output_folder"] + new_name + "_resized" + extension)  # Rename and save
                else:
                    image.save(model["output_folder"] + new_name + extension)  # Rename and save

    def process_select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        model["output_folder"] = folder + "/"

    def process_show_dialog(self):
        self.process_dialog.lw_image_list.clear()
        # Add the images from image viewer (model["image_path"])
        for image in model["image_path"]:
            self.process_dialog.lw_image_list.addItem(image)
        # Use exec() instead of show() to block the main window until the dialog is closed
        self.process_dialog.exec()

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
                self.image_viewer.list_viewer.addItem(item)

        # Set current path to the first image in the list. At this point self.current path is still empty,
        # unless image is clicked in the picker
        self.current_path = model["image_path"][0]

        # Display the first image in the list upon adding the images
        scaled_pixmap = model["pixmap_original"][0].scaled(self.image_display.label_image_display.size(),
                                                           Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_display.label_image_display.setPixmap(scaled_pixmap)

    def clear_image_picker(self):
        self.image_viewer.list_viewer.clear()  # Clear image viewer
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

    def resizeEvent(self, event):

        # Scale the pixmap to label size when the UI is resized and keep aspect ratio
        for path, pixmap in zip(model["image_path"], model["pixmap_original"]):
            if path == self.current_path:
                label_size = self.image_display.label_image_display.size()  # Get current label size
                scaled_pixmap = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                # Swap the pixmap with its scaled version
                self.image_display.label_image_display.setPixmap(scaled_pixmap)

        super().resizeEvent(event)

    def show_next_image(self):

        current_index = model["image_path"].index(self.current_path)
        if int(current_index) < len(model["image_path"]) - 1:
            self.current_path = model["image_path"][current_index + 1]
            self.display_image()
        else:
            self.current_path = model["image_path"][0]
            self.display_image()

    def show_previous_image(self):
        current_index = model["image_path"].index(self.current_path)
        if int(current_index) > 0:
            self.current_path = model["image_path"][current_index - 1]
            self.display_image()
        else:
            self.current_path = model["image_path"][len(model["image_path"]) - 1]
            self.display_image()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    from Model.model import model

    window = MainWindow()
    window.show()
    app.exec()
