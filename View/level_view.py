from PySide.QtCore import QBasicTimer, Qt
from PySide.QtGui import QFrame, QImage, QPainter, QWidget

from background_view import BackgroundView
from enemy_ship_view import EnemyShipView
from hero_ship_view import HeroShipView

class LevelView(QFrame):
    """ Represents the View of the Level """

    def __init__(self, parent, level):
        """ Initialize the Level View """
        QFrame.__init__(self, parent)

        self.level = level
        self.background = BackgroundView()
        self.enemy_view = EnemyShipView(self.level.enemy)
        self.ship_view = HeroShipView(self.level.ship)

        self.setFocusPolicy(Qt.StrongFocus)

    def paintEvent(self, event):
        """ Paint the ship """
        painter = QPainter(self)
        self.background.draw(painter, self)
        self.ship_view.draw(painter, self)
        self.enemy_view.draw(painter, self)