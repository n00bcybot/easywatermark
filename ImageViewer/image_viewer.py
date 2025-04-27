import sys
from PySide6.QtWidgets import (QApplication, QWidget, QFileDialog, QListWidgetItem)
from PySide6.QtCore import Qt, Signal, Slot, QSize
from model.model import *
from ImageViewer.UI.image_viewer_ui import Ui_wg_image_viewer


class ImageViewer(QWidget, Ui_wg_image_viewer):
    sg_item_clicked = Signal(QListWidgetItem)

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.list_viewer.itemClicked.connect(self.display_clicked_item)


    def add_image(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Images", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)"
        )

        items = []
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
            items.append(item)
        # Select the first item in the list
        items[0].setSelected(True)
        for i in items:
            if i not in model["list_viewer_items"]:
                model["list_viewer_items"].append(i)
            else:
                model["list_viewer_items"] = items



    def clear_image_picker(self):
        self.list_viewer.clear()  # Clear image viewer
        model["image_path"].clear()  # Clear the paths list as well
        model["list_viewer_items"].clear()

    @Slot()
    def display_clicked_item(self):
        items = [self.list_viewer.item(i) for i in range(self.list_viewer.count())]
        for i in items:
            if i.isSelected():
                self.sg_item_clicked.emit(i)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ImageViewer()
#     window.show()
#     app.exec()
