import sys
from PySide6.QtWidgets import (QApplication, QWidget, QDialog, QMessageBox, QFileDialog)
from Process.UI.process_ui import Ui_process_dialog
from PySide6.QtCore import Signal, Slot
from PIL import Image
from model.model import *
from functions import static


class ProcessDialog(QDialog, Ui_process_dialog):

    sg_sendIndex = Signal(int)
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements


    def process_batch(self):
        if model["output_folder"] == "":
            QMessageBox.information(self, "Output Folder Not Selected", "Please select an output folder!")
        else:
            index = 1
            for image_path in model["image_path"]:

                static.set_image_data(image_path)
                self.sg_sendIndex.emit(index)

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
                        image_resized.save(
                            model["output_folder"] + data["new_name"] + data["counter"] + data["extension"])
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProcessDialog()
    window.show()
    app.exec()
