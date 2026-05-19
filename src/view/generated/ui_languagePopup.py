# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'languagePopup.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_languagePopup(object):
    def setupUi(self, languagePopup):
        if not languagePopup.objectName():
            languagePopup.setObjectName(u"languagePopup")
        languagePopup.resize(389, 296)
        languagePopup.setStyleSheet(u"#languagePopup {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"#frame {\n"
"	border: 2px solid rgb(0, 0, 0);\n"
"	border-radius: 12px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(languagePopup)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(languagePopup)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_2.addWidget(self.frame_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(languagePopup)

        QMetaObject.connectSlotsByName(languagePopup)
    # setupUi

    def retranslateUi(self, languagePopup):
        languagePopup.setWindowTitle(QCoreApplication.translate("languagePopup", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("languagePopup", u"PushButton", None))
    # retranslateUi

