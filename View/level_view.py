from PySide.QtCore import QBasicTimer, Qt
from PySide.QtGui import QFrame, QPainter, QWidget

from Game.Core.game_engine import TheGameEngine
from hero_ship_view import HeroShipView

class LevelView(QFrame):
    """ Represents the View of the Level """

    def __init__(self, parent, level):
        """ Initialize the Level View """
        QFrame.__init__(self, parent)

        self.level = level
        self.ship_view = HeroShipView(self.level.ship)

        self.setFocusPolicy(Qt.StrongFocus)

    def paintEvent(self, event):
        """ Paint the ship """
        painter = QPainter(self)
        self.ship_view.draw(painter, self)

    def keyPressEvent(self, event):
        """ Process Keys """
        key = event.key()
        
        if key == Qt.Key_Left:
            self.level.ship.left(self.contentsRect().width(), self.contentsRect().height())
        elif key == Qt.Key_Right:
            self.level.ship.right(self.contentsRect().width(), self.contentsRect().height())
        elif key == Qt.Key_Down:
            self.level.ship.down(self.contentsRect().width(), self.contentsRect().height())
        elif key == Qt.Key_Up:
            self.level.ship.up(self.contentsRect().width(), self.contentsRect().height())
        else:
            QWidget.keyPressEvent(self, event)

        if self.level.ship.update:
            self.update()

    def keyReleaseEvent(self, event):
        """ Process Keys """
        key = event.key()
        
        if key == Qt.Key_Left:
            self.level.ship.releaseLeft()
        elif key == Qt.Key_Right:
            self.level.ship.releaseRight()
        elif key == Qt.Key_Down:
            self.level.ship.releaseDown()
        elif key == Qt.Key_Up:
            self.level.ship.releaseUp()
        else:
            QWidget.keyPressEvent(self, event)

        if self.level.ship.update:
            self.update()