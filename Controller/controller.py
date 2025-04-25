from PySide6.QtCore import QObject, Slot, Signal, QSize
from model.model import *


class Controller(QObject):

    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window  # Import MainWindow
        self.converter = self.main_window.toolbox.convert_widget  # Import any other widget
        self.image_viewer = self.main_window.image_viewer
        self.image_display = self.main_window.image_display

        # Connect the signal from Converter to redirecting slot
        self.converter.indexChanged.connect(self.receive_converter_indexChanged)
        self.main_window.signal_add_images.connect(self.receive_add_images)
        self.image_viewer.signal_set_statusbar.connect(self.receive_status_bar)
        self.image_viewer.signal_display_pixmap.connect(self.receive_display_pixmap)


    def get_image_display_size(self):
        model["initial_label_display_size"] = self.image_display.label_image_display.size()

    # Redirect indexChanged signal to update MainWindow status bar
    @Slot(str)
    def receive_converter_indexChanged(self, message):
        data["extension"] = message  # Update model
        self.main_window.statusbar.showMessage(message)  # Set statusbar message

    @Slot()
    def receive_add_images(self):
        self.image_viewer.add_image()

    @Slot(str)
    def receive_status_bar(self, message):
        self.main_window.statusbar.showMessage(message)

    @Slot(QPixmap)
    def receive_display_pixmap(self, pixmap):
        self.image_display.label_image_display.setPixmap(pixmap)


