from View.level_controller import LevelController
from PySide.QtGui import QDesktopWidget, QMainWindow

class GalagaEsque(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle('Galaga-Esque')
        self.level_controller = LevelController(self)
        self.level_controller.run()
            
        self.showFullScreen()