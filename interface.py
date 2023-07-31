# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStackedWidget, QTextBrowser,
    QVBoxLayout, QWidget)
import files_rc
import files_rc

class Ui_migr(object):
    def setupUi(self, migr):
        if not migr.objectName():
            migr.setObjectName(u"migr")
        migr.resize(1126, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(migr.sizePolicy().hasHeightForWidth())
        migr.setSizePolicy(sizePolicy)
        migr.setMinimumSize(QSize(1126, 700))
        migr.setMaximumSize(QSize(1126, 700))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(51, 153, 255, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        migr.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        migr.setFont(font)
        migr.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(migr)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-transfer.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(True)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy3)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.paginas = QStackedWidget(self.frame_content)
        self.paginas.setObjectName(u"paginas")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.paginas.sizePolicy().hasHeightForWidth())
        self.paginas.setSizePolicy(sizePolicy4)
        self.paginas.setStyleSheet(u"background: transparent;")
        self.paginas.setFrameShadow(QFrame.Plain)
        self.paginas.setLineWidth(1)
        self.bemvindo = QWidget()
        self.bemvindo.setObjectName(u"bemvindo")
        self.frame_div_content_6 = QFrame(self.bemvindo)
        self.frame_div_content_6.setObjectName(u"frame_div_content_6")
        self.frame_div_content_6.setGeometry(QRect(350, 40, 411, 500))
        self.frame_div_content_6.setMinimumSize(QSize(0, 500))
        self.frame_div_content_6.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_6.setFocusPolicy(Qt.ClickFocus)
        self.frame_div_content_6.setContextMenuPolicy(Qt.CustomContextMenu)
        self.frame_div_content_6.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_6.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_6.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_div_content_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 70, 231, 61))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(40)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"")
        self.label_7.setPixmap(QPixmap(u"imgs/logo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.btn_vai_firebird = QPushButton(self.frame_div_content_6)
        self.btn_vai_firebird.setObjectName(u"btn_vai_firebird")
        self.btn_vai_firebird.setGeometry(QRect(130, 400, 171, 30))
        self.btn_vai_firebird.setMinimumSize(QSize(150, 30))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(9)
        self.btn_vai_firebird.setFont(font5)
        self.btn_vai_firebird.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_vai_firebird.setIcon(icon3)
        self.labelBoxBlenderInstalation_12 = QLabel(self.frame_div_content_6)
        self.labelBoxBlenderInstalation_12.setObjectName(u"labelBoxBlenderInstalation_12")
        self.labelBoxBlenderInstalation_12.setGeometry(QRect(70, 170, 291, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.labelBoxBlenderInstalation_12.setFont(font6)
        self.labelBoxBlenderInstalation_12.setStyleSheet(u"")
        self.barrinha = QTextBrowser(self.frame_div_content_6)
        self.barrinha.setObjectName(u"barrinha")
        self.barrinha.setGeometry(QRect(55, 320, 321, 50))
        self.barrinha.setMinimumSize(QSize(0, 0))
        self.barrinha.setMaximumSize(QSize(321, 50))
        self.barrinha.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.barrinha.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.barrinha.setFrameShape(QFrame.StyledPanel)
        self.barrinha.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.barrinha.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.barrinha.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textBrowser_5 = QTextBrowser(self.frame_div_content_6)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(65, 250, 301, 51))
        self.textBrowser_5.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelBoxBlenderInstalation_13 = QLabel(self.frame_div_content_6)
        self.labelBoxBlenderInstalation_13.setObjectName(u"labelBoxBlenderInstalation_13")
        self.labelBoxBlenderInstalation_13.setGeometry(QRect(140, 200, 161, 31))
        self.labelBoxBlenderInstalation_13.setFont(font6)
        self.labelBoxBlenderInstalation_13.setStyleSheet(u"")
        self.paginas.addWidget(self.bemvindo)
        self.firebird = QWidget()
        self.firebird.setObjectName(u"firebird")
        self.verticalLayout_6 = QVBoxLayout(self.firebird)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.firebird)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setGeometry(QRect(50, 180, 991, 81))
        self.frame_div_content_1.setMinimumSize(QSize(0, 50))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.caminho_gdb = QLineEdit(self.frame_div_content_1)
        self.caminho_gdb.setObjectName(u"caminho_gdb")
        self.caminho_gdb.setGeometry(QRect(10, 10, 791, 30))
        self.caminho_gdb.setMinimumSize(QSize(0, 30))
        self.caminho_gdb.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"color: rgb(98, 103, 111); ")
        self.labelVersion_3 = QLabel(self.frame_div_content_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setGeometry(QRect(20, 50, 281, 16))
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_procura_gdb = QPushButton(self.frame_div_content_1)
        self.btn_procura_gdb.setObjectName(u"btn_procura_gdb")
        self.btn_procura_gdb.setGeometry(QRect(810, 10, 171, 30))
        self.btn_procura_gdb.setMinimumSize(QSize(150, 30))
        self.btn_procura_gdb.setFont(font5)
        self.btn_procura_gdb.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_procura_gdb.setIcon(icon4)
        self.frame_title_wid_1 = QFrame(self.frame)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setGeometry(QRect(50, 140, 991, 35))
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setGeometry(QRect(9, 9, 176, 17))
        self.labelBoxBlenderInstalation.setFont(font1)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")
        self.btn_vai_postgres = QPushButton(self.frame)
        self.btn_vai_postgres.setObjectName(u"btn_vai_postgres")
        self.btn_vai_postgres.setGeometry(QRect(460, 290, 150, 30))
        self.btn_vai_postgres.setMinimumSize(QSize(150, 30))
        self.btn_vai_postgres.setFont(font5)
        self.btn_vai_postgres.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-chevron-circle-right-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_vai_postgres.setIcon(icon5)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 0, 151, 121))
        self.label_3.setPixmap(QPixmap(u"imgs/firebird.png"))
        self.label_3.setScaledContents(True)
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setGeometry(QRect(220, 10, 481, 31))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(16)
        font7.setBold(False)
        self.labelBoxBlenderInstalation_2.setFont(font7)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setGeometry(QRect(220, 50, 291, 17))
        self.labelBoxBlenderInstalation_3.setFont(font1)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")
        self.textBrowser_7 = QTextBrowser(self.frame)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(220, 80, 481, 41))
        self.textBrowser_7.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_12.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.paginas.addWidget(self.firebird)
        self.postgresql = QWidget()
        self.postgresql.setObjectName(u"postgresql")
        self.frame_2 = QFrame(self.postgresql)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(60, -30, 1006, 580))
        self.frame_2.setStyleSheet(u"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.VLine)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_div_content_3 = QFrame(self.frame_2)
        self.frame_div_content_3.setObjectName(u"frame_div_content_3")
        self.frame_div_content_3.setGeometry(QRect(0, 220, 991, 81))
        self.frame_div_content_3.setMinimumSize(QSize(0, 50))
        self.frame_div_content_3.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_3.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_3.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_3.setFrameShadow(QFrame.Raised)
        self.nome_nova_base = QLineEdit(self.frame_div_content_3)
        self.nome_nova_base.setObjectName(u"nome_nova_base")
        self.nome_nova_base.setGeometry(QRect(10, 10, 791, 30))
        self.nome_nova_base.setMinimumSize(QSize(0, 30))
        self.nome_nova_base.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"color: rgb(98, 103, 111); ")
        self.btn_cria_base = QPushButton(self.frame_div_content_3)
        self.btn_cria_base.setObjectName(u"btn_cria_base")
        self.btn_cria_base.setGeometry(QRect(810, 10, 171, 30))
        self.btn_cria_base.setMinimumSize(QSize(150, 30))
        self.btn_cria_base.setFont(font5)
        self.btn_cria_base.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cria_base.setIcon(icon6)
        self.frame_div_content_4 = QFrame(self.frame_div_content_3)
        self.frame_div_content_4.setObjectName(u"frame_div_content_4")
        self.frame_div_content_4.setGeometry(QRect(600, 50, 991, 61))
        self.frame_div_content_4.setMinimumSize(QSize(0, 50))
        self.frame_div_content_4.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_4.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_4.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_4.setFrameShadow(QFrame.Raised)
        self.pushButton_10 = QPushButton(self.frame_div_content_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(630, 10, 171, 30))
        self.pushButton_10.setMinimumSize(QSize(150, 30))
        self.pushButton_10.setFont(font5)
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_10.setIcon(icon4)
        self.pushButton_11 = QPushButton(self.frame_div_content_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(810, 10, 171, 30))
        self.pushButton_11.setMinimumSize(QSize(150, 30))
        self.pushButton_11.setFont(font5)
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-transfer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon7)
        self.layoutWidget = QWidget(self.frame_div_content_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(25, 52, 291, 18))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.msg_banco_criado = QLabel(self.layoutWidget)
        self.msg_banco_criado.setObjectName(u"msg_banco_criado")
        sizePolicy3.setHeightForWidth(self.msg_banco_criado.sizePolicy().hasHeightForWidth())
        self.msg_banco_criado.setSizePolicy(sizePolicy3)
        self.msg_banco_criado.setMinimumSize(QSize(261, 0))
        self.msg_banco_criado.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.msg_banco_criado.setLineWidth(1)
        self.msg_banco_criado.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.msg_banco_criado)

        self.icon_banco_criado = QLabel(self.layoutWidget)
        self.icon_banco_criado.setObjectName(u"icon_banco_criado")
        self.icon_banco_criado.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.icon_banco_criado.setAutoFillBackground(False)
        self.icon_banco_criado.setInputMethodHints(Qt.ImhHiddenText)
        self.icon_banco_criado.setPixmap(QPixmap(u":/16x16/icons/16x16/cil-check-circle.png"))

        self.horizontalLayout_9.addWidget(self.icon_banco_criado)

        self.frame_title_wid_2 = QFrame(self.frame_2)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setGeometry(QRect(0, 180, 991, 35))
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_6 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_6.setObjectName(u"labelBoxBlenderInstalation_6")
        self.labelBoxBlenderInstalation_6.setGeometry(QRect(9, 9, 211, 17))
        self.labelBoxBlenderInstalation_6.setFont(font1)
        self.labelBoxBlenderInstalation_6.setStyleSheet(u"")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 151, 121))
        self.label_4.setPixmap(QPixmap(u"imgs/postgresql.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.labelBoxBlenderInstalation_7 = QLabel(self.frame_2)
        self.labelBoxBlenderInstalation_7.setObjectName(u"labelBoxBlenderInstalation_7")
        self.labelBoxBlenderInstalation_7.setGeometry(QRect(170, 50, 481, 31))
        self.labelBoxBlenderInstalation_7.setFont(font7)
        self.labelBoxBlenderInstalation_7.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_8 = QLabel(self.frame_2)
        self.labelBoxBlenderInstalation_8.setObjectName(u"labelBoxBlenderInstalation_8")
        self.labelBoxBlenderInstalation_8.setGeometry(QRect(170, 90, 291, 17))
        self.labelBoxBlenderInstalation_8.setFont(font1)
        self.labelBoxBlenderInstalation_8.setStyleSheet(u"")
        self.textBrowser_3 = QTextBrowser(self.frame_2)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(170, 120, 471, 41))
        self.textBrowser_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.btn_vai_confirmacao = QPushButton(self.frame_2)
        self.btn_vai_confirmacao.setObjectName(u"btn_vai_confirmacao")
        self.btn_vai_confirmacao.setGeometry(QRect(500, 450, 150, 30))
        self.btn_vai_confirmacao.setMinimumSize(QSize(150, 30))
        self.btn_vai_confirmacao.setFont(font5)
        self.btn_vai_confirmacao.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_vai_confirmacao.setIcon(icon5)
        self.btn_volta_firebird = QPushButton(self.frame_2)
        self.btn_volta_firebird.setObjectName(u"btn_volta_firebird")
        self.btn_volta_firebird.setGeometry(QRect(340, 450, 150, 30))
        self.btn_volta_firebird.setMinimumSize(QSize(150, 30))
        self.btn_volta_firebird.setFont(font5)
        self.btn_volta_firebird.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-chevron-circle-left-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_volta_firebird.setIcon(icon8)
        self.frame_title_wid_4 = QFrame(self.frame_2)
        self.frame_title_wid_4.setObjectName(u"frame_title_wid_4")
        self.frame_title_wid_4.setGeometry(QRect(1, 311, 989, 35))
        self.frame_title_wid_4.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_4.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_4.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_4.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_11 = QLabel(self.frame_title_wid_4)
        self.labelBoxBlenderInstalation_11.setObjectName(u"labelBoxBlenderInstalation_11")
        self.labelBoxBlenderInstalation_11.setGeometry(QRect(9, 9, 211, 17))
        self.labelBoxBlenderInstalation_11.setFont(font1)
        self.labelBoxBlenderInstalation_11.setStyleSheet(u"")
        self.frame_title_wid_5 = QFrame(self.frame_title_wid_4)
        self.frame_title_wid_5.setObjectName(u"frame_title_wid_5")
        self.frame_title_wid_5.setGeometry(QRect(710, 20, 991, 35))
        self.frame_title_wid_5.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_5.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_5.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_5.setFrameShadow(QFrame.Raised)
        self.frame_div_content_5 = QFrame(self.frame_2)
        self.frame_div_content_5.setObjectName(u"frame_div_content_5")
        self.frame_div_content_5.setGeometry(QRect(1, 352, 989, 78))
        self.frame_div_content_5.setMinimumSize(QSize(0, 50))
        self.frame_div_content_5.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_5.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_5.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_5.setFrameShadow(QFrame.Raised)
        self.caminho_base_zerada = QLineEdit(self.frame_div_content_5)
        self.caminho_base_zerada.setObjectName(u"caminho_base_zerada")
        self.caminho_base_zerada.setGeometry(QRect(10, 10, 611, 30))
        self.caminho_base_zerada.setMinimumSize(QSize(0, 30))
        self.caminho_base_zerada.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"color: rgb(98, 103, 111); ")
        self.btn_busca_dump = QPushButton(self.frame_div_content_5)
        self.btn_busca_dump.setObjectName(u"btn_busca_dump")
        self.btn_busca_dump.setGeometry(QRect(630, 10, 171, 30))
        self.btn_busca_dump.setMinimumSize(QSize(150, 30))
        self.btn_busca_dump.setFont(font5)
        self.btn_busca_dump.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_busca_dump.setIcon(icon4)
        self.btn_zera_base = QPushButton(self.frame_div_content_5)
        self.btn_zera_base.setObjectName(u"btn_zera_base")
        self.btn_zera_base.setGeometry(QRect(810, 10, 171, 30))
        self.btn_zera_base.setMinimumSize(QSize(150, 30))
        self.btn_zera_base.setFont(font5)
        self.btn_zera_base.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_zera_base.setIcon(icon9)
        self.msg_base_importada = QLabel(self.frame_div_content_5)
        self.msg_base_importada.setObjectName(u"msg_base_importada")
        self.msg_base_importada.setGeometry(QRect(21, 51, 189, 16))
        self.msg_base_importada.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.msg_base_importada.setLineWidth(1)
        self.msg_base_importada.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.icon_base_importada = QLabel(self.frame_div_content_5)
        self.icon_base_importada.setObjectName(u"icon_base_importada")
        self.icon_base_importada.setGeometry(QRect(220, 51, 16, 16))
        self.icon_base_importada.setAutoFillBackground(False)
        self.icon_base_importada.setPixmap(QPixmap(u":/16x16/icons/16x16/cil-check-circle.png"))
        self.paginas.addWidget(self.postgresql)
        self.confirmacao = QWidget()
        self.confirmacao.setObjectName(u"confirmacao")
        self.frame_4 = QFrame(self.confirmacao)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(60, -30, 1006, 580))
        self.frame_4.setStyleSheet(u"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.VLine)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_div_content_7 = QFrame(self.frame_4)
        self.frame_div_content_7.setObjectName(u"frame_div_content_7")
        self.frame_div_content_7.setGeometry(QRect(0, 220, 991, 150))
        self.frame_div_content_7.setMinimumSize(QSize(0, 150))
        self.frame_div_content_7.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_7.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_7.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_7.setFrameShadow(QFrame.Raised)
        self.confirmar = QTextBrowser(self.frame_div_content_7)
        self.confirmar.setObjectName(u"confirmar")
        self.confirmar.setGeometry(QRect(10, 10, 541, 201))
        self.confirmar.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.frame_title_wid_3 = QFrame(self.frame_4)
        self.frame_title_wid_3.setObjectName(u"frame_title_wid_3")
        self.frame_title_wid_3.setGeometry(QRect(0, 180, 991, 35))
        self.frame_title_wid_3.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_3.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_3.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_3.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_14 = QLabel(self.frame_title_wid_3)
        self.labelBoxBlenderInstalation_14.setObjectName(u"labelBoxBlenderInstalation_14")
        self.labelBoxBlenderInstalation_14.setGeometry(QRect(9, 9, 211, 17))
        self.labelBoxBlenderInstalation_14.setFont(font1)
        self.labelBoxBlenderInstalation_14.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_15 = QLabel(self.frame_4)
        self.labelBoxBlenderInstalation_15.setObjectName(u"labelBoxBlenderInstalation_15")
        self.labelBoxBlenderInstalation_15.setGeometry(QRect(170, 50, 481, 31))
        self.labelBoxBlenderInstalation_15.setFont(font7)
        self.labelBoxBlenderInstalation_15.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_16 = QLabel(self.frame_4)
        self.labelBoxBlenderInstalation_16.setObjectName(u"labelBoxBlenderInstalation_16")
        self.labelBoxBlenderInstalation_16.setGeometry(QRect(170, 90, 291, 17))
        self.labelBoxBlenderInstalation_16.setFont(font1)
        self.labelBoxBlenderInstalation_16.setStyleSheet(u"")
        self.textBrowser_6 = QTextBrowser(self.frame_4)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(170, 120, 511, 41))
        self.textBrowser_6.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.btn_processar = QPushButton(self.frame_4)
        self.btn_processar.setObjectName(u"btn_processar")
        self.btn_processar.setGeometry(QRect(480, 390, 150, 30))
        self.btn_processar.setMinimumSize(QSize(150, 30))
        self.btn_processar.setFont(font5)
        self.btn_processar.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_processar.setIcon(icon7)
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 40, 151, 120))
        self.label_8.setPixmap(QPixmap(u"imgs/check.png"))
        self.label_8.setScaledContents(True)
        self.btn_volta_postgres = QPushButton(self.frame_4)
        self.btn_volta_postgres.setObjectName(u"btn_volta_postgres")
        self.btn_volta_postgres.setGeometry(QRect(320, 390, 150, 30))
        self.btn_volta_postgres.setMinimumSize(QSize(150, 30))
        self.btn_volta_postgres.setFont(font5)
        self.btn_volta_postgres.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_volta_postgres.setIcon(icon8)
        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 440, 991, 8))
        self.progressBar.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)
        self.paginas.addWidget(self.confirmacao)
        self.guarda = QWidget()
        self.guarda.setObjectName(u"guarda")
        self.btn_guarda_dump = QPushButton(self.guarda)
        self.btn_guarda_dump.setObjectName(u"btn_guarda_dump")
        self.btn_guarda_dump.setGeometry(QRect(470, 300, 150, 30))
        self.btn_guarda_dump.setMinimumSize(QSize(150, 30))
        self.btn_guarda_dump.setFont(font5)
        self.btn_guarda_dump.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_guarda_dump.setIcon(icon5)
        self.frame_title_wid_6 = QFrame(self.guarda)
        self.frame_title_wid_6.setObjectName(u"frame_title_wid_6")
        self.frame_title_wid_6.setGeometry(QRect(60, 150, 991, 35))
        self.frame_title_wid_6.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_6.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_6.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_6.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_5 = QLabel(self.frame_title_wid_6)
        self.labelBoxBlenderInstalation_5.setObjectName(u"labelBoxBlenderInstalation_5")
        self.labelBoxBlenderInstalation_5.setGeometry(QRect(9, 9, 201, 17))
        self.labelBoxBlenderInstalation_5.setFont(font1)
        self.labelBoxBlenderInstalation_5.setStyleSheet(u"")
        self.frame_div_content_2 = QFrame(self.guarda)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setGeometry(QRect(60, 190, 991, 81))
        self.frame_div_content_2.setMinimumSize(QSize(0, 50))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.caminho_base_importada = QLineEdit(self.frame_div_content_2)
        self.caminho_base_importada.setObjectName(u"caminho_base_importada")
        self.caminho_base_importada.setGeometry(QRect(10, 10, 791, 30))
        self.caminho_base_importada.setMinimumSize(QSize(0, 30))
        self.caminho_base_importada.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"color: rgb(98, 103, 111); ")
        self.labelVersion_5 = QLabel(self.frame_div_content_2)
        self.labelVersion_5.setObjectName(u"labelVersion_5")
        self.labelVersion_5.setGeometry(QRect(20, 50, 281, 16))
        self.labelVersion_5.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_procura_local = QPushButton(self.frame_div_content_2)
        self.btn_procura_local.setObjectName(u"btn_procura_local")
        self.btn_procura_local.setGeometry(QRect(810, 10, 171, 30))
        self.btn_procura_local.setMinimumSize(QSize(150, 30))
        self.btn_procura_local.setFont(font5)
        self.btn_procura_local.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_procura_local.setIcon(icon4)
        self.paginas.addWidget(self.guarda)
        self.conclusao = QWidget()
        self.conclusao.setObjectName(u"conclusao")
        self.frame_div_content_8 = QFrame(self.conclusao)
        self.frame_div_content_8.setObjectName(u"frame_div_content_8")
        self.frame_div_content_8.setGeometry(QRect(350, 40, 411, 500))
        self.frame_div_content_8.setMinimumSize(QSize(0, 500))
        self.frame_div_content_8.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_8.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_8.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_8.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_div_content_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(90, 70, 231, 61))
        self.label_9.setFont(font4)
        self.label_9.setStyleSheet(u"")
        self.label_9.setPixmap(QPixmap(u"imgs/logo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.btn_concluir = QPushButton(self.frame_div_content_8)
        self.btn_concluir.setObjectName(u"btn_concluir")
        self.btn_concluir.setGeometry(QRect(130, 340, 171, 30))
        self.btn_concluir.setMinimumSize(QSize(150, 30))
        self.btn_concluir.setFont(font5)
        self.btn_concluir.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/16x16/icons/16x16/cil-check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_concluir.setIcon(icon10)
        self.labelBoxBlenderInstalation_17 = QLabel(self.frame_div_content_8)
        self.labelBoxBlenderInstalation_17.setObjectName(u"labelBoxBlenderInstalation_17")
        self.labelBoxBlenderInstalation_17.setGeometry(QRect(100, 170, 231, 31))
        self.labelBoxBlenderInstalation_17.setFont(font6)
        self.labelBoxBlenderInstalation_17.setStyleSheet(u"")
        self.textBrowser_9 = QTextBrowser(self.frame_div_content_8)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(65, 250, 301, 81))
        self.textBrowser_9.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelBoxBlenderInstalation_18 = QLabel(self.frame_div_content_8)
        self.labelBoxBlenderInstalation_18.setObjectName(u"labelBoxBlenderInstalation_18")
        self.labelBoxBlenderInstalation_18.setGeometry(QRect(150, 200, 131, 31))
        self.labelBoxBlenderInstalation_18.setFont(font6)
        self.labelBoxBlenderInstalation_18.setStyleSheet(u"")
        self.paginas.addWidget(self.conclusao)

        self.verticalLayout_9.addWidget(self.paginas)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        migr.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)

        self.retranslateUi(migr)

        self.paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(migr)
    # setupUi

    def retranslateUi(self, migr):
        migr.setWindowTitle(QCoreApplication.translate("migr", u"MainWindow", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("migr", u"ASSISTENTE DE MIGRA\u00c7\u00c3O DE BANCO DE DADOS", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("migr", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("migr", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("migr", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText("")
        self.label_top_info_2.setText("")
        self.label_7.setText("")
        self.btn_vai_firebird.setText(QCoreApplication.translate("migr", u"Avan\u00e7ar", None))
        self.labelBoxBlenderInstalation_12.setText(QCoreApplication.translate("migr", u"BEM-VINDO AO ASSISTENTE", None))
        self.barrinha.setHtml(QCoreApplication.translate("migr", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dados importados no Banco de Dados de Destino:</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Centro de Custo, Departamento, Ramais, Contas, Troncos, Grupos de Troncos, Filtro de Liga\u00e7\u00f5es, Agenda, Planos, Oper"
                        "adoras, Hor\u00e1rios, Par\u00e2metros, Operador, Acessos, Identificadores de Entrada e Opcionais.</span></p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("migr", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">O Assistente de Migra\u00e7\u00e3o de Banco de Dados do SOMA Tarifador auxiliar\u00e1 na transfer\u00eancia de dados entre bases Firebird e PostgreSQL.</p></body></html>", None))
        self.labelBoxBlenderInstalation_13.setText(QCoreApplication.translate("migr", u"DE MIGRA\u00c7\u00c3O", None))
        self.caminho_gdb.setText("")
        self.caminho_gdb.setPlaceholderText(QCoreApplication.translate("migr", u"Caminho do Banco de Dados", None))
        self.labelVersion_3.setText(QCoreApplication.translate("migr", u"Ex: C:/Program Files (x86)/Tarifador/Dados/DADOS.GDB", None))
        self.btn_procura_gdb.setText(QCoreApplication.translate("migr", u"Abrir Local do Arquivo", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("migr", u"BANCO DE DADOS FIREBIRD", None))
        self.btn_vai_postgres.setText(QCoreApplication.translate("migr", u"Avan\u00e7ar", None))
        self.label_3.setText("")
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("migr", u"ASSISTENTE DE MIGRA\u00c7\u00c3O DE BANCO DE DADOS", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("migr", u"CONEX\u00c3O NO BANCO DE DADOS DE ORIGEM", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("migr", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Selecione o arquivo DADOS.GDB que ser\u00e1 utilizado como ORIGEM dos Dados.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Antes de Avan\u00e7ar, certifique-se de que a vers\u00e3o 2.5 do Firebird est\u00e1 instalado na sua m\u00e1quina.</p></body></html>", None))
        self.nome_nova_base.setText("")
        self.nome_nova_base.setPlaceholderText(QCoreApplication.translate("migr", u"Base zerada PostgreSQL", None))
        self.btn_cria_base.setText(QCoreApplication.translate("migr", u"Criar Base de Dados", None))
        self.pushButton_10.setText(QCoreApplication.translate("migr", u"Abrir Local do Arquivo", None))
        self.pushButton_11.setText(QCoreApplication.translate("migr", u"Processar", None))
        self.msg_banco_criado.setText(QCoreApplication.translate("migr", u"Base de Dados SOMASOLUCOES criada com sucesso!    ", None))
        self.icon_banco_criado.setText("")
        self.labelBoxBlenderInstalation_6.setText(QCoreApplication.translate("migr", u"CRIAR BASE DE DADOS", None))
        self.label_4.setText("")
        self.labelBoxBlenderInstalation_7.setText(QCoreApplication.translate("migr", u"ASSISTENTE DE MIGRA\u00c7\u00c3O DE BANCO DE DADOS", None))
        self.labelBoxBlenderInstalation_8.setText(QCoreApplication.translate("migr", u"CONEX\u00c3O NO BANCO DE DADOS DE DESTINO", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("migr", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Crie a Base de Dados que ser\u00e1 utilizada para o DESTINO dos Dados.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Em seguida, importe a base zerada do SOMA Tarifador.</p></body></html>", None))
        self.btn_vai_confirmacao.setText(QCoreApplication.translate("migr", u"Avan\u00e7ar", None))
        self.btn_volta_firebird.setText(QCoreApplication.translate("migr", u"Anterior", None))
        self.labelBoxBlenderInstalation_11.setText(QCoreApplication.translate("migr", u"IMPORTAR BASE ZERADA", None))
        self.caminho_base_zerada.setText("")
        self.caminho_base_zerada.setPlaceholderText(QCoreApplication.translate("migr", u"Caminho da Base de Dados", None))
        self.btn_busca_dump.setText(QCoreApplication.translate("migr", u"Abrir Local do Arquivo", None))
        self.btn_zera_base.setText(QCoreApplication.translate("migr", u"Importar", None))
        self.msg_base_importada.setText(QCoreApplication.translate("migr", u"Base de Dados importada com sucesso!", None))
        self.icon_base_importada.setText("")
        self.confirmar.setHtml(QCoreApplication.translate("migr", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BANCO DE DADOS DE ORIGEM (Firebird)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Diret\u00f3rio de Origem: C:\\Program Files (x86)\\Tarifador\\Dados\\DADOS.GDB</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-------------------------------------------------------------</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BANCO DE DADOS DE DESTINO (PostgreSQL)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Base de Dados de Destino: SOMASOLUCOES</p></body></html>", None))
        self.labelBoxBlenderInstalation_14.setText(QCoreApplication.translate("migr", u"CONFIRMA\u00c7\u00c3O DOS DADOS", None))
        self.labelBoxBlenderInstalation_15.setText(QCoreApplication.translate("migr", u"ASSISTENTE DE MIGRA\u00c7\u00c3O DE BANCO DE DADOS", None))
        self.labelBoxBlenderInstalation_16.setText(QCoreApplication.translate("migr", u"PRONTO PARA MIGRAR", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("migr", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">O Assistente est\u00e1 pronto para realizar a migra\u00e7\u00e3o entre as bases de dados. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Antes de Processar, apenas confirme os dados abaixo.</p></body></html>", None))
        self.btn_processar.setText(QCoreApplication.translate("migr", u"Processar", None))
        self.label_8.setText("")
        self.btn_volta_postgres.setText(QCoreApplication.translate("migr", u"Anterior", None))
        self.btn_guarda_dump.setText(QCoreApplication.translate("migr", u"Avan\u00e7ar", None))
        self.labelBoxBlenderInstalation_5.setText(QCoreApplication.translate("migr", u"DESTINO DA BASE IMPORTADA", None))
        self.caminho_base_importada.setText("")
        self.caminho_base_importada.setPlaceholderText(QCoreApplication.translate("migr", u"Destino do dump da nova base", None))
        self.labelVersion_5.setText(QCoreApplication.translate("migr", u"Ex: C:/Users/Usuario/Desktop", None))
        self.btn_procura_local.setText(QCoreApplication.translate("migr", u"Selecionar Local", None))
        self.label_9.setText("")
        self.btn_concluir.setText(QCoreApplication.translate("migr", u"Concluir", None))
        self.labelBoxBlenderInstalation_17.setText(QCoreApplication.translate("migr", u"MIGRA\u00c7\u00c3O DE DADOS", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("migr", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">O Assistente concluiu a migra\u00e7\u00e3o de dados entre as bases Firebird e PostgreSQL.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Clique em Concluir para finalizar o Assistente.</p></body></html>", None))
        self.labelBoxBlenderInstalation_18.setText(QCoreApplication.translate("migr", u"CONCLU\u00cdDA!", None))
        self.label_credits.setText(QCoreApplication.translate("migr", u"Desenvolvido por SOMA Solu\u00e7\u00f5es", None))
        self.label_version.setText(QCoreApplication.translate("migr", u"v1.0.0", None))
    # retranslateUi

