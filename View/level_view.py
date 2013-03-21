from PySide.QtCore import QBasicTimer, Qt
from PySide.QtGui import QFrame, QPainter, QWidget

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