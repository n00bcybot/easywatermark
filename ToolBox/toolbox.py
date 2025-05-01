import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QVBoxLayout, QListWidget,
                               QListWidgetItem, QPushButton, QFileDialog, QListView, QListWidgetItem, QListWidget,
                               QToolBox)

from ToolBox.UI.toolbox_ui import Ui_wg_toolbox
from Resize.resize import ResizeWidget
from Converter.converter import ConverterWidget
from Rename.rename import RenameWidget
from Watermark.watermark import Watermark


class ToolBoxWidget(QWidget, Ui_wg_toolbox, ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Load UI elements

        self.page_2.setHidden(True)
        self.page_3.setHidden(True)
        self.page_4.setHidden(True)

        # Import Watermark widget
        # --------------------------------------------------------------------------------------------------
        self.watermark = Watermark()
        self.page_1.layout().addWidget(self.watermark)

        self.watermark.fr_container.setDisabled(True)
        self.watermark.fr_browse.setDisabled(True)
        self.watermark.fr_combo.setDisabled(True)
        self.watermark.lb_enter_text.setDisabled(True)
        self.watermark.le_text.setDisabled(True)


        # Import Resize widget
        # --------------------------------------------------------------------------------------------------
        self.resize_widget = ResizeWidget()
        self.page_2.layout().addWidget(self.resize_widget)

        self.resize_widget.fr_container.setDisabled(True)
        self.resize_widget.fr_custom_size.setDisabled(True)
        self.resize_widget.fr_percent.setDisabled(True)
        self.resize_widget.fr_predefined.setDisabled(True)

        # Import Converter widget
        # --------------------------------------------------------------------------------------------------
        self.convert_widget = ConverterWidget()
        self.page_4.layout().addWidget(self.convert_widget)

        # Import Rename widget
        # --------------------------------------------------------------------------------------------------
        self.rename_widget = RenameWidget()
        self.page_3.layout().addWidget(self.rename_widget)

        self.rename_widget.fr_container.setDisabled(True)
        self.rename_widget.fr_keep_name.setDisabled(True)
        self.rename_widget.fr_new_name.setDisabled(True)
        self.rename_widget.comb_digit.setDisabled(True)
        self.rename_widget.le_remove_string.setDisabled(True)
        self.rename_widget.le_remove_first.setDisabled(True)
        self.rename_widget.le_remove_last.setDisabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToolBoxWidget()
    window.show()
    app.exec()
