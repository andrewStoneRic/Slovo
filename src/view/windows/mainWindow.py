import logging as log

from PySide6.QtWidgets import QMainWindow, QAbstractButton, QPushButton
from PySide6.QtGui import QIcon, QCursor

from ..generated.ui_mainWindow import Ui_MainWindow

from ..widgets.languagePopup import LanguagePopup
from ..widgets.dashboard import Dashboard

from ..utils.renderIcons import render_svg_icon_color

class MainWindow(QMainWindow):
    """"""
    def __init__(self):
        """"""
        super().__init__()
        
        log.info("Инициализация UI главного окна")
        self.ui = Ui_MainWindow()
        
        log.info("Настройка основных параметров UI главного окна")
        self.ui.setupUi(self)

        log.info("Инициализация стека виджета рабочего пространства")
        self.initStackedWidget()

        log.info("Настройка кнопок иструментов")
        self.setupToolButtons()
        
        log.info("Инициализация темы")
        self.initStylesSheet()
   
    def initStackedWidget(self):
        """Настройка стека виджетов"""

        dashboard = Dashboard()
        self.ui.workspaceStackedWidget.addWidget(dashboard)

    def setupToolButtons(self):
        """Устанавливает вид кнопок инструментов"""
        
        checkedBtn = self.ui.toolButtonGroup.checkedButton()
        if checkedBtn is not None:
            current_icon = render_svg_icon_color(checkedBtn.property("icon_path"), "#23D223")
            checkedBtn.setIcon(current_icon)
        else:
            log.error("Нету выбранной кнопки!")

    def make_icon_of_check_btn_current(self, btn: QPushButton):
        """Делает иконку проверяемой кнопки выбранной"""
        
        log.info("Перекраска кнопки в выбраный цвет")
        current_icon = render_svg_icon_color(btn.property("icon_path"), "#23D223")
        btn.setIcon(current_icon)
             
    def make_icon_of_check_btn_normal(self, btn: QPushButton): 
        """Делает иконку проверяемой кнопки нормальной"""
        
        log.info("Возвращение кнопки в нормальный цвет")
        normal_icon = QIcon(btn.property("icon_path"))
        btn.setIcon(normal_icon)

    def show_LanguagePopup(self):
        """Показ плавующего окна для смены языка"""

        log.info("Установка координат для плавующего окна")
        pos_cursor = QCursor().pos()

        x, y = pos_cursor.x(), pos_cursor.y()
        
        log.info("Инициализация плавующего окна")
        popup = LanguagePopup(self)

        # Вычитание для того, чтобы окно было над курсором, а не под ним 
        popup.move(x, y - popup.height())
        popup.show()

    def show_home(self):
        """Показ дома"""
        
        log.info("Смена workplace на дом")
        self.ui.workspaceStackedWidget.setCurrentIndex(0)

    def show_dashboard(self):
        """Показ дашборда"""
        
        log.info("Смена workplace на дашборд")
        self.ui.workspaceStackedWidget.setCurrentIndex(1)

    def initStylesSheet(self, theme='light'):
        """Недоработано"""
        
        log.debug("Окрытие файла стилей")
        with open("res/styles/light.qss") as theme:
            log.debug("Чтение QSS")
            theme = theme.read()
        
        log.info("Установка темы")
        self.setStyleSheet(theme)
    
