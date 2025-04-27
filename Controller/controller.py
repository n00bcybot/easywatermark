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

    def add_images(self):
        # Add images
        self.image_viewer.add_image()

        self.current_path = model["image_path"][0]
        model["current_image_path"] = self.current_path

        self.main_window.statusbar.showMessage(model["image_path"][0])
        # Display the first image in the list upon adding the images
        scaled_pixmap = static.scale_pixmap(self.image_display.lb_display.size(), model["pixmap_original"][0])
        self.image_display.lb_display.setPixmap(scaled_pixmap)

    def display_image(self):

        for path, pixmap in zip(model["image_path"], model["pixmap_original"]):
            if path == self.current_path:
                # Scale to label size
                scaled_pixmap = static.scale_pixmap(self.image_display.lb_display.size(), pixmap)
                self.image_display.lb_display.setPixmap(scaled_pixmap)
                self.main_window.statusbar.showMessage(path)
                model["current_image_path"] = path

    def show_next_image(self):
        if int(model["image_path"].index(self.current_path)) < len(model["image_path"]) - 1:
            self.current_path = model["image_path"][model["image_path"].index(self.current_path) + 1]
        else:
            self.current_path = model["image_path"][0]

        self.display_image()

    def show_previous_image(self):
        if int(model["image_path"].index(self.current_path)) > 0:
            self.current_path = model["image_path"][model["image_path"].index(self.current_path) - 1]
        else:
            self.current_path = model["image_path"][len(model["image_path"]) - 1]

        self.display_image()
