from View.level_controller import LevelController
from PySide.QtGui import QDesktopWidget, QMainWindow

class GalagaEsque(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('Galaga-Esque')
        self.level_controller = LevelController(self)
        self.level_controller.run()
            
        #self.level.start()
        self.showFullScreen()

    def center(self):
        
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)