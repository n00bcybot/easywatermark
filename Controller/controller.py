from PySide6.QtWidgets import QFileDialog, QMessageBox, QWidget
from PySide6.QtCore import QObject, Slot, Signal, QSize
from PySide6.QtGui import Qt
from PIL import Image
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

    def receive_watermark_path(self, path):
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
            QMessageBox.information(self, "Output Folder Not Selected", "Please select an output folder!")
        else:
            index = 1
            for image_path in model["image_paths"]:

                static.set_image_data(image_path)
                self.rename.set_rename_data(index)
                # self.sg_sendIndex.emit(index)

                # Create image object
                image = Image.open(image_path)
                image_resized = None

                if self.resize.chb_resize.isChecked():
                    if self.resize.rb_custom.isChecked():
                        width = int(self.resize.le_width.text())
                        height = int(self.resize.le_height.text())
                        if self.resize.chb_keep_ratio.isChecked():
                            new_width, new_height = static.keep_ratio(image.width, image.height,
                                                                      int(self.resize.le_width.text()),
                                                                      int(self.resize.le_height.text()))
                            image_resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        else:
                            image_resized = image.resize((width, height), Image.Resampling.LANCZOS)
                    elif self.resize.rb_percent.isChecked():
                        new_width, new_height = static.reduce_by_percent(int(self.resize.le_percent.text()),
                                                                         image.width, image.height)
                        image_resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                    elif self.resize.rb_predefined.isChecked():
                        width, height = static.predefined_size(self.resize.comb_presize.currentText())
                        image_resized = image.resize((width, height), Image.Resampling.LANCZOS)

                    if self.rename.chb_add_count.isChecked():
                        image_resized.save(
                            model["output_folder"] + data["new_name"] + data["counter"] + data["extension"])
                    else:
                        image_resized.save(model["output_folder"] + data["base_name"] + data["extension"])
                else:
                    if self.rename.chb_add_count.isChecked():
                        image.save(model["output_folder"] + data["new_name"] + data["counter"] + data["extension"])
                    else:
                        image.save(model["output_folder"] + data["base_name"] + data["extension"])

                index += 1

    def process_select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        model["output_folder"] = folder + "/"
