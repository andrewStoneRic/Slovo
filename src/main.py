import sys
import logging as log

from PySide6.QtWidgets import QApplication

log.basicConfig(level=log.INFO)

from controller.mainController import MainController

if __name__ == "__main__":
    
    log.info("Запуск приложения")
    app = QApplication(sys.argv)
    
    log.info("Запуск контроллера")
    controller = MainController()
    
    app.exec()
    
