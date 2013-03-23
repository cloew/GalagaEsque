from PySide.QtCore import QBasicTimer, QRect, Qt
from PySide.QtGui import QApplication, QColor, QFont, QFrame, QImage, QLabel, QPainter, QPushButton, QStyle, QStyleOptionButton, QWidget

from background_view import BackgroundView
from enemy_ship_view import EnemyShipView
from hero_ship_view import HeroShipView
from laser_view import LaserView

class LevelView(QFrame):
    """ Represents the View of the Level """

    def __init__(self, parent, level):
        """ Initialize the Level View """
        QFrame.__init__(self, parent)

        self.level = level
        self.background = BackgroundView()
        self.enemy_view = EnemyShipView(self.level.enemy)
        self.ship_view = HeroShipView(self.level.ship)
        self.laser_views = []

        self.setFocusPolicy(Qt.StrongFocus)

    def paintEvent(self, event):
        """ Paint the ship """
        painter = QPainter(self)
        
        self.background.draw(painter, self)
        self.drawLasers(painter)
        self.ship_view.draw(painter, self)
        self.enemy_view.draw(painter, self)
        if not self.level.over:
            self.drawScore(painter)
        else:
            self.drawGameOver(painter)
        
    def drawScore(self, painter):
        """ Draw the score label """
        font = QFont()
        font.setPointSize(24)
        penColor = QColor(238, 250, 12)
        
        painter.setFont(font)
        painter.setPen(penColor)
        painter.drawText(10, 50, "Score: {0:,}".format(self.level.score))
        
    def drawGameOver(self, painter):
        """ Draw the game over """
        font = QFont()
        font.setPointSize(48)
        penColor = QColor(255, 0, 0)
        
        painter.setFont(font)
        painter.setPen(penColor)
        painter.drawText(self.contentsRect(), Qt.AlignCenter, "Game Over")
        
    def drawLasers(self, painter):
        """ Draw Lasers """
        for laser_view in self.laser_views:
            if laser_view.laser not in self.level.lasers:
                self.laser_views.remove(laser_view)
            else:
                laser_view.draw(painter, self)
        
    def addLaser(self):
        """ Add a laser to the screen """
        for laser in self.level.lasers:
            for laser_view in self.laser_views:
                if laser_view.laser is laser:
                    None
            else:
                self.laser_views.append(LaserView(laser))