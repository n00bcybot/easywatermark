from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget
from PySide6.QtCore import QObject, Slot, Signal, QSize
from PySide6.QtGui import Qt
from PIL import Image

import model.model
from model.model import *
from functions import static


class Controller(QWidget, QObject):

    def __init__(self, main_window):
        super().__init__()

        self.current_path = ""
        self.list_widget_item = QListWidgetItem

        self.main_window = main_window  # Import MainWindow
        self.converter = self.main_window.toolbox.convert_widget  # Import any other widget
        self.image_viewer = self.main_window.image_viewer
        self.image_display = self.main_window.image_display
        self.flicker = self.main_window.image_flicker
        self.rename = self.main_window.toolbox.rename_widget
        self.resize = self.main_window.toolbox.resize_widget
        self.watermark = self.main_window.toolbox.watermark
        self.process = self.main_window.process
        self.watermark_label = self.main_window.watermark_label

        self.main_window.action_add.triggered.connect(self.add_images)
        self.main_window.action_clear.triggered.connect(self.image_viewer.clear_list_viewer)
        self.main_window.action_remove.triggered.connect(self.rebuild_viewer)
        self.main_window.action_process.triggered.connect(self.process_show_dialog)

        self.image_viewer.sg_selected_item.connect(self.on_item_clicked)
        self.image_viewer.sg_selected_item.connect(self.receive_item)

        self.flicker.sg_display_next.connect(self.show_next_image)
        self.flicker.sg_display_previous.connect(self.show_previous_image)

        self.rename.receive_extension(self.converter.cb_convert.currentText())

        self.converter.sg_indexChanged.connect(self.extension_changed)

        self.watermark.sg_sendFilePath.connect(self.receive_watermark_path)

        self.process.pb_select_folder.clicked.connect(self.process_select_folder)
        self.process.pb_process.clicked.connect(self.process_batch)

    # ------------------------------------------------------------------------------------------------------------------
    # Adding, removing, displaying images
    # ------------------------------------------------------------------------------------------------------------------

    # Add images to the image viewer
    def add_images(self):
        files, _ = QFileDialog.getOpenFileNames(
            self.main_window, "Select Images", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        for file_path in files:
            item = static.list_widget_item(file_path)  # Create list widget item from images on disk
            if file_path not in model["image_paths"]:  # Check if the file is already in the list:
                model["image_paths"].append(file_path)  # Create/update image list
                model["list_viewer_items"].append(item)  # Create/update list widget items list

        self.add_list_viewer_item()  # Add all items in the list widget items list to the viewer
        self.current_path = model["current_image_path"] = model["image_paths"][0]  # Set current image path
        model["current_pixmap"] = static.make_pixmap(self.current_path)  # Create pixmap from initial image
        self.image_display.display_image(self.current_path)
        self.main_window.set_statusbar(self.current_path)  # Show image path in the statusbar

    def add_list_viewer_item(self):
        for item in model["list_viewer_items"]:
            self.image_viewer.list_viewer.addItem(item)

    def receive_item(self, item):
        self.list_widget_item = item

    def rebuild_viewer(self):
        for item in model["list_viewer_items"]:
            if item.isSelected():
                index = model["list_viewer_items"].index(item)
                self.image_viewer.list_viewer.takeItem(index)
                model["list_viewer_items"].remove(item)
                model["image_paths"].remove(model["image_paths"][index])

    def add_items(self):
        self.image_viewer.add_list_viewer_item()

    def clear_viewer(self):
        self.image_viewer.list_viewer.clear()

    @Slot(int)
    def on_item_clicked(self, item):
        path = model["image_paths"][model["list_viewer_items"].index(item)]
        self.image_display.display_image(path)
        self.main_window.set_statusbar(path)

    def send_list_widget_item(self, item):
        # Add images
        self.image_viewer.add_list_viewer_item(item)

    def get_current_path(self, path):
        self.current_path = path

    def show_next_image(self):
        current_list = model["image_paths"]
        if int(current_list.index(self.current_path)) < len(current_list) - 1:
            self.current_path = current_list[current_list.index(self.current_path) + 1]
            # model["list_viewer_items"][current_list.index(self.current_path)].setSelected(True)
        else:
            self.current_path = current_list[0]
        self.main_window.set_statusbar(self.current_path)
        self.image_display.display_image(self.current_path)

    def show_previous_image(self):
        current_list = model["image_paths"]
        if int(current_list.index(self.current_path)) > 0:
            self.current_path = current_list[current_list.index(self.current_path) - 1]
            # model["list_viewer_items"][current_list.index(self.current_path)].setSelected(True)
        else:
            self.current_path = current_list[len(current_list) - 1]
        self.main_window.set_statusbar(self.current_path)
        self.image_display.display_image(self.current_path)

    # ------------------------------------------------------------------------------------------------------------------
    # Watermark
    # ------------------------------------------------------------------------------------------------------------------

    def receive_watermark_path(self, path):
        process["watermark_path"] = path
        self.image_display.lb_display.watermark = QPixmap(path)
        self.image_display.lb_display.update()

    # ------------------------------------------------------------------------------------------------------------------
    # Rename
    # ------------------------------------------------------------------------------------------------------------------

    def extension_changed(self, text):
        self.rename.receive_extension(text)

    @Slot(int)
    def set_image_data(self, index):
        self.rename.set_rename_data(index)

    # ------------------------------------------------------------------------------------------------------------------
    # Process
    # ------------------------------------------------------------------------------------------------------------------

    def process_show_dialog(self):
        self.process.lw_image_list.clear()
        # Add the images from image viewer (model["image_path"])
        for image in model["image_paths"]:
            self.process.lw_image_list.addItem(image)
        # Use exec() instead of show() to block the main window until the dialog is closed
        self.process.exec()

    def process_batch(self):

        if model["output_folder"] == "":
            QMessageBox.information(self, "Output folder fot selected", "Please select an output folder!")
        else:
            index = 1
            for image_path in model["image_paths"]:

                static.set_image_data(image_path)
                self.rename.set_rename_data(index)
                # self.sg_sendIndex.emit(index)

                # Create image objects
                working_image = Image.open(image_path)
                watermark = Image.open(process["watermark_path"])

                original_image_width = working_image.width
                original_image_height = working_image.height

                # -----------------------------------
                # Dimensions of the image as seen in the image display (image_display.py)
                preview_image_width = process["current_image_width"]

                # Dimensions of the watermark as seen in the watermark custom label (watermark_label)
                preview_watermark_width = process["watermark_current_width"]
                preview_watermark_height = process["watermark_current_height"]

                # Watermark's position in watermark_label
                preview_watermark_posX = process["watermark_pos"][0]
                preview_watermark_posY = process["watermark_pos"][1]

                desired_image_width = original_image_width if not self.resize.le_width.text() else int(self.resize.le_width.text())
                desired_image_height = original_image_height if not self.resize.le_height.text() else int(self.resize.le_height.text())

                ratio = desired_image_width / preview_image_width

                watermark_new_width = round(ratio * preview_watermark_width)
                watermark_new_height = round(ratio * preview_watermark_height)

                watermark_new_positionX = round(ratio * preview_watermark_posX)
                watermark_new_positionY = round(ratio * preview_watermark_posY)

                working_image.thumbnail((desired_image_width, desired_image_height), Image.Resampling.NEAREST)
                watermark.thumbnail((watermark_new_width, watermark_new_height))

                if self.resize.chb_resize.isChecked():
                    if self.resize.rb_custom.isChecked():

                        if self.resize.chb_keep_ratio.isChecked():
                            desired_image_width, desired_image_height = static.keep_ratio(working_image.width, working_image.height,
                                                                      int(self.resize.le_width.text()),
                                                                      int(self.resize.le_height.text()))
                            working_image.resize((desired_image_width, desired_image_height), Image.Resampling.LANCZOS)
                        else:
                            working_image.resize((desired_image_width, desired_image_height), Image.Resampling.LANCZOS)
                    elif self.resize.rb_percent.isChecked():
                        desired_image_width, desired_image_height = static.reduce_by_percent(int(self.resize.le_percent.text()),
                                                                         working_image.width, working_image.height)
                        working_image.resize((desired_image_width, desired_image_height), Image.Resampling.LANCZOS)

                    elif self.resize.rb_predefined.isChecked():
                        desired_image_width, desired_image_width = static.predefined_size(self.resize.comb_presize.currentText())
                        working_image.resize((desired_image_width, desired_image_width), Image.Resampling.LANCZOS)

                    if self.rename.chb_add_count.isChecked():
                        path = model["output_folder"] + data["new_name"] + data["counter"] + data["extension"]
                        self.canvas_save(working_image, desired_image_width, desired_image_height, watermark,
                                         watermark_new_positionX, watermark_new_positionY, path)
                    else:
                        path = model["output_folder"] + data["base_name"] + data["extension"]
                        self.canvas_save(working_image, desired_image_width, desired_image_height, watermark,
                                         watermark_new_positionX, watermark_new_positionY, path)
                else:
                    if self.rename.chb_add_count.isChecked():
                        path = model["output_folder"] + data["new_name"] + data["counter"] + data["extension"]
                        self.canvas_save(working_image, desired_image_width, desired_image_height, watermark,
                                         watermark_new_positionX, watermark_new_positionY, path)
                    else:
                        path = model["output_folder"] + data["base_name"] + data["extension"]
                        self.canvas_save(working_image, desired_image_width, desired_image_height, watermark,
                                         watermark_new_positionX, watermark_new_positionY, path)

                index += 1

    def canvas_save(self, image, width, height, watermark, positionX, positionY, path):
        canvas = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        canvas.paste(
            image.convert("RGBA"))  # Convert to RGBA for compositing and paste into the canvas

        # Paste resized watermark and set position
        canvas.paste(watermark, (round(positionX), round(positionY)),
                     mask=watermark)
        canvas.save(path)

    def process_select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        model["output_folder"] = folder + "/"