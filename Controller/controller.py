from PySide6.QtCore import QObject, Slot, Signal, QSize
from PySide6.QtGui import Qt
from model.model import *
from functions import static


class Controller(QObject):

    def __init__(self, main_window):
        super().__init__()

        self.current_path = ""

        self.main_window = main_window  # Import MainWindow
        self.converter = self.main_window.toolbox.convert_widget  # Import any other widget
        self.image_viewer = self.main_window.image_viewer
        self.image_display = self.main_window.image_display
        self.flicker = self.main_window.image_flicker

        self.main_window.action_add.triggered.connect(self.add_images)
        self.main_window.action_clear.triggered.connect(self.image_viewer.clear_image_picker)

        self.flicker.bt_next.clicked.connect(self.show_next_image)
        self.flicker.bt_previous.clicked.connect(self.show_previous_image)

        self.image_viewer.list_viewer.itemClicked.connect(self.on_item_clicked)

    @Slot(int)
    def on_item_clicked(self, item):
        index = model["list_viewer_items"].index(item)
        path = model["image_path"][index]

        self.display_image(path)

    def add_images(self):
        # Add images
        self.image_viewer.add_image()

        self.current_path = model["image_path"][0]
        model["current_image_path"] = self.current_path

        self.main_window.statusbar.showMessage(model["image_path"][0])
        # Display the first image in the list upon adding the images
        scaled_pixmap = static.scale_pixmap(self.image_display.lb_display.size(), model["pixmap_original"][0])
        self.image_display.lb_display.setPixmap(scaled_pixmap)

    # def display_image(self):
    #
    #     for path, pixmap in zip(model["image_path"], model["pixmap_original"]):
    #         if path == self.current_path:
    #             # Scale to label size
    #             scaled_pixmap = static.scale_pixmap(self.image_display.lb_display.size(), pixmap)
    #             self.image_display.lb_display.setPixmap(scaled_pixmap)
    #             self.main_window.statusbar.showMessage(path)
    #             model["current_image_path"] = path

    def display_image(self, path):

        if path in model["image_path"]:
            pixmap = model["pixmap_original"][model["image_path"].index(path)]
            scaled_pixmap = static.scale_pixmap(self.image_display.lb_display.size(), pixmap)
            self.image_display.lb_display.setPixmap(scaled_pixmap)
            self.main_window.statusbar.showMessage(path)
            model["current_image_path"] = path

    def show_next_image(self):
        current_list = model["image_path"]
        if int(current_list.index(self.current_path)) < len(current_list) - 1:
            self.current_path = current_list[current_list.index(self.current_path) + 1]
            model["list_viewer_items"][current_list.index(self.current_path)].setSelected(True)
        else:
            self.current_path = current_list[0]

        self.display_image(self.current_path)

    def show_previous_image(self):
        current_list = model["image_path"]
        if int(current_list.index(self.current_path)) > 0:
            self.current_path = current_list[current_list.index(self.current_path) - 1]
            model["list_viewer_items"][current_list.index(self.current_path)].setSelected(True)
        else:
            self.current_path = current_list[len(current_list) - 1]

        self.display_image(self.current_path)
