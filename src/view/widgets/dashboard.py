import logging as log

from PySide6.QtWidgets import QWidget

from ..generated.ui_dashboard import Ui_dashboard

class Dashboard(QWidget):
    """Виджет дашборда в главном окне"""

    def __init__(self):
        
        super().__init__()

        log.info("Инициализация дашборда")
        self.ui = Ui_dashboard()
        
        log.info("Настройка основных параметров UI дашборда")
        self.ui.setupUi(self)

