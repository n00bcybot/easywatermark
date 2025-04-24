# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageViewer_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1207, 672)
        MainWindow.setStyleSheet(u"")
        self.act_AddImage = QAction(MainWindow)
        self.act_AddImage.setObjectName(u"act_AddImage")
        self.act_Close = QAction(MainWindow)
        self.act_Close.setObjectName(u"act_Close")
        self.act_Clear = QAction(MainWindow)
        self.act_Clear.setObjectName(u"act_Clear")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fr_ImagePicker = QFrame(self.centralwidget)
        self.fr_ImagePicker.setObjectName(u"fr_ImagePicker")
        self.fr_ImagePicker.setMaximumSize(QSize(280, 16777215))
        self.fr_ImagePicker.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_ImagePicker.setFrameShadow(QFrame.Shadow.Plain)
        self.fr_ImagePicker.setLineWidth(5)
        self.layout_Image = QVBoxLayout(self.fr_ImagePicker)
        self.layout_Image.setObjectName(u"layout_Image")
        self.layout_Image.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.fr_ImagePicker)

        self.lb_ImageDisplay = QLabel(self.centralwidget)
        self.lb_ImageDisplay.setObjectName(u"lb_ImageDisplay")
        self.lb_ImageDisplay.setFrameShape(QFrame.Shape.NoFrame)
        self.lb_ImageDisplay.setFrameShadow(QFrame.Shadow.Plain)
        self.lb_ImageDisplay.setLineWidth(0)

        self.horizontalLayout.addWidget(self.lb_ImageDisplay)

        MainWindow.setCentralWidget(self.centralwidget)
        self.mb_main = QMenuBar(MainWindow)
        self.mb_main.setObjectName(u"mb_main")
        self.mb_main.setGeometry(QRect(0, 0, 1207, 33))
        self.mn_File = QMenu(self.mb_main)
        self.mn_File.setObjectName(u"mn_File")
        MainWindow.setMenuBar(self.mb_main)
        self.sb_MainWindow = QStatusBar(MainWindow)
        self.sb_MainWindow.setObjectName(u"sb_MainWindow")
        self.sb_MainWindow.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.sb_MainWindow)

        self.mb_main.addAction(self.mn_File.menuAction())
        self.mn_File.addAction(self.act_AddImage)
        self.mn_File.addSeparator()
        self.mn_File.addAction(self.act_Clear)
        self.mn_File.addSeparator()
        self.mn_File.addAction(self.act_Close)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.act_AddImage.setText(QCoreApplication.translate("MainWindow", u"Add Images", None))
        self.act_Close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.act_Clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lb_ImageDisplay.setText("")
        self.mn_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

