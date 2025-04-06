import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget
                               )
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import QSize, Qt

from ImageViewer.UI.ImageViewer_ui import Ui_MainWindow


class ImageWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.thumbnail_size = QSize(100, 100)

        # Close the window
        self.act_Close.triggered.connect(self.close)

        # Clear the image picker
        self.act_Clear.triggered.connect(self.clear_image_picker)

        # Add images to the file picker
        self.act_AddImage.triggered.connect(self.add_images)

        self.list_widget = QListWidget()
        self.list_widget.setIconSize(self.thumbnail_size)

        # This makes the items display in rows, wrapping as needed
        self.list_widget.setViewMode(QListWidget.IconMode)
        self.list_widget.setResizeMode(QListWidget.Adjust)
        self.list_widget.setMovement(QListWidget.Static)
        self.list_widget.setSpacing(10)
        self.list_widget.itemClicked.connect(self.show_image_path)

        self.layout_Image.addWidget(self.list_widget)

    def add_images(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Images", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )

        for file in files:
            # Create pixmap from image
            pixmap = QPixmap(file)

            # Create list item and add the pixmap to it
            item = QListWidgetItem(pixmap, "")

            # Store filepath as user data
            item.setData(Qt.UserRole, file)
            self.list_widget.addItem(item)

    def clear_image_picker(self):
        self.list_widget.clear()

    def show_image_path(self, item):
        # Retrieve user data, previously acquired in add_images
        image_path = item.data(Qt.UserRole)
        self.sb_MainWindow.showMessage(image_path)

        # Create pixmap to display image in the main window
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(QSize(self.lb_ImageDisplay.size()), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.lb_ImageDisplay.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageWindow()
    window.show()
    app.exec()
