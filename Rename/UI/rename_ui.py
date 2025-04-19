# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rename_ui.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Rename(object):
    def setupUi(self, Rename):
        if not Rename.objectName():
            Rename.setObjectName(u"Rename")
        Rename.resize(300, 380)
        Rename.setMinimumSize(QSize(300, 0))
        self.verticalLayout_4 = QVBoxLayout(Rename)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.chb_rename = QCheckBox(Rename)
        self.chb_rename.setObjectName(u"chb_rename")

        self.verticalLayout_4.addWidget(self.chb_rename)

        self.fr_container = QFrame(Rename)
        self.fr_container.setObjectName(u"fr_container")
        self.fr_container.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.fr_name_choice = QFrame(self.fr_container)
        self.fr_name_choice.setObjectName(u"fr_name_choice")
        self.fr_name_choice.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_name_choice.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_name_choice)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rb_keep = QRadioButton(self.fr_name_choice)
        self.rb_keep.setObjectName(u"rb_keep")

        self.verticalLayout_2.addWidget(self.rb_keep)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.rb_change = QRadioButton(self.fr_name_choice)
        self.rb_change.setObjectName(u"rb_change")
        self.rb_change.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.rb_change)


        self.verticalLayout_3.addWidget(self.fr_name_choice)

        self.fr_ch_name_opt = QFrame(self.fr_container)
        self.fr_ch_name_opt.setObjectName(u"fr_ch_name_opt")
        self.fr_ch_name_opt.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_ch_name_opt.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_ch_name_opt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_3 = QRadioButton(self.fr_ch_name_opt)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.lineEdit = QLineEdit(self.fr_ch_name_opt)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_4 = QRadioButton(self.fr_ch_name_opt)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_2.addWidget(self.radioButton_4)

        self.lineEdit_2 = QLineEdit(self.fr_ch_name_opt)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radioButton_5 = QRadioButton(self.fr_ch_name_opt)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_3.addWidget(self.radioButton_5)

        self.lineEdit_3 = QLineEdit(self.fr_ch_name_opt)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.label = QLabel(self.fr_ch_name_opt)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_6 = QRadioButton(self.fr_ch_name_opt)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_4.addWidget(self.radioButton_6)

        self.lineEdit_4 = QLineEdit(self.fr_ch_name_opt)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(30, 0))
        self.lineEdit_4.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.label_2 = QLabel(self.fr_ch_name_opt)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.fr_ch_name_opt)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.layout_prefix = QHBoxLayout()
        self.layout_prefix.setObjectName(u"layout_prefix")
        self.checkBox = QCheckBox(self.fr_container)
        self.checkBox.setObjectName(u"checkBox")

        self.layout_prefix.addWidget(self.checkBox)

        self.lineEdit_5 = QLineEdit(self.fr_container)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.layout_prefix.addWidget(self.lineEdit_5)


        self.verticalLayout_3.addLayout(self.layout_prefix)

        self.layout_suffix = QHBoxLayout()
        self.layout_suffix.setObjectName(u"layout_suffix")
        self.checkBox_2 = QCheckBox(self.fr_container)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.layout_suffix.addWidget(self.checkBox_2)

        self.lineEdit_6 = QLineEdit(self.fr_container)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.layout_suffix.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addLayout(self.layout_suffix)

        self.layout_count = QHBoxLayout()
        self.layout_count.setObjectName(u"layout_count")
        self.checkBox_3 = QCheckBox(self.fr_container)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.layout_count.addWidget(self.checkBox_3)

        self.comboBox = QComboBox(self.fr_container)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(170, 0))

        self.layout_count.addWidget(self.comboBox)


        self.verticalLayout_3.addLayout(self.layout_count)

        self.lb_preview = QLabel(self.fr_container)
        self.lb_preview.setObjectName(u"lb_preview")

        self.verticalLayout_3.addWidget(self.lb_preview)


        self.verticalLayout_4.addWidget(self.fr_container)


        self.retranslateUi(Rename)
        self.chb_rename.clicked["bool"].connect(self.fr_container.setEnabled)

        QMetaObject.connectSlotsByName(Rename)
    # setupUi

    def retranslateUi(self, Rename):
        Rename.setWindowTitle(QCoreApplication.translate("Rename", u"RenameWidget", None))
        self.chb_rename.setText(QCoreApplication.translate("Rename", u"Rename", None))
        self.rb_keep.setText(QCoreApplication.translate("Rename", u"Keep the same name", None))
        self.rb_change.setText(QCoreApplication.translate("Rename", u"Change name", None))
        self.radioButton_3.setText(QCoreApplication.translate("Rename", u"New name      ", None))
        self.radioButton_4.setText(QCoreApplication.translate("Rename", u"Remove string", None))
        self.radioButton_5.setText(QCoreApplication.translate("Rename", u"Remove first    ", None))
        self.label.setText(QCoreApplication.translate("Rename", u"character(s)", None))
        self.radioButton_6.setText(QCoreApplication.translate("Rename", u"Remove last     ", None))
        self.label_2.setText(QCoreApplication.translate("Rename", u"character(s)", None))
        self.checkBox.setText(QCoreApplication.translate("Rename", u"Add prefix        ", None))
        self.checkBox_2.setText(QCoreApplication.translate("Rename", u"Add suffix        ", None))
        self.checkBox_3.setText(QCoreApplication.translate("Rename", u"Add count", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Rename", u"1 digit", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Rename", u"2 digits", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Rename", u"3 digits", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Rename", u"4 digits", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Rename", u"5 digits", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Rename", u"6 digits", None))

        self.lb_preview.setText("")
    # retranslateUi

