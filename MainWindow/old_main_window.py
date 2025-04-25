import sys
import os
from PIL import Image
from PySide6.QtWidgets import (QMainWindow, QApplication, QFileDialog, QMessageBox, QListWidgetItem)

from PySide6.QtCore import Qt

from model.model import *
from MainWindow.UI.main_window_ui import Ui_MainWindow
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



    def set_rename_data(self, index):

        data["replace_name"] = self.toolbox.rename_widget.le_new_name.text()
        data["remove_string"] = self.toolbox.rename_widget.le_remove_string.text()
        data["remove_first"] = self.toolbox.rename_widget.le_remove_first.text()
        data["remove_last"] = self.toolbox.rename_widget.le_remove_last.text()
        data["prefix"] = self.toolbox.rename_widget.le_add_prefix.text()
        data["suffix"] = self.toolbox.rename_widget.le_add_suffix.text()
        count = self.get_digit(self.toolbox.rename_widget.comb_digit.currentText())
        data["counter"] = f"{index:0{count}}"
        data["delimiter"] = self.set_delimiter(self.toolbox.rename_widget.comb_delimiter.currentText())
        selected_format = self.toolbox.convert_widget.cb_convert.currentText()
        data["extension"] = self.image_format(selected_format)

    def set_preview(self):
        self.set_image_data(model["image_path"][0])
        result = ("/" + data["prefix"] + data["replace_name"] + data["base_name"] + data["suffix"] +
                  data["counter"] + data["extension"])
        self.toolbox.rename_widget.lb_preview.setText(result)

    def set_dynamic_preview(self):
        self.set_rename_data(index=1)
        if not self.toolbox.rename_widget.chb_add_count.isChecked():
            data["counter"] = ""

        vars_list = []
        dm = data["delimiter"]

        if self.toolbox.rename_widget.rb_keep.isChecked():
            data["new_name"] = data["base_name"]
            if self.toolbox.rename_widget.rb_remove_string.isChecked():
                data["new_name"] = self.remove_string(data["base_name"],
                                                      str(self.toolbox.rename_widget.le_remove_string.text()))
            elif self.toolbox.rename_widget.rb_remove_first.isChecked():
                data["new_name"] = self.remove_first(data["base_name"],
                                                     self.toolbox.rename_widget.le_remove_first.text())
            elif self.toolbox.rename_widget.rb_remove_last.isChecked():
                data["new_name"] = self.remove_last(data["base_name"], self.toolbox.rename_widget.le_remove_last.text())

            if data["new_name"] == "":
                vars_list = [data["prefix"], data["base_name"], data["suffix"], data["counter"]]
            else:
                vars_list = [data["prefix"], data["new_name"], data["suffix"], data["counter"]]

        elif self.toolbox.rename_widget.rb_change.isChecked():
            vars_list = [data["prefix"], data["replace_name"], data["suffix"], data["counter"]]

        variable = [var for var in vars_list if var]
        new_name = "/" + dm.join(variable) + data["extension"]

        print(vars_list)

        self.toolbox.rename_widget.lb_preview.setText(new_name)

        # Set the new name for later use in processing
        new_list = [var for var in vars_list if var != data["counter"]]
        data["new_name"] = dm.join(new_list)

    def run_rename(self):
        self.toolbox.rename_widget.chb_rename.clicked.connect(self.set_preview)

    def process_batch(self):
        if model["output_folder"] == "":
            QMessageBox.information(self, "Output Folder Not Selected", "Please select an output folder!")

        else:

            index = 1
            for image_path in model["image_path"]:

                self.set_image_data(image_path)
                self.set_rename_data(index)

                # Create image object
                image = Image.open(image_path)
                image_resized = None

                if self.toolbox.resize_widget.chb_resize.isChecked():
                    if self.toolbox.resize_widget.rb_custom.isChecked():
                        width = int(self.toolbox.resize_widget.le_width.text())
                        height = int(self.toolbox.resize_widget.le_height.text())
                        image_resized = image.resize((width, height), Image.Resampling.LANCZOS)  # Resize

                    elif self.toolbox.resize_widget.rb_percent.isChecked():
                        image_resized = image.resize((300, 300), Image.Resampling.LANCZOS)

                    elif self.toolbox.resize_widget.rb_predefined.isChecked():
                        width, height = self.predefined_size(self.toolbox.resize_widget.comb_presize.currentText())
                        image_resized = image.resize((width, height), Image.Resampling.LANCZOS)

                    if self.toolbox.rename_widget.chb_add_count.isChecked():
                        image_resized.save(model["output_folder"] + data["new_name"] + data["counter"] + data["extension"])
                    else:
                        image_resized.save(model["output_folder"] + data["base_name"] + data["extension"])
                else:
                    if self.toolbox.rename_widget.chb_add_count.isChecked():
                        image.save(model["output_folder"] + data["new_name"] + data["counter"] + data["extension"])
                    else:
                        image.save(model["output_folder"] + data["base_name"] + data["extension"])

                index += 1

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
    from model.model import model

    window = MainWindow()
    window.show()
    app.exec()