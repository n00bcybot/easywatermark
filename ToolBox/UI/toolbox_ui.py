# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toolbox_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QSizePolicy,
    QToolBox, QWidget)

class Ui_wg_toolbox(object):
    def setupUi(self, wg_toolbox):
        if not wg_toolbox.objectName():
            wg_toolbox.setObjectName(u"wg_toolbox")
        wg_toolbox.resize(300, 300)
        wg_toolbox.setMinimumSize(QSize(0, 300))
        self.gridLayout = QGridLayout(wg_toolbox)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(wg_toolbox)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(300, 300))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setGeometry(QRect(0, 0, 300, 180))
        self.layout_watermark = QGridLayout(self.page_1)
        self.layout_watermark.setObjectName(u"layout_watermark")
        self.toolBox.addItem(self.page_1, u"Watermark")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 300, 180))
        self.layout_resize = QGridLayout(self.page_2)
        self.layout_resize.setObjectName(u"layout_resize")
        self.toolBox.addItem(self.page_2, u"Resize")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 300, 180))
        self.layout_rename = QGridLayout(self.page_3)
        self.layout_rename.setObjectName(u"layout_rename")
        self.toolBox.addItem(self.page_3, u"Rename")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 300, 180))
        self.layout_saveas = QGridLayout(self.page_4)
        self.layout_saveas.setObjectName(u"layout_saveas")
        self.toolBox.addItem(self.page_4, u"Save As")

        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)


        self.retranslateUi(wg_toolbox)

        self.toolBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(wg_toolbox)
    # setupUi

    def retranslateUi(self, wg_toolbox):
        wg_toolbox.setWindowTitle(QCoreApplication.translate("wg_toolbox", u"Form", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), QCoreApplication.translate("wg_toolbox", u"Watermark", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("wg_toolbox", u"Resize", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("wg_toolbox", u"Rename", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("wg_toolbox", u"Save As", None))
    # retranslateUi

