from View.level_view import LevelView
from PySide.QtGui import QDesktopWidget, QMainWindow

class GalagaEsque(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('Galaga-Esque')
        self.level = LevelView(self)

        self.setCentralWidget(self.level)

        #self.statusbar = self.statusBar()
            
        self.level.start()
        self.center()
        self.showFullScreen()

    def center(self):
        
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)