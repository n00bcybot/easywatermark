# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resize_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_wg_resize(object):
    def setupUi(self, wg_resize):
        if not wg_resize.objectName():
            wg_resize.setObjectName(u"wg_resize")
        wg_resize.resize(300, 323)
        wg_resize.setMinimumSize(QSize(300, 0))
        self.gridLayout_5 = QGridLayout(wg_resize)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.fr_container = QFrame(wg_resize)
        self.fr_container.setObjectName(u"fr_container")
        self.fr_container.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_container.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.fr_container)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.rb_custom = QRadioButton(self.fr_container)
        self.rb_custom.setObjectName(u"rb_custom")
        self.rb_custom.setMinimumSize(QSize(110, 0))

        self.verticalLayout.addWidget(self.rb_custom)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.fr_container)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.lb_width = QLabel(self.groupBox)
        self.lb_width.setObjectName(u"lb_width")

        self.gridLayout_4.addWidget(self.lb_width, 0, 0, 1, 1)

        self.chb_keep_ratio = QCheckBox(self.groupBox)
        self.chb_keep_ratio.setObjectName(u"chb_keep_ratio")

        self.gridLayout_4.addWidget(self.chb_keep_ratio, 2, 0, 1, 2)

        self.lb_height = QLabel(self.groupBox)
        self.lb_height.setObjectName(u"lb_height")

        self.gridLayout_4.addWidget(self.lb_height, 0, 1, 1, 1)

        self.le_width = QLineEdit(self.groupBox)
        self.le_width.setObjectName(u"le_width")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_width.sizePolicy().hasHeightForWidth())
        self.le_width.setSizePolicy(sizePolicy)
        self.le_width.setMaximumSize(QSize(60, 16777215))
        self.le_width.setSizeIncrement(QSize(0, 0))

        self.gridLayout_4.addWidget(self.le_width, 1, 0, 1, 1)

        self.le_height = QLineEdit(self.groupBox)
        self.le_height.setObjectName(u"le_height")
        sizePolicy.setHeightForWidth(self.le_height.sizePolicy().hasHeightForWidth())
        self.le_height.setSizePolicy(sizePolicy)
        self.le_height.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_4.addWidget(self.le_height, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.rb_percent = QRadioButton(self.fr_container)
        self.rb_percent.setObjectName(u"rb_percent")
        self.rb_percent.setMinimumSize(QSize(110, 0))

        self.verticalLayout_2.addWidget(self.rb_percent)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.fr_container)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.le_percent = QLineEdit(self.groupBox_2)
        self.le_percent.setObjectName(u"le_percent")
        self.le_percent.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.le_percent)

        self.lb_percent = QLabel(self.groupBox_2)
        self.lb_percent.setObjectName(u"lb_percent")

        self.horizontalLayout_3.addWidget(self.lb_percent)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.rb_predefined = QRadioButton(self.fr_container)
        self.rb_predefined.setObjectName(u"rb_predefined")
        self.rb_predefined.setMinimumSize(QSize(110, 0))

        self.verticalLayout_3.addWidget(self.rb_predefined)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.fr_container)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFlat(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.cb_psize = QComboBox(self.groupBox_3)
        self.cb_psize.addItem("")
        self.cb_psize.addItem("")
        self.cb_psize.addItem("")
        self.cb_psize.setObjectName(u"cb_psize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_psize.sizePolicy().hasHeightForWidth())
        self.cb_psize.setSizePolicy(sizePolicy1)
        self.cb_psize.setFrame(False)

        self.horizontalLayout_4.addWidget(self.cb_psize)


        self.gridLayout_3.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.lb_projected = QLabel(self.fr_container)
        self.lb_projected.setObjectName(u"lb_projected")

        self.horizontalLayout.addWidget(self.lb_projected)

        self.lb_projected_dsp = QLabel(self.fr_container)
        self.lb_projected_dsp.setObjectName(u"lb_projected_dsp")

        self.horizontalLayout.addWidget(self.lb_projected_dsp)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)


        self.gridLayout_5.addWidget(self.fr_container, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chb_resize = QCheckBox(wg_resize)
        self.chb_resize.setObjectName(u"chb_resize")

        self.horizontalLayout_2.addWidget(self.chb_resize)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(wg_resize)
        self.chb_resize.clicked["bool"].connect(self.fr_container.setEnabled)

        QMetaObject.connectSlotsByName(wg_resize)
    # setupUi

    def retranslateUi(self, wg_resize):
        wg_resize.setWindowTitle(QCoreApplication.translate("wg_resize", u"ResizeWidget", None))
        self.rb_custom.setText(QCoreApplication.translate("wg_resize", u"Custom Size", None))
        self.groupBox.setTitle("")
        self.lb_width.setText(QCoreApplication.translate("wg_resize", u"  Width", None))
        self.chb_keep_ratio.setText(QCoreApplication.translate("wg_resize", u"Keep Aspect Ratio", None))
        self.lb_height.setText(QCoreApplication.translate("wg_resize", u"  Height", None))
        self.rb_percent.setText(QCoreApplication.translate("wg_resize", u"By Percentage", None))
        self.groupBox_2.setTitle("")
        self.lb_percent.setText(QCoreApplication.translate("wg_resize", u"%", None))
        self.rb_predefined.setText(QCoreApplication.translate("wg_resize", u"Predefined Size", None))
        self.groupBox_3.setTitle("")
        self.cb_psize.setItemText(0, QCoreApplication.translate("wg_resize", u"1920 x 1080 (Full HD)", None))
        self.cb_psize.setItemText(1, QCoreApplication.translate("wg_resize", u"2048\u2009\u00d7\u20091152 (QWXGA)", None))
        self.cb_psize.setItemText(2, QCoreApplication.translate("wg_resize", u"800 x 600", None))

        self.cb_psize.setCurrentText(QCoreApplication.translate("wg_resize", u"1920 x 1080 (Full HD)", None))
        self.lb_projected.setText(QCoreApplication.translate("wg_resize", u"Projected Size:  ", None))
        self.lb_projected_dsp.setText("")
        self.chb_resize.setText(QCoreApplication.translate("wg_resize", u"Resize", None))
    # retranslateUi

