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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_wg_toolbox(object):
    def setupUi(self, wg_toolbox):
        if not wg_toolbox.objectName():
            wg_toolbox.setObjectName(u"wg_toolbox")
        wg_toolbox.resize(300, 420)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_toolbox.sizePolicy().hasHeightForWidth())
        wg_toolbox.setSizePolicy(sizePolicy)
        wg_toolbox.setMinimumSize(QSize(0, 0))
        self.gridLayout_9 = QGridLayout(wg_toolbox)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 85, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.layout_watermark = QGridLayout()
        self.layout_watermark.setSpacing(0)
        self.layout_watermark.setObjectName(u"layout_watermark")
        self.layout_watermark.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.bt_watermark = QPushButton(wg_toolbox)
        self.bt_watermark.setObjectName(u"bt_watermark")
        self.bt_watermark.setMinimumSize(QSize(0, 25))
        self.bt_watermark.setCheckable(True)
        self.bt_watermark.setChecked(False)
        self.bt_watermark.setAutoDefault(False)
        self.bt_watermark.setFlat(False)

        self.layout_watermark.addWidget(self.bt_watermark, 0, 0, 1, 1)

        self.page_1 = QFrame(wg_toolbox)
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMinimumSize(QSize(0, 0))
        self.page_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.page_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.page_1)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.layout_watermark.addWidget(self.page_1, 1, 0, 1, 1)


        self.gridLayout_9.addLayout(self.layout_watermark, 0, 0, 1, 1)

        self.layout_rename = QGridLayout()
        self.layout_rename.setSpacing(0)
        self.layout_rename.setObjectName(u"layout_rename")
        self.layout_rename.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.bt_rename = QPushButton(wg_toolbox)
        self.bt_rename.setObjectName(u"bt_rename")
        self.bt_rename.setMinimumSize(QSize(0, 25))
        self.bt_rename.setCheckable(True)
        self.bt_rename.setChecked(False)
        self.bt_rename.setAutoDefault(False)
        self.bt_rename.setFlat(False)

        self.layout_rename.addWidget(self.bt_rename, 0, 0, 1, 1)

        self.page_3 = QFrame(wg_toolbox)
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMinimumSize(QSize(0, 0))
        self.page_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.page_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)

        self.layout_rename.addWidget(self.page_3, 1, 0, 1, 1)


        self.gridLayout_9.addLayout(self.layout_rename, 2, 0, 1, 1)

        self.layout_save = QGridLayout()
        self.layout_save.setSpacing(0)
        self.layout_save.setObjectName(u"layout_save")
        self.layout_save.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.bt_save = QPushButton(wg_toolbox)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setMinimumSize(QSize(0, 25))
        self.bt_save.setCheckable(True)
        self.bt_save.setChecked(False)
        self.bt_save.setAutoDefault(False)
        self.bt_save.setFlat(False)

        self.layout_save.addWidget(self.bt_save, 0, 0, 1, 1)

        self.page_4 = QFrame(wg_toolbox)
        self.page_4.setObjectName(u"page_4")
        self.page_4.setMinimumSize(QSize(0, 0))
        self.page_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.page_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.page_4)
        self.gridLayout_8.setSpacing(5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)

        self.layout_save.addWidget(self.page_4, 1, 0, 1, 1)


        self.gridLayout_9.addLayout(self.layout_save, 3, 0, 1, 1)

        self.layout_resize = QGridLayout()
        self.layout_resize.setSpacing(0)
        self.layout_resize.setObjectName(u"layout_resize")
        self.layout_resize.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.bt_resize = QPushButton(wg_toolbox)
        self.bt_resize.setObjectName(u"bt_resize")
        self.bt_resize.setMinimumSize(QSize(0, 25))
        self.bt_resize.setCheckable(True)
        self.bt_resize.setChecked(False)
        self.bt_resize.setAutoDefault(False)
        self.bt_resize.setFlat(False)

        self.layout_resize.addWidget(self.bt_resize, 0, 0, 1, 1)

        self.page_2 = QFrame(wg_toolbox)
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMinimumSize(QSize(300, 0))
        self.page_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.page_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.layout_resize.addWidget(self.page_2, 1, 0, 1, 1)


        self.gridLayout_9.addLayout(self.layout_resize, 1, 0, 1, 1)


        self.retranslateUi(wg_toolbox)
        self.bt_resize.clicked["bool"].connect(self.page_2.setHidden)
        self.bt_watermark.clicked["bool"].connect(self.page_1.setHidden)
        self.bt_rename.clicked["bool"].connect(self.page_3.setHidden)
        self.bt_save.clicked["bool"].connect(self.page_4.setHidden)

        self.bt_watermark.setDefault(False)
        self.bt_rename.setDefault(False)
        self.bt_save.setDefault(False)
        self.bt_resize.setDefault(False)


        QMetaObject.connectSlotsByName(wg_toolbox)
    # setupUi

    def retranslateUi(self, wg_toolbox):
        wg_toolbox.setWindowTitle(QCoreApplication.translate("wg_toolbox", u"ToolBox", None))
        self.bt_watermark.setText(QCoreApplication.translate("wg_toolbox", u"Watermark", None))
        self.bt_rename.setText(QCoreApplication.translate("wg_toolbox", u"Rename", None))
        self.bt_save.setText(QCoreApplication.translate("wg_toolbox", u"Save As", None))
        self.bt_resize.setText(QCoreApplication.translate("wg_toolbox", u"Resize", None))
    # retranslateUi

