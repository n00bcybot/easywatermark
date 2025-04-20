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
        Rename.resize(300, 384)
        Rename.setMinimumSize(QSize(300, 0))
        self.verticalLayout = QVBoxLayout(Rename)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.chb_rename = QCheckBox(Rename)
        self.chb_rename.setObjectName(u"chb_rename")

        self.verticalLayout.addWidget(self.chb_rename)

        self.fr_container = QFrame(Rename)
        self.fr_container.setObjectName(u"fr_container")
        self.fr_container.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_container.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.fr_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fr_set_name = QFrame(self.fr_container)
        self.fr_set_name.setObjectName(u"fr_set_name")
        self.fr_set_name.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_set_name.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_set_name)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.rb_change = QRadioButton(self.fr_set_name)
        self.rb_change.setObjectName(u"rb_change")
        self.rb_change.setCheckable(True)
        self.rb_change.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.rb_change)

        self.fr_new_name = QFrame(self.fr_set_name)
        self.fr_new_name.setObjectName(u"fr_new_name")
        self.fr_new_name.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_new_name.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_new_name)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_new_name = QLabel(self.fr_new_name)
        self.lb_new_name.setObjectName(u"lb_new_name")

        self.horizontalLayout.addWidget(self.lb_new_name)

        self.le_new_name = QLineEdit(self.fr_new_name)
        self.le_new_name.setObjectName(u"le_new_name")

        self.horizontalLayout.addWidget(self.le_new_name)


        self.verticalLayout_4.addWidget(self.fr_new_name)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.rb_keep = QRadioButton(self.fr_set_name)
        self.rb_keep.setObjectName(u"rb_keep")
        self.rb_keep.setCheckable(True)

        self.verticalLayout_4.addWidget(self.rb_keep)

        self.fr_keep_name = QFrame(self.fr_set_name)
        self.fr_keep_name.setObjectName(u"fr_keep_name")
        self.fr_keep_name.setFrameShape(QFrame.Shape.NoFrame)
        self.fr_keep_name.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_keep_name)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rb_remove_string = QRadioButton(self.fr_keep_name)
        self.rb_remove_string.setObjectName(u"rb_remove_string")

        self.horizontalLayout_2.addWidget(self.rb_remove_string)

        self.le_remove_string = QLineEdit(self.fr_keep_name)
        self.le_remove_string.setObjectName(u"le_remove_string")

        self.horizontalLayout_2.addWidget(self.le_remove_string)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rb_remove_first = QRadioButton(self.fr_keep_name)
        self.rb_remove_first.setObjectName(u"rb_remove_first")

        self.horizontalLayout_3.addWidget(self.rb_remove_first)

        self.le_remove_first = QLineEdit(self.fr_keep_name)
        self.le_remove_first.setObjectName(u"le_remove_first")
        self.le_remove_first.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.le_remove_first)

        self.lb_remove_first = QLabel(self.fr_keep_name)
        self.lb_remove_first.setObjectName(u"lb_remove_first")

        self.horizontalLayout_3.addWidget(self.lb_remove_first)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.rb_remove_last = QRadioButton(self.fr_keep_name)
        self.rb_remove_last.setObjectName(u"rb_remove_last")

        self.horizontalLayout_4.addWidget(self.rb_remove_last)

        self.le_remove_last = QLineEdit(self.fr_keep_name)
        self.le_remove_last.setObjectName(u"le_remove_last")
        self.le_remove_last.setMinimumSize(QSize(30, 0))
        self.le_remove_last.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.le_remove_last)

        self.lb_remove_last = QLabel(self.fr_keep_name)
        self.lb_remove_last.setObjectName(u"lb_remove_last")

        self.horizontalLayout_4.addWidget(self.lb_remove_last)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addWidget(self.fr_keep_name)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.fr_set_name)

        self.layout_prefix = QHBoxLayout()
        self.layout_prefix.setObjectName(u"layout_prefix")
        self.lb_add_prefix = QLabel(self.fr_container)
        self.lb_add_prefix.setObjectName(u"lb_add_prefix")

        self.layout_prefix.addWidget(self.lb_add_prefix)

        self.le_add_prefix = QLineEdit(self.fr_container)
        self.le_add_prefix.setObjectName(u"le_add_prefix")
        self.le_add_prefix.setMinimumSize(QSize(150, 0))

        self.layout_prefix.addWidget(self.le_add_prefix)


        self.verticalLayout_3.addLayout(self.layout_prefix)

        self.layout_suffix = QHBoxLayout()
        self.layout_suffix.setObjectName(u"layout_suffix")
        self.lb_add_suffix = QLabel(self.fr_container)
        self.lb_add_suffix.setObjectName(u"lb_add_suffix")

        self.layout_suffix.addWidget(self.lb_add_suffix)

        self.le_add_suffix = QLineEdit(self.fr_container)
        self.le_add_suffix.setObjectName(u"le_add_suffix")
        self.le_add_suffix.setMinimumSize(QSize(150, 0))

        self.layout_suffix.addWidget(self.le_add_suffix)


        self.verticalLayout_3.addLayout(self.layout_suffix)

        self.layout_count = QHBoxLayout()
        self.layout_count.setObjectName(u"layout_count")
        self.chb_add_count = QCheckBox(self.fr_container)
        self.chb_add_count.setObjectName(u"chb_add_count")

        self.layout_count.addWidget(self.chb_add_count)

        self.comb_digit = QComboBox(self.fr_container)
        self.comb_digit.addItem("")
        self.comb_digit.addItem("")
        self.comb_digit.addItem("")
        self.comb_digit.addItem("")
        self.comb_digit.addItem("")
        self.comb_digit.addItem("")
        self.comb_digit.setObjectName(u"comb_digit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comb_digit.sizePolicy().hasHeightForWidth())
        self.comb_digit.setSizePolicy(sizePolicy)
        self.comb_digit.setMinimumSize(QSize(150, 0))

        self.layout_count.addWidget(self.comb_digit)


        self.verticalLayout_3.addLayout(self.layout_count)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_delimiter = QLabel(self.fr_container)
        self.lb_delimiter.setObjectName(u"lb_delimiter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_delimiter.sizePolicy().hasHeightForWidth())
        self.lb_delimiter.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.lb_delimiter)

        self.comb_delimiter = QComboBox(self.fr_container)
        self.comb_delimiter.addItem("")
        self.comb_delimiter.addItem("")
        self.comb_delimiter.addItem("")
        self.comb_delimiter.setObjectName(u"comb_delimiter")
        sizePolicy.setHeightForWidth(self.comb_delimiter.sizePolicy().hasHeightForWidth())
        self.comb_delimiter.setSizePolicy(sizePolicy)
        self.comb_delimiter.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_6.addWidget(self.comb_delimiter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.lb_preview = QLabel(self.fr_container)
        self.lb_preview.setObjectName(u"lb_preview")
        self.lb_preview.setMinimumSize(QSize(0, 24))
        self.lb_preview.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_3.addWidget(self.lb_preview)


        self.verticalLayout.addWidget(self.fr_container)


        self.retranslateUi(Rename)
        self.chb_rename.clicked["bool"].connect(self.fr_container.setEnabled)
        self.rb_change.toggled.connect(self.fr_new_name.setEnabled)
        self.rb_keep.toggled.connect(self.fr_keep_name.setEnabled)
        self.chb_add_count.clicked["bool"].connect(self.comb_digit.setEnabled)

        QMetaObject.connectSlotsByName(Rename)
    # setupUi

    def retranslateUi(self, Rename):
        Rename.setWindowTitle(QCoreApplication.translate("Rename", u"RenameWidget", None))
        self.chb_rename.setText(QCoreApplication.translate("Rename", u"Rename", None))
        self.rb_change.setText(QCoreApplication.translate("Rename", u"Change name", None))
        self.lb_new_name.setText(QCoreApplication.translate("Rename", u"    Enter new name     ", None))
        self.rb_keep.setText(QCoreApplication.translate("Rename", u"Keep the same name", None))
        self.rb_remove_string.setText(QCoreApplication.translate("Rename", u"Remove string", None))
        self.rb_remove_first.setText(QCoreApplication.translate("Rename", u"Remove first    ", None))
        self.lb_remove_first.setText(QCoreApplication.translate("Rename", u"character(s)", None))
        self.rb_remove_last.setText(QCoreApplication.translate("Rename", u"Remove last     ", None))
        self.lb_remove_last.setText(QCoreApplication.translate("Rename", u"character(s)", None))
        self.lb_add_prefix.setText(QCoreApplication.translate("Rename", u"Add prefix                    ", None))
        self.lb_add_suffix.setText(QCoreApplication.translate("Rename", u"Add suffix                    ", None))
        self.chb_add_count.setText(QCoreApplication.translate("Rename", u"Add counter       ", None))
        self.comb_digit.setItemText(0, QCoreApplication.translate("Rename", u"1 digit", None))
        self.comb_digit.setItemText(1, QCoreApplication.translate("Rename", u"2 digits", None))
        self.comb_digit.setItemText(2, QCoreApplication.translate("Rename", u"3 digits", None))
        self.comb_digit.setItemText(3, QCoreApplication.translate("Rename", u"4 digits", None))
        self.comb_digit.setItemText(4, QCoreApplication.translate("Rename", u"5 digits", None))
        self.comb_digit.setItemText(5, QCoreApplication.translate("Rename", u"6 digits", None))

        self.lb_delimiter.setText(QCoreApplication.translate("Rename", u"Choose delimiter       ", None))
        self.comb_delimiter.setItemText(0, QCoreApplication.translate("Rename", u". (dot)", None))
        self.comb_delimiter.setItemText(1, QCoreApplication.translate("Rename", u"- (dash)", None))
        self.comb_delimiter.setItemText(2, QCoreApplication.translate("Rename", u"_ (underscore)", None))

        self.lb_preview.setText("")
    # retranslateUi

