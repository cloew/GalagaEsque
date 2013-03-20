from board import Board
from PySide.QtGui import QDesktopWidget, QMainWindow

class GalagaEsque(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('Galaga-Esque')
        self.board = Board(self)

        self.setCentralWidget(self.board)

        #self.statusbar = self.statusBar()
            
        self.board.start()
        self.center()
        self.showFullScreen()

    def center(self):
        
        screen = QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)