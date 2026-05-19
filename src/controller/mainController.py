from model.appModel import AppModel
from .mainWindowController import MainWindowController
from view.windows.mainWindow import MainWindow

class MainController:
    """Главный контроллер"""
    
    def __init__(self):
        self._model = AppModel()

        self.mainWindow = MainWindow()
        self.mainWindow.show()

        self.mainWindowController = MainWindowController(self._model, self.mainWindow)
        self.mainWindowController.setupConnection()


