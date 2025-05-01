# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'watermark_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFontComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_wg_watermark(object):
    def setupUi(self, wg_watermark):
        if not wg_watermark.objectName():
            wg_watermark.setObjectName(u"wg_watermark")
        wg_watermark.resize(300, 153)
        wg_watermark.setMinimumSize(QSize(300, 0))
        self.gridLayout_2 = QGridLayout(wg_watermark)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.chb_watermark = QCheckBox(wg_watermark)
        self.chb_watermark.setObjectName(u"chb_watermark")

        self.gridLayout_2.addWidget(self.chb_watermark, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(189, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.fr_container = QFrame(wg_watermark)
        self.fr_container.setObjectName(u"fr_container")
        self.fr_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_container.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.fr_container)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fr_browse = QFrame(self.fr_container)
        self.fr_browse.setObjectName(u"fr_browse")
        self.fr_browse.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_browse.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fr_browse)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_browse = QPushButton(self.fr_browse)
        self.bt_browse.setObjectName(u"bt_browse")

        self.horizontalLayout_2.addWidget(self.bt_browse)


        self.gridLayout.addWidget(self.fr_browse, 0, 2, 1, 1)

        self.rb_text = QRadioButton(self.fr_container)
        self.rb_text.setObjectName(u"rb_text")

        self.gridLayout.addWidget(self.rb_text, 1, 0, 1, 1)

        self.fr_combo = QFrame(self.fr_container)
        self.fr_combo.setObjectName(u"fr_combo")
        self.fr_combo.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_combo.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.fr_combo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.comb_text = QFontComboBox(self.fr_combo)
        self.comb_text.setObjectName(u"comb_text")

        self.horizontalLayout.addWidget(self.comb_text)


        self.gridLayout.addWidget(self.fr_combo, 1, 2, 1, 1)

        self.rb_import = QRadioButton(self.fr_container)
        self.rb_import.setObjectName(u"rb_import")

        self.gridLayout.addWidget(self.rb_import, 0, 0, 1, 1)

        self.lb_enter_text = QLabel(self.fr_container)
        self.lb_enter_text.setObjectName(u"lb_enter_text")

        self.gridLayout.addWidget(self.lb_enter_text, 2, 0, 1, 1)

        self.le_text = QLineEdit(self.fr_container)
        self.le_text.setObjectName(u"le_text")

        self.gridLayout.addWidget(self.le_text, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.fr_container, 1, 0, 1, 2)


        self.retranslateUi(wg_watermark)
        self.chb_watermark.clicked["bool"].connect(self.fr_container.setEnabled)
        self.rb_import.toggled.connect(self.fr_browse.setEnabled)
        self.rb_text.toggled.connect(self.fr_combo.setEnabled)
        self.rb_text.toggled.connect(self.lb_enter_text.setEnabled)
        self.rb_text.toggled.connect(self.le_text.setEnabled)

        QMetaObject.connectSlotsByName(wg_watermark)
    # setupUi

    def retranslateUi(self, wg_watermark):
        wg_watermark.setWindowTitle(QCoreApplication.translate("wg_watermark", u"WatermarkWidget", None))
        self.chb_watermark.setText(QCoreApplication.translate("wg_watermark", u"Watermark", None))
        self.bt_browse.setText(QCoreApplication.translate("wg_watermark", u"Browse", None))
        self.rb_text.setText(QCoreApplication.translate("wg_watermark", u"Create From Text", None))
        self.rb_import.setText(QCoreApplication.translate("wg_watermark", u"Import Watermark", None))
        self.lb_enter_text.setText(QCoreApplication.translate("wg_watermark", u"        Enter Text", None))
    # retranslateUi

