# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_viewer_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QLayout, QListView, QListWidget,
    QListWidgetItem, QSizePolicy, QWidget)

class Ui_wg_image_viewer(object):
    def setupUi(self, wg_image_viewer):
        if not wg_image_viewer.objectName():
            wg_image_viewer.setObjectName(u"wg_image_viewer")
        wg_image_viewer.resize(300, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_image_viewer.sizePolicy().hasHeightForWidth())
        wg_image_viewer.setSizePolicy(sizePolicy)
        wg_image_viewer.setMinimumSize(QSize(0, 200))
        self.gridLayout = QGridLayout(wg_image_viewer)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.list_viewer = QListWidget(wg_image_viewer)
        self.list_viewer.setObjectName(u"list_viewer")
        self.list_viewer.setMinimumSize(QSize(150, 350))
        self.list_viewer.setBaseSize(QSize(0, 0))
        self.list_viewer.setStyleSheet(u"")
        self.list_viewer.setFrameShape(QFrame.Shape.NoFrame)
        self.list_viewer.setFrameShadow(QFrame.Shadow.Plain)
        self.list_viewer.setLineWidth(0)
        self.list_viewer.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.list_viewer.setAutoScrollMargin(16)
        self.list_viewer.setDragEnabled(True)
        self.list_viewer.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.list_viewer.setIconSize(QSize(96, 72))
        self.list_viewer.setMovement(QListView.Movement.Static)
        self.list_viewer.setProperty(u"isWrapping", True)
        self.list_viewer.setResizeMode(QListView.ResizeMode.Adjust)
        self.list_viewer.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.list_viewer.setSpacing(5)
        self.list_viewer.setGridSize(QSize(108, 77))
        self.list_viewer.setViewMode(QListView.ViewMode.IconMode)
        self.list_viewer.setUniformItemSizes(True)
        self.list_viewer.setBatchSize(500)
        self.list_viewer.setWordWrap(True)
        self.list_viewer.setSelectionRectVisible(False)
        self.list_viewer.setItemAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.list_viewer, 0, 0, 1, 1)


        self.retranslateUi(wg_image_viewer)

        QMetaObject.connectSlotsByName(wg_image_viewer)
    # setupUi

    def retranslateUi(self, wg_image_viewer):
        wg_image_viewer.setWindowTitle(QCoreApplication.translate("wg_image_viewer", u"Form", None))
    # retranslateUi

