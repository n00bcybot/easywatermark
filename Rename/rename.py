import sys
import os
from PySide6.QtWidgets import (QApplication, QWidget, )
from PySide6.QtCore import Signal, Slot
from model.model import *
from functions import static

from Rename.UI.rename_ui import Ui_Rename


class RenameWidget(QWidget, Ui_Rename):

    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.extension = ""

        self.chb_rename.checkStateChanged.connect(self.run_rename)
        self.chb_add_count.checkStateChanged.connect(self.set_dynamic_preview)
        self.rb_change.clicked.connect(self.set_dynamic_preview)
        self.rb_keep.clicked.connect(self.set_dynamic_preview)
        self.le_new_name.textChanged.connect(self.set_dynamic_preview)
        self.le_add_prefix.textChanged.connect(self.set_dynamic_preview)
        self.le_add_suffix.textChanged.connect(self.set_dynamic_preview)
        self.le_remove_string.textChanged.connect(self.set_dynamic_preview)
        self.le_remove_first.textChanged.connect(self.set_dynamic_preview)
        self.le_remove_last.textChanged.connect(self.set_dynamic_preview)

        self.comb_digit.textActivated.connect(self.set_dynamic_preview)
        self.comb_digit.textActivated.connect(static.get_digit(self.comb_digit.currentText))
        self.comb_delimiter.textActivated.connect(self.set_dynamic_preview)
        self.comb_delimiter.textActivated.connect(static.set_delimiter)

    def set_rename_data(self, index):

        data["replace_name"] = self.le_new_name.text()
        data["remove_string"] = self.le_remove_string.text()
        data["remove_first"] = self.le_remove_first.text()
        data["remove_last"] = self.le_remove_last.text()
        data["prefix"] = self.le_add_prefix.text()
        data["suffix"] = self.le_add_suffix.text()
        count = static.get_digit(self.comb_digit.currentText())
        data["counter"] = f"{index:0{count}}"
        data["delimiter"] = static.set_delimiter(self.comb_delimiter.currentText())
        selected_format = self.extension
        data["extension"] = static.image_format(selected_format)

    def set_preview(self):
        static.set_image_data(model["image_paths"][0])
        result = ("/" + data["prefix"] + data["replace_name"] + data["base_name"] + data["suffix"] +
                  data["counter"] + data["extension"])
        self.lb_preview.setText(result)

    def set_dynamic_preview(self):
        self.set_rename_data(index=1)
        if not self.chb_add_count.isChecked():
            data["counter"] = ""

        vars_list = []
        dm = data["delimiter"]

        if self.rb_keep.isChecked():
            data["new_name"] = data["base_name"]
            if self.rb_remove_string.isChecked():
                data["new_name"] = static.remove_string(data["base_name"], str(self.le_remove_string.text()))
            elif self.rb_remove_first.isChecked():
                data["new_name"] = static.remove_first(data["base_name"], self.le_remove_first.text())
            elif self.rb_remove_last.isChecked():
                data["new_name"] = static.remove_last(data["base_name"], self.le_remove_last.text())

            if data["new_name"] == "":
                vars_list = [data["prefix"], data["base_name"], data["suffix"], data["counter"]]
            else:
                vars_list = [data["prefix"], data["new_name"], data["suffix"], data["counter"]]

        elif self.rb_change.isChecked():
            vars_list = [data["prefix"], data["replace_name"], data["suffix"], data["counter"]]

        variable = [var for var in vars_list if var]
        new_name = "/" + dm.join(variable) + data["extension"]

        print(vars_list)

        self.lb_preview.setText(new_name)

        # Set the new name for later use in processing
        new_list = [var for var in vars_list if var != data["counter"]]
        data["new_name"] = dm.join(new_list)

    def run_rename(self):
        self.chb_rename.clicked.connect(self.set_preview)

    def receive_extension(self, text):
        self.extension = text
        # Prints empty list (?)
        self.set_dynamic_preview()






#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = RenameWidget()
#     window.show()
#     app.exec()
