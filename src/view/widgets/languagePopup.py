import logging as log

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt

from ..generated.ui_languagePopup import Ui_languagePopup

class LanguagePopup(QWidget):
    """Класс плавоещего меню для смены языка"""

    def __init__(self, parent=None):
        
        super().__init__(parent)

        log.info("Инициализация плавующего окна для смены языка")
        self.ui = Ui_languagePopup()
        
        log.info("Настройка основных параметров UI плавующего окна для смены языка")
        self.ui.setupUi(self)

        log.info("Настройка атрибутов плавующего окна")
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
