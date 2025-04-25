# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watermark_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_wg_watermark(object):
    def setupUi(self, wg_watermark):
        if not wg_watermark.objectName():
            wg_watermark.setObjectName(u"wg_watermark")
        wg_watermark.resize(300, 368)
        wg_watermark.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(wg_watermark)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(wg_watermark)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(wg_watermark)

        QMetaObject.connectSlotsByName(wg_watermark)
    # setupUi

    def retranslateUi(self, wg_watermark):
        wg_watermark.setWindowTitle(QCoreApplication.translate("wg_watermark", u"WatermarkWidget", None))
        self.label.setText(QCoreApplication.translate("wg_watermark", u"Hello", None))
    # retranslateUi

