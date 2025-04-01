# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browser_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
    QLabel, QSizePolicy, QTreeView, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(200, 800)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tv_browser = QTreeView(Dialog)
        self.tv_browser.setObjectName(u"tv_browser")
        font = QFont()
        font.setPointSize(12)
        self.tv_browser.setFont(font)
        self.tv_browser.setFrameShape(QFrame.Shape.StyledPanel)

        self.verticalLayout.addWidget(self.tv_browser)

        self.lb_browser = QLabel(Dialog)
        self.lb_browser.setObjectName(u"lb_browser")

        self.verticalLayout.addWidget(self.lb_browser)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lb_browser.setText("")
    # retranslateUi

