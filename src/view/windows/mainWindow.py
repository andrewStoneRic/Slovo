import logging as log

from PySide6.QtWidgets import QMainWindow, QAbstractButton, QPushButton
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QCursor

from ..generated.ui_mainWindow import Ui_MainWindow

from ..widgets.languagePopup import LanguagePopup

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
        
        log.info("Настройка сигналов кнопок")
        self.setupSignalsButtons()
        
        log.info("Инициализация темы")
        self.initStylesSheet()
    
    def setupSignalsButtons(self):
        """Устанавливает сигналы для кнопок"""

        log.info("Настройка кнопок иструментов")
        self.setupToolButtons()
        
        log.info("Настройка сигнала при нажатии на кнопку изменения языка")
        self.ui.changeLanguageButton.clicked.connect(self.view_LanguagePopup)


    def setupToolButtons(self):
        """Устанавливает поведение и вид кнопок инструментов"""
        
        checkedBtn = self.ui.toolButtonGroup.checkedButton()
        if checkedBtn is not None:
            current_icon = render_svg_icon_color(checkedBtn.property("icon_path"), "#23D223")
            checkedBtn.setIcon(current_icon)
        else:
            log.error("Нету выбранной кнопки!")

        self.ui.toolButtonGroup.buttonToggled.connect(self.on_toolButtonGroup_toggled)
    
    @Slot(QAbstractButton, bool) 
    def on_toolButtonGroup_toggled(self, btn: QPushButton, checked: bool):
        """Проявление действия при нажатии или разжатии кнопки инструмента"""

        if checked:
            log.info(f"Кнопка {btn} - активирована")
            self.make_icon_of_check_btn_current(btn)
        else:
            log.info(f"Кнопка {btn} - выключена")
            self.make_icon_of_check_btn_normal(btn)

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

    def view_LanguagePopup(self):
        """Показ плавующего окна для смены языка"""

        log.info("Установка координат для плавоющего окна")
        pos_cursor = QCursor().pos()

        x, y = pos_cursor.x(), pos_cursor.y()
        
        log.info("Инициализация плавующего окна")
        popup = LanguagePopup(self)

        # Вычитание для того, чтобы окно было над курсором, а не под ним 
        popup.move(x, y - popup.height())
        popup.show()

    def initStylesSheet(self, theme='light'):
        """Недоработано"""
        
        log.debug("Окрытие файла стилей")
        with open("res/styles/light.qss") as theme:
            log.debug("Чтение QSS")
            theme = theme.read()
        
        log.info("Установка темы")
        self.setStyleSheet(theme)
    
