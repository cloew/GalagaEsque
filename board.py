from PySide.QtCore import QBasicTimer, Qt
from PySide.QtGui import QFrame, QPainter, QWidget

from game_engine import TheGameEngine
from hero_ship import HeroShip
from hero_ship_view import HeroShipView

class Board(QFrame):
    
    BoardWidth = 10
    BoardHeight = 10
    Speed = 20

    def __init__(self, parent):
        super(Board, self).__init__()

        self.ship = HeroShip()
        self.ship_view = HeroShipView(self.ship)

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False


    def squareWidth(self):
        return self.contentsRect().width() / Board.BoardWidth

    def squareHeight(self):
        return self.contentsRect().height() / Board.BoardHeight

    def start(self):
        if self.isPaused:
            return
        self.isStarted = True

        TheGameEngine.start(self)

    def pause(self):
        
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        
        if self.isPaused:
            self.timer.stop()
        else:
            self.timer.start(Board.Speed, self)

        self.update()

    def paintEvent(self, event):
        """ Paint the ship """
        painter = QPainter(self)
        self.ship_view.draw(painter, self)

    def keyPressEvent(self, event):
        """ Process Keys """
        if not self.isStarted:
            QWidget.keyPressEvent(self, event)
            return

        key = event.key()
        
        if key == Qt.Key_P:
            self.pause()
            return
        if self.isPaused:
            return
        elif key == Qt.Key_Left:
            self.ship.left(self.contentsRect().width(), self.contentsRect().height())
        elif key == Qt.Key_Right:
            self.ship.right(self.contentsRect().width(), self.contentsRect().height())
        elif key == Qt.Key_Down:
            self.ship.down(self.contentsRect().width(), self.contentsRect().height())
        elif key == Qt.Key_Up:
            self.ship.up(self.contentsRect().width(), self.contentsRect().height())
        else:
            QWidget.keyPressEvent(self, event)

        if self.ship.update:
            self.update()

    def keyReleaseEvent(self, event):
        """ Process Keys """
        if not self.isStarted:
            QWidget.keyPressEvent(self, event)
            return

        key = event.key()
        
        if key == Qt.Key_Left:
            self.ship.releaseLeft()
        elif key == Qt.Key_Right:
            self.ship.releaseRight()
        elif key == Qt.Key_Down:
            self.ship.releaseDown()
        elif key == Qt.Key_Up:
            self.ship.releaseUp()
        else:
            QWidget.keyPressEvent(self, event)

        if self.ship.update:
            self.update()

    def timerEvent(self, event):
        self.ship.timer(self.contentsRect().width(), self.contentsRect().height())
        if event.timerId() == self.timer.timerId():
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
            self.update()
        else:
            QFrame.timerEvent(self, event)

    def callback(self, width, height):
        self.ship.timer()
        self.update()