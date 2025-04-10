# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSplitter, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 754)
        self.action_add = QAction(MainWindow)
        self.action_add.setObjectName(u"action_add")
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        self.action_close = QAction(MainWindow)
        self.action_close.setObjectName(u"action_close")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layout_main = QGridLayout(self.centralwidget)
        self.layout_main.setObjectName(u"layout_main")
        self.splitter_main = QSplitter(self.centralwidget)
        self.splitter_main.setObjectName(u"splitter_main")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_main.sizePolicy().hasHeightForWidth())
        self.splitter_main.setSizePolicy(sizePolicy)
        self.splitter_main.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_main.setChildrenCollapsible(True)
        self.sp_images_tools = QSplitter(self.splitter_main)
        self.sp_images_tools.setObjectName(u"sp_images_tools")
        self.sp_images_tools.setMinimumSize(QSize(150, 320))
        self.sp_images_tools.setMaximumSize(QSize(300, 954))
        self.sp_images_tools.setOrientation(Qt.Orientation.Vertical)
        self.sp_images_tools.setChildrenCollapsible(False)
        self.layout_image_viewer = QFrame(self.sp_images_tools)
        self.layout_image_viewer.setObjectName(u"layout_image_viewer")
        self.layout_image_viewer.setMinimumSize(QSize(150, 150))
        self.layout_image_viewer.setMaximumSize(QSize(300, 500))
        self.layout_image_viewer.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_image_viewer.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.layout_image_viewer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.wg_ph_imageviewer = QWidget(self.layout_image_viewer)
        self.wg_ph_imageviewer.setObjectName(u"wg_ph_imageviewer")
        self.wg_ph_imageviewer.setMinimumSize(QSize(150, 150))
        self.wg_ph_imageviewer.setMaximumSize(QSize(300, 16777215))
        self.wg_ph_imageviewer.setStyleSheet(u"background-color: rgb(137, 220, 255);")

        self.gridLayout.addWidget(self.wg_ph_imageviewer, 0, 0, 1, 1)

        self.sp_images_tools.addWidget(self.layout_image_viewer)
        self.layout_toolbox = QFrame(self.sp_images_tools)
        self.layout_toolbox.setObjectName(u"layout_toolbox")
        self.layout_toolbox.setMinimumSize(QSize(300, 320))
        self.layout_toolbox.setMaximumSize(QSize(300, 449))
        self.layout_toolbox.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_toolbox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.layout_toolbox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.wg_ph_toolbox = QWidget(self.layout_toolbox)
        self.wg_ph_toolbox.setObjectName(u"wg_ph_toolbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.wg_ph_toolbox.sizePolicy().hasHeightForWidth())
        self.wg_ph_toolbox.setSizePolicy(sizePolicy1)
        self.wg_ph_toolbox.setMinimumSize(QSize(300, 320))
        self.wg_ph_toolbox.setMaximumSize(QSize(16777215, 16777215))
        self.wg_ph_toolbox.setStyleSheet(u"background-color: rgb(253, 185, 255);")

        self.verticalLayout.addWidget(self.wg_ph_toolbox)

        self.sp_images_tools.addWidget(self.layout_toolbox)
        self.splitter_main.addWidget(self.sp_images_tools)
        self.layout_display_flick = QFrame(self.splitter_main)
        self.layout_display_flick.setObjectName(u"layout_display_flick")
        self.layout_display_flick.setMinimumSize(QSize(400, 300))
        self.layout_display_flick.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_display_flick.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.layout_display_flick)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layout_image_display = QFrame(self.layout_display_flick)
        self.layout_image_display.setObjectName(u"layout_image_display")
        self.layout_image_display.setMinimumSize(QSize(400, 300))
        self.layout_image_display.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_image_display.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.layout_image_display)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.wg_ph_image_display = QWidget(self.layout_image_display)
        self.wg_ph_image_display.setObjectName(u"wg_ph_image_display")
        self.wg_ph_image_display.setMinimumSize(QSize(400, 300))
        self.wg_ph_image_display.setStyleSheet(u"background-color: rgb(240, 255, 199);")

        self.gridLayout_2.addWidget(self.wg_ph_image_display, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.layout_image_display)

        self.layout_flick = QFrame(self.layout_display_flick)
        self.layout_flick.setObjectName(u"layout_flick")
        self.layout_flick.setMinimumSize(QSize(400, 80))
        self.layout_flick.setMaximumSize(QSize(16777215, 100))
        self.layout_flick.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_flick.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.layout_flick)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.wg_ph_flick = QWidget(self.layout_flick)
        self.wg_ph_flick.setObjectName(u"wg_ph_flick")
        self.wg_ph_flick.setMinimumSize(QSize(0, 80))
        self.wg_ph_flick.setMaximumSize(QSize(16777215, 100))
        self.wg_ph_flick.setStyleSheet(u"background-color: rgb(206, 255, 185);")

        self.horizontalLayout.addWidget(self.wg_ph_flick)


        self.verticalLayout_2.addWidget(self.layout_flick)

        self.splitter_main.addWidget(self.layout_display_flick)

        self.layout_main.addWidget(self.splitter_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menuFIle.addAction(self.action_add)
        self.menuFIle.addAction(self.action_clear)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.action_close)

        self.retranslateUi(MainWindow)
        self.action_close.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_add.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"Clear Image", None))
        self.action_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
    # retranslateUi

