# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        self.main_layout = QWidget(MainWindow)
        self.main_layout.setObjectName(u"main_layout")
        self.main_window_layout = QHBoxLayout(self.main_layout)
        self.main_window_layout.setObjectName(u"main_window_layout")
        self.gb_browser = QGroupBox(self.main_layout)
        self.gb_browser.setObjectName(u"gb_browser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_browser.sizePolicy().hasHeightForWidth())
        self.gb_browser.setSizePolicy(sizePolicy)
        self.gb_browser.setMaximumSize(QSize(400, 600))
        self.gb_layout = QHBoxLayout(self.gb_browser)
        self.gb_layout.setObjectName(u"gb_layout")
        self.gb_layout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)

        self.main_window_layout.addWidget(self.gb_browser)

        self.lb_display = QLabel(self.main_layout)
        self.lb_display.setObjectName(u"lb_display")
        sizePolicy.setHeightForWidth(self.lb_display.sizePolicy().hasHeightForWidth())
        self.lb_display.setSizePolicy(sizePolicy)

        self.main_window_layout.addWidget(self.lb_display)

        MainWindow.setCentralWidget(self.main_layout)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_quit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.gb_browser.setTitle(QCoreApplication.translate("MainWindow", u"Browse Image", None))
        self.lb_display.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

