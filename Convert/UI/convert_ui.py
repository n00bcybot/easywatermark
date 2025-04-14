# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convert_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_wg_convert(object):
    def setupUi(self, wg_convert):
        if not wg_convert.objectName():
            wg_convert.setObjectName(u"wg_convert")
        wg_convert.resize(200, 200)
        font = QFont()
        font.setPointSize(12)
        wg_convert.setFont(font)
        self.vl_convert = QVBoxLayout(wg_convert)
        self.vl_convert.setObjectName(u"vl_convert")
        self.cb_convert = QComboBox(wg_convert)
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.cb_convert.addItem("")
        self.cb_convert.setObjectName(u"cb_convert")
        self.cb_convert.setEditable(False)
        self.cb_convert.setMaxCount(10)

        self.vl_convert.addWidget(self.cb_convert)


        self.retranslateUi(wg_convert)

        QMetaObject.connectSlotsByName(wg_convert)
    # setupUi

    def retranslateUi(self, wg_convert):
        wg_convert.setWindowTitle(QCoreApplication.translate("wg_convert", u"Form", None))
        self.cb_convert.setItemText(0, QCoreApplication.translate("wg_convert", u"JPG", None))
        self.cb_convert.setItemText(1, QCoreApplication.translate("wg_convert", u"PNG", None))
        self.cb_convert.setItemText(2, QCoreApplication.translate("wg_convert", u"TIFF", None))

        self.cb_convert.setCurrentText(QCoreApplication.translate("wg_convert", u"JPG", None))
    # retranslateUi

