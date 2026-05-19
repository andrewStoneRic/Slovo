from model.appModel import AppModel
from view.windows.mainWindow import MainWindow

class MainController:
    """"""
    
    def __init__(self):
        """"""
        
        self._model = AppModel()


        self.mainWindow = MainWindow()
        self.mainWindow.show()

        
    
    
