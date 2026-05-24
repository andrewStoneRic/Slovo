import logging as log

from PySide6.QtWidgets import QAbstractButton, QPushButton
from PySide6.QtCore import Slot

from view.windows.mainWindow import MainWindow

class MainWindowController:
    """Контроллер главного окна"""

    def __init__(self, _model, mainWindow: MainWindow):
        self.model = _model
        self.view = mainWindow

    def setupConnection(self):
        """Настраивает соединения с кнопками главного окна"""
        
        self.view.ui.toolButtonGroup.buttonToggled.connect(self.on_toolButtonGroup_toggled)

        log.info("Настройка сигнала при нажатии на кнопку изменения языка")
        self.view.ui.changeLanguageButton.clicked.connect(self.view.show_LanguagePopup)

        log.info("Настройка сигнала при нажатии на кнопку дашборда из панели активностей")
        self.view.ui.dashboardButton.clicked.connect(self.view.show_dashboard)

        log.info("Настройка сигнала при нажатии на кнопку дома из панели активностей")
        self.view.ui.homeButton.clicked.connect(self.view.show_home)

    @Slot(QAbstractButton, bool) 
    def on_toolButtonGroup_toggled(self, btn: QPushButton, checked: bool):
        """Проявление действия при нажатии или разжатии кнопки инструмента"""

        if checked:
            log.info(f"Кнопка {btn} - активирована")
            self.view.make_icon_of_check_btn_current(btn)
        else:
            log.info(f"Кнопка {btn} - выключена")
            self.view.make_icon_of_check_btn_normal(btn)

