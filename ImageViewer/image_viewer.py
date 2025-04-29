from PySide6.QtWidgets import (QWidget, QListWidgetItem)
from PySide6.QtCore import Signal, Slot
from model.model import *
from ImageViewer.UI.image_viewer_ui import Ui_wg_image_viewer


class ImageViewer(QWidget, Ui_wg_image_viewer):
    sg_selected_item = Signal(QListWidgetItem)
    sg_rebuild_viewer = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.list_viewer.itemClicked.connect(self.display_clicked_item)

    def clear_list_viewer(self):
        model["image_paths"].clear()  # Clear the paths list as well
        model["list_viewer_items"].clear()
        self.list_viewer.clear()

        # def remove_item(self):
        #
        #     for item in model["list_viewer_items"]:
        #         if item.isSelected():
        #             path = model["image_paths"][model["list_viewer_items"].index(item)]
        #             model["image_paths"].remove(path)  # Clear the paths list as well
        #             model["list_viewer_items"].remove(item)

        self.sg_rebuild_viewer.emit()

    def display_clicked_item(self):
        # model["list_viewer_items"] = [self.list_viewer.item(i) for i in range(self.list_viewer.count())]
        for item in model["list_viewer_items"]:
            if item.isSelected():
                self.sg_selected_item.emit(item)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = ImageViewer()
#     window.show()
#     app.exec()
