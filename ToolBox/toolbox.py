import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget,
                               QToolBox)

from ToolBox.UI.toolbox_ui import Ui_wg_toolbox
from Resize.resize import ResizeWidget
from Convert.convert import ConvertWidget
from Rename.rename import RenameWidget


class ToolBoxWidget(QWidget, Ui_wg_toolbox, ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements


        self.page_2.setHidden(True)
        self.page_3.setHidden(True)
        self.page_4.setHidden(True)

        # Import Resize widget
        # --------------------------------------------------------------------------------------------------
        self.resize_widget = ResizeWidget()
        self.page_2.layout().addWidget(self.resize_widget)
        self.resize_widget.fr_container.setDisabled(True)


        # Import Convert widget
        # --------------------------------------------------------------------------------------------------
        self.convert_widget = ConvertWidget()
        self.page_4.layout().addWidget(self.convert_widget)

        # Import Rename widget
        # --------------------------------------------------------------------------------------------------
        self.rename_widget = RenameWidget()
        self.page_3.layout().addWidget(self.rename_widget)
        self.rename_widget.fr_container.setDisabled(True)
        self.rename_widget.fr_keep_name.setDisabled(True)
        self.rename_widget.fr_new_name.setDisabled(True)
        self.rename_widget.comb_digit.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToolBoxWidget()
    window.show()
    app.exec()
