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
from PySide6.QtWidgets import (QApplication, QLayout, QSizePolicy, QToolBox,
    QVBoxLayout, QWidget)

class Ui_wg_toolbox(object):
    def setupUi(self, wg_toolbox):
        if not wg_toolbox.objectName():
            wg_toolbox.setObjectName(u"wg_toolbox")
        wg_toolbox.resize(302, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_toolbox.sizePolicy().hasHeightForWidth())
        wg_toolbox.setSizePolicy(sizePolicy)
        wg_toolbox.setMinimumSize(QSize(302, 450))
        wg_toolbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        wg_toolbox.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(wg_toolbox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(wg_toolbox)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(302, 450))
        self.toolBox.setStyleSheet(u"background-color: rgb(208, 255, 237);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setGeometry(QRect(0, 0, 302, 330))
        self.page_1.setMinimumSize(QSize(300, 0))
        self.toolBox.addItem(self.page_1, u"Watermark")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 302, 330))
        self.page_2.setMinimumSize(QSize(300, 200))
        self.toolBox.addItem(self.page_2, u"Resize")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMinimumSize(QSize(300, 200))
        self.toolBox.addItem(self.page_3, u"Rename")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setMinimumSize(QSize(300, 200))
        self.toolBox.addItem(self.page_4, u"Convert")

        self.verticalLayout.addWidget(self.toolBox)


        self.retranslateUi(wg_toolbox)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(wg_toolbox)
    # setupUi

    def retranslateUi(self, wg_toolbox):
        wg_toolbox.setWindowTitle(QCoreApplication.translate("wg_toolbox", u"Form", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), QCoreApplication.translate("wg_toolbox", u"Watermark", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("wg_toolbox", u"Resize", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("wg_toolbox", u"Rename", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("wg_toolbox", u"Convert", None))
    # retranslateUi

