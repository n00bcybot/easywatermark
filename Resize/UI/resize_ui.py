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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_wg_resize(object):
    def setupUi(self, wg_resize):
        if not wg_resize.objectName():
            wg_resize.setObjectName(u"wg_resize")
        wg_resize.resize(293, 286)
        self.gridLayout_5 = QGridLayout(wg_resize)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.groupBox = QGroupBox(wg_resize)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 2, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QSize(60, 16777215))
        self.lineEdit.setSizeIncrement(QSize(0, 0))

        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(wg_resize)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(110, 0))

        self.verticalLayout.addWidget(self.radioButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_2 = QRadioButton(wg_resize)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setMinimumSize(QSize(110, 0))

        self.verticalLayout_2.addWidget(self.radioButton_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(wg_resize)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButton_3 = QRadioButton(wg_resize)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setMinimumSize(QSize(110, 0))

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(wg_resize)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFlat(False)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_4.addWidget(self.comboBox)


        self.gridLayout_3.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(wg_resize)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(wg_resize)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.gridLayout_5.addLayout(self.horizontalLayout, 3, 0, 1, 1)


        self.retranslateUi(wg_resize)

        QMetaObject.connectSlotsByName(wg_resize)
    # setupUi

    def retranslateUi(self, wg_resize):
        wg_resize.setWindowTitle(QCoreApplication.translate("wg_resize", u"Resize", None))
        self.groupBox.setTitle("")
        self.label_5.setText(QCoreApplication.translate("wg_resize", u"  Width", None))
        self.checkBox.setText(QCoreApplication.translate("wg_resize", u"Keep Aspect Ratio", None))
        self.label_6.setText(QCoreApplication.translate("wg_resize", u"  Height", None))
        self.radioButton.setText(QCoreApplication.translate("wg_resize", u"Custom Size", None))
        self.radioButton_2.setText(QCoreApplication.translate("wg_resize", u"By Percentage", None))
        self.groupBox_2.setTitle("")
        self.label_7.setText(QCoreApplication.translate("wg_resize", u"%", None))
        self.radioButton_3.setText(QCoreApplication.translate("wg_resize", u"Predefined Size", None))
        self.groupBox_3.setTitle("")
        self.comboBox.setItemText(0, QCoreApplication.translate("wg_resize", u"1920 x 1080 (Full HD)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("wg_resize", u"2048\u2009\u00d7\u20091152 (QWXGA)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("wg_resize", u"800 x 600", None))

        self.label.setText(QCoreApplication.translate("wg_resize", u"Projected Size", None))
        self.label_2.setText("")
    # retranslateUi

