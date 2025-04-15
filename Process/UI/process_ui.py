# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'process_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_process_dialog(object):
    def setupUi(self, process_dialog):
        if not process_dialog.objectName():
            process_dialog.setObjectName(u"process_dialog")
        process_dialog.resize(571, 373)
        process_dialog.setMaximumSize(QSize(600, 400))
        self.layout_process = QGridLayout(process_dialog)
        self.layout_process.setObjectName(u"layout_process")
        self.layout_process.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.lb_select_folder = QLabel(process_dialog)
        self.lb_select_folder.setObjectName(u"lb_select_folder")

        self.layout_process.addWidget(self.lb_select_folder, 1, 0, 1, 1)

        self.pb_select_folder = QPushButton(process_dialog)
        self.pb_select_folder.setObjectName(u"pb_select_folder")

        self.layout_process.addWidget(self.pb_select_folder, 1, 1, 1, 1)

        self.progressBar = QProgressBar(process_dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.layout_process.addWidget(self.progressBar, 2, 0, 1, 1)

        self.pb_process = QPushButton(process_dialog)
        self.pb_process.setObjectName(u"pb_process")

        self.layout_process.addWidget(self.pb_process, 2, 1, 1, 1)

        self.lw_image_list = QListWidget(process_dialog)
        self.lw_image_list.setObjectName(u"lw_image_list")

        self.layout_process.addWidget(self.lw_image_list, 0, 0, 1, 2)


        self.retranslateUi(process_dialog)

        QMetaObject.connectSlotsByName(process_dialog)
    # setupUi

    def retranslateUi(self, process_dialog):
        process_dialog.setWindowTitle(QCoreApplication.translate("process_dialog", u"Process Images", None))
        self.lb_select_folder.setText(QCoreApplication.translate("process_dialog", u"Select Output Folder", None))
        self.pb_select_folder.setText(QCoreApplication.translate("process_dialog", u"Browse", None))
        self.pb_process.setText(QCoreApplication.translate("process_dialog", u"Process", None))
    # retranslateUi

