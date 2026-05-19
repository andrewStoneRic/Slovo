# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from . import mainWindow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 520)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listAndToolsAndSettingsWidget = QWidget(self.centralwidget)
        self.listAndToolsAndSettingsWidget.setObjectName(u"listAndToolsAndSettingsWidget")
        self.verticalLayout = QVBoxLayout(self.listAndToolsAndSettingsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolsWidget = QWidget(self.listAndToolsAndSettingsWidget)
        self.toolsWidget.setObjectName(u"toolsWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.toolsWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.wordsListViewButton = QPushButton(self.toolsWidget)
        self.toolButtonGroup = QButtonGroup(MainWindow)
        self.toolButtonGroup.setObjectName(u"toolButtonGroup")
        self.toolButtonGroup.addButton(self.wordsListViewButton)
        self.wordsListViewButton.setObjectName(u"wordsListViewButton")
        font = QFont()
        font.setFamilies([u"Sans Serif"])
        self.wordsListViewButton.setFont(font)
        self.wordsListViewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/light_image/image/light/light_add_box.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wordsListViewButton.setIcon(icon)
        self.wordsListViewButton.setIconSize(QSize(40, 40))
        self.wordsListViewButton.setCheckable(True)
        self.wordsListViewButton.setChecked(True)
        self.wordsListViewButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.wordsListViewButton)

        self.chunksListViewButton = QPushButton(self.toolsWidget)
        self.toolButtonGroup.addButton(self.chunksListViewButton)
        self.chunksListViewButton.setObjectName(u"chunksListViewButton")
        self.chunksListViewButton.setFont(font)
        self.chunksListViewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/light_image/image/light/light_cube.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.chunksListViewButton.setIcon(icon1)
        self.chunksListViewButton.setIconSize(QSize(40, 40))
        self.chunksListViewButton.setCheckable(True)
        self.chunksListViewButton.setChecked(False)
        self.chunksListViewButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.chunksListViewButton)

        self.contextListViewButton = QPushButton(self.toolsWidget)
        self.toolButtonGroup.addButton(self.contextListViewButton)
        self.contextListViewButton.setObjectName(u"contextListViewButton")
        self.contextListViewButton.setFont(font)
        self.contextListViewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/light_image/image/light/light_liblary_books.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contextListViewButton.setIcon(icon2)
        self.contextListViewButton.setIconSize(QSize(40, 40))
        self.contextListViewButton.setCheckable(True)
        self.contextListViewButton.setChecked(False)
        self.contextListViewButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.contextListViewButton)

        self.favouriteListViewButton = QPushButton(self.toolsWidget)
        self.toolButtonGroup.addButton(self.favouriteListViewButton)
        self.favouriteListViewButton.setObjectName(u"favouriteListViewButton")
        self.favouriteListViewButton.setFont(font)
        self.favouriteListViewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/light_image/image/light/light_bookmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.favouriteListViewButton.setIcon(icon3)
        self.favouriteListViewButton.setIconSize(QSize(40, 40))
        self.favouriteListViewButton.setCheckable(True)
        self.favouriteListViewButton.setChecked(False)
        self.favouriteListViewButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.favouriteListViewButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.plusElementViewButton = QPushButton(self.toolsWidget)
        self.plusElementViewButton.setObjectName(u"plusElementViewButton")
        self.plusElementViewButton.setFont(font)
        self.plusElementViewButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/light_image/image/light/light_add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.plusElementViewButton.setIcon(icon4)
        self.plusElementViewButton.setIconSize(QSize(40, 40))
        self.plusElementViewButton.setCheckable(False)
        self.plusElementViewButton.setChecked(False)
        self.plusElementViewButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.plusElementViewButton)


        self.verticalLayout.addWidget(self.toolsWidget)

        self.listWidget = QWidget(self.listAndToolsAndSettingsWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.verticalLayout_2 = QVBoxLayout(self.listWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.listWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 362, 334))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.listWidget)

        self.settingsWidget = QWidget(self.listAndToolsAndSettingsWidget)
        self.settingsWidget.setObjectName(u"settingsWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.settingsWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.changeLanguageButton = QPushButton(self.settingsWidget)
        self.changeLanguageButton.setObjectName(u"changeLanguageButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeLanguageButton.sizePolicy().hasHeightForWidth())
        self.changeLanguageButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Sans Serif"])
        font1.setPointSize(20)
        font1.setHintingPreference(QFont.PreferDefaultHinting)
        self.changeLanguageButton.setFont(font1)
        self.changeLanguageButton.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.changeLanguageButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/light_image/image/light/light_expand_all.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.changeLanguageButton.setIcon(icon5)
        self.changeLanguageButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.changeLanguageButton)

        self.helpButton = QPushButton(self.settingsWidget)
        self.helpButton.setObjectName(u"helpButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u":/light_image/image/light/light_help.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpButton.setIcon(icon6)
        self.helpButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.helpButton)

        self.settingsButton = QPushButton(self.settingsWidget)
        self.settingsButton.setObjectName(u"settingsButton")
        icon7 = QIcon()
        icon7.addFile(u":/light_image/image/light/light_settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsButton.setIcon(icon7)
        self.settingsButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.settingsButton)


        self.verticalLayout.addWidget(self.settingsWidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 13)
        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.listAndToolsAndSettingsWidget)

        self.workspaceWidget = QWidget(self.centralwidget)
        self.workspaceWidget.setObjectName(u"workspaceWidget")
        self.workspaceWidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.workspaceWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.topVerticalSpacer = QSpacerItem(20, 166, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.topVerticalSpacer)

        self.createWordButton = QPushButton(self.workspaceWidget)
        self.createWordButton.setObjectName(u"createWordButton")
        font2 = QFont()
        font2.setPointSize(20)
        self.createWordButton.setFont(font2)
        self.createWordButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createWordButton.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.createWordButton)

        self.createChunkButton = QPushButton(self.workspaceWidget)
        self.createChunkButton.setObjectName(u"createChunkButton")
        self.createChunkButton.setFont(font2)
        self.createChunkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.createChunkButton)

        self.createContextButton = QPushButton(self.workspaceWidget)
        self.createContextButton.setObjectName(u"createContextButton")
        self.createContextButton.setFont(font2)
        self.createContextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.createContextButton)

        self.searchButton = QPushButton(self.workspaceWidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setFont(font2)
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.searchButton)

        self.bottomVerticalSpacer = QSpacerItem(20, 166, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.bottomVerticalSpacer)


        self.horizontalLayout.addWidget(self.workspaceWidget)

        self.actionWidget = QWidget(self.centralwidget)
        self.actionWidget.setObjectName(u"actionWidget")

        self.horizontalLayout.addWidget(self.actionWidget)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 14)
        self.horizontalLayout.setStretch(2, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.wordsListViewButton.setText("")
        self.wordsListViewButton.setProperty(u"icon_path", QCoreApplication.translate("MainWindow", u":/light_image/image/light/light_add_box.svg", None))
        self.chunksListViewButton.setText("")
        self.chunksListViewButton.setProperty(u"icon_path", QCoreApplication.translate("MainWindow", u":/light_image/image/light/light_cube.svg", None))
        self.contextListViewButton.setText("")
        self.contextListViewButton.setProperty(u"icon_path", QCoreApplication.translate("MainWindow", u":/light_image/image/light/light_liblary_books.svg", None))
        self.favouriteListViewButton.setText("")
        self.favouriteListViewButton.setProperty(u"icon_path", QCoreApplication.translate("MainWindow", u":/light_image/image/light/light_bookmark.svg", None))
        self.plusElementViewButton.setText("")
        self.changeLanguageButton.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.helpButton.setText("")
        self.settingsButton.setText("")
        self.createWordButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0441\u043b\u043e\u0432\u043e", None))
        self.createChunkButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0447\u0430\u043d\u043a", None))
        self.createContextButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u043d\u0442\u0435\u043a\u0441\u0442", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi

