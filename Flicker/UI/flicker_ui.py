# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flicker_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_wg_flicker(object):
    def setupUi(self, wg_flicker):
        if not wg_flicker.objectName():
            wg_flicker.setObjectName(u"wg_flicker")
        wg_flicker.resize(1209, 80)
        self.horizontalLayout = QHBoxLayout(wg_flicker)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_previous = QPushButton(wg_flicker)
        self.bt_previous.setObjectName(u"bt_previous")
        self.bt_previous.setMinimumSize(QSize(90, 40))
        font = QFont()
        font.setPointSize(11)
        self.bt_previous.setFont(font)

        self.horizontalLayout.addWidget(self.bt_previous)

        self.bt_next = QPushButton(wg_flicker)
        self.bt_next.setObjectName(u"bt_next")
        self.bt_next.setMinimumSize(QSize(90, 40))
        self.bt_next.setFont(font)

        self.horizontalLayout.addWidget(self.bt_next)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(wg_flicker)

        QMetaObject.connectSlotsByName(wg_flicker)
    # setupUi

    def retranslateUi(self, wg_flicker):
        wg_flicker.setWindowTitle(QCoreApplication.translate("wg_flicker", u"Form", None))
        self.bt_previous.setText(QCoreApplication.translate("wg_flicker", u"Previous", None))
        self.bt_next.setText(QCoreApplication.translate("wg_flicker", u"Next", None))
    # retranslateUi

