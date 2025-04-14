# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_dsplay_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_layout_image_display(object):
    def setupUi(self, layout_image_display):
        if not layout_image_display.objectName():
            layout_image_display.setObjectName(u"layout_image_display")
        layout_image_display.resize(1000, 600)
        self.gridLayout = QGridLayout(layout_image_display)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_image_display = QLabel(layout_image_display)
        self.label_image_display.setObjectName(u"label_image_display")
        self.label_image_display.setStyleSheet(u"")
        self.label_image_display.setScaledContents(False)
        self.label_image_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_image_display, 0, 0, 1, 1)


        self.retranslateUi(layout_image_display)

        QMetaObject.connectSlotsByName(layout_image_display)
    # setupUi

    def retranslateUi(self, layout_image_display):
        layout_image_display.setWindowTitle(QCoreApplication.translate("layout_image_display", u"Form", None))
        self.label_image_display.setText("")
    # retranslateUi

