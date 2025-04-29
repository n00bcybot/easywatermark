# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_ui.ui'
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
    QLayout, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet(u"")
        self.action_add = QAction(MainWindow)
        self.action_add.setObjectName(u"action_add")
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        self.action_close = QAction(MainWindow)
        self.action_close.setObjectName(u"action_close")
        self.action_process = QAction(MainWindow)
        self.action_process.setObjectName(u"action_process")
        self.action_remove = QAction(MainWindow)
        self.action_remove.setObjectName(u"action_remove")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.sp_main = QSplitter(self.centralwidget)
        self.sp_main.setObjectName(u"sp_main")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sp_main.sizePolicy().hasHeightForWidth())
        self.sp_main.setSizePolicy(sizePolicy)
        self.sp_main.setOrientation(Qt.Orientation.Horizontal)
        self.sp_main.setChildrenCollapsible(False)
        self.sp_image_tools = QSplitter(self.sp_main)
        self.sp_image_tools.setObjectName(u"sp_image_tools")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sp_image_tools.sizePolicy().hasHeightForWidth())
        self.sp_image_tools.setSizePolicy(sizePolicy1)
        self.sp_image_tools.setMinimumSize(QSize(300, 0))
        self.sp_image_tools.setMaximumSize(QSize(16777215, 16777215))
        self.sp_image_tools.setBaseSize(QSize(0, 0))
        self.sp_image_tools.setOrientation(Qt.Orientation.Vertical)
        self.sp_image_tools.setChildrenCollapsible(False)
        self.layout_viewer = QFrame(self.sp_image_tools)
        self.layout_viewer.setObjectName(u"layout_viewer")
        self.layout_viewer.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_viewer.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.layout_viewer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sp_image_tools.addWidget(self.layout_viewer)
        self.layout_toolbox = QFrame(self.sp_image_tools)
        self.layout_toolbox.setObjectName(u"layout_toolbox")
        self.layout_toolbox.setMinimumSize(QSize(0, 0))
        self.layout_toolbox.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_toolbox.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.layout_toolbox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sp_image_tools.addWidget(self.layout_toolbox)
        self.sp_main.addWidget(self.sp_image_tools)
        self.layoutWidget = QWidget(self.sp_main)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.layout_display = QFrame(self.layoutWidget)
        self.layout_display.setObjectName(u"layout_display")
        self.layout_display.setMinimumSize(QSize(600, 400))
        self.layout_display.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_display.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.layout_display)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout.addWidget(self.layout_display)

        self.layout_flick = QFrame(self.layoutWidget)
        self.layout_flick.setObjectName(u"layout_flick")
        self.layout_flick.setMaximumSize(QSize(16777215, 80))
        self.layout_flick.setFrameShape(QFrame.Shape.StyledPanel)
        self.layout_flick.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.layout_flick)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addWidget(self.layout_flick)

        self.sp_main.addWidget(self.layoutWidget)

        self.gridLayout_4.addWidget(self.sp_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 33))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menuFIle.addAction(self.action_add)
        self.menuFIle.addAction(self.action_remove)
        self.menuFIle.addAction(self.action_clear)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.action_process)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.action_close)

        self.retranslateUi(MainWindow)
        self.action_close.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_add.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"Clear Image Browser", None))
        self.action_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.action_process.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.action_remove.setText(QCoreApplication.translate("MainWindow", u"Remove Image", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
    # retranslateUi

