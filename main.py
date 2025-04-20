import sys
import os
from PIL import Image
from PySide6.QtWidgets import (QMainWindow, QApplication, QListWidgetItem, QPushButton, QFileDialog, QListView,
                               QListWidgetItem, QListWidget, QDialog, QMessageBox)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt

from Model.model import *
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

        # Import ImageDisplay
        # --------------------------------------------------------------------------------------------------
        self.image_viewer = ImageViewer()
        self.layout_viewer.layout().addWidget(self.image_viewer)  # Connect to layout
        self.action_add.triggered.connect(self.add_image)  # Connect to menu
        self.image_viewer.list_viewer.itemClicked.connect(self.show_image_path)  # Display path in status bar
        self.image_viewer.list_viewer.itemClicked.connect(self.display_image)  # Display image in viewer
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
        # --------------------------------------------------------------------------------------------------

        # Import ToolBoxWidget
        # --------------------------------------------------------------------------------------------------
        self.toolbox = ToolBoxWidget()
        self.layout_toolbox.layout().addWidget(self.toolbox)  # Connect to layout
        self.toolbox.rename_widget.chb_rename.checkStateChanged.connect(self.run_rename)
        self.toolbox.rename_widget.chb_add_count.checkStateChanged.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.rb_change.clicked.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.rb_keep.clicked.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.le_new_name.textChanged.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.le_add_prefix.textChanged.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.le_add_suffix.textChanged.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.le_remove_string.textChanged.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.le_remove_first.textChanged.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.le_remove_last.textChanged.connect(self.set_dynamic_preview)

        self.toolbox.rename_widget.comb_digit.textActivated.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.comb_digit.textActivated.connect(
            self.get_digit(self.toolbox.rename_widget.comb_digit.currentText))
        self.toolbox.rename_widget.comb_delimiter.textActivated.connect(self.set_dynamic_preview)
        self.toolbox.rename_widget.comb_delimiter.textActivated.connect(self.set_delimiter)

        # --------------------------------------------------------------------------------------------------

        # Import Process dialog
        # --------------------------------------------------------------------------------------------------
        self.process_dialog = ProcessDialog()
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

    def set_delimiter(self, text):
        match text:
            case ". (dot)":
                return "."
            case "- (dash)":
                return "-"
            case "_ (underscore)":
                return "_"

    def get_digit(self, selection):
        match selection:
            case "1 digit":
                return 1
            case "2 digits":
                return 2
            case "3 digits":
                return 3
            case "4 digits":
                return 4
            case "5 digits":
                return 5
            case "6 digits":
                return 6

    def remove_string(self, name, string):
        if str(string) in name:
            new_name = name.replace(str(string), "")
            return new_name
    def remove_first(self, name, number):
        if number < len(name):
            new_name = name[number:len(name)]
            return new_name

    def remove_last(self, name,number):
        if number < len(name):
            new_name = name[0:number]
            return new_name

    def set_image_data(self, image_path):
        data["directory"], data["file_name"] = os.path.split(image_path)
        data["path_no_ext"], data["extension"] = os.path.splitext(image_path)
        data["base_name"] = data["file_name"].replace(data["extension"], "")

    def set_rename_data(self):
        index = 1
        data["replace_name"] = self.toolbox.rename_widget.le_new_name.text()
        data["remove_string"] = self.toolbox.rename_widget.le_remove_string.text()
        data["remove_first"] = self.toolbox.rename_widget.le_remove_first.text()
        data["remove_last"] = self.toolbox.rename_widget.le_remove_last.text()
        data["prefix"] = self.toolbox.rename_widget.le_add_prefix.text()
        data["suffix"] = self.toolbox.rename_widget.le_add_suffix.text()
        count = self.get_digit(self.toolbox.rename_widget.comb_digit.currentText())
        data["counter"] = f"{index:0{count}}"
        print(data["counter"])
        data["delimiter"] = self.set_delimiter(self.toolbox.rename_widget.comb_delimiter.currentText())

    def set_preview(self):
        self.set_image_data(model["image_path"][0])
        result = ("/" + data["prefix"] + data["replace_name"] + data["base_name"] + data["suffix"] +
                  data["counter"] + data["extension"])
        self.toolbox.rename_widget.lb_preview.setText(result)

    def set_dynamic_preview(self):
        self.set_rename_data()
        if not self.toolbox.rename_widget.chb_add_count.isChecked():
            data["counter"] = ""

        vars_list = []
        dm = data["delimiter"]

        if self.toolbox.rename_widget.rb_keep.isChecked():
            if self.toolbox.rename_widget.rb_remove_string.isChecked():
                data["base_name"] = self.remove_string(data["base_name"], self.toolbox.rename_widget.le_remove_string.text())
            elif self.toolbox.rename_widget.rb_remove_first.isChecked():
                data["base_name"] = self.remove_first(data["base_name"], int(self.toolbox.rename_widget.le_remove_first.text()))
            elif self.toolbox.rename_widget.rb_remove_last.isChecked():
                data["base_name"] = self.remove_last(data["base_name"], int(self.toolbox.rename_widget.le_remove_last.text()))

            vars_list = [data["prefix"], data["base_name"], data["suffix"], data["counter"]]

        elif self.toolbox.rename_widget.rb_change.isChecked():
            vars_list = [data["prefix"], data["replace_name"], data["suffix"], data["counter"]]

        variable = [var for var in vars_list if var]
        new_name = "/" + dm.join(variable) + data["extension"]
        print(vars_list)

        self.toolbox.rename_widget.lb_preview.setText(new_name)


    def run_rename(self):

        self.toolbox.rename_widget.chb_rename.clicked.connect(self.set_preview)

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
        # Display the first image in the list upon adding images
        self.image_display.label_image_display.setPixmap(scaled_pixmap)
        # Show image path in the statusbar
        self.statusbar.showMessage(model["image_path"][0])

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
