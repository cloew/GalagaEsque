from PySide.QtCore import Qt
from PySide.QtGui import QImage, QMatrix

from Game.Core.game_engine import TheGameEngine
from Game.Core.game_object_rectangle import GameObjectRectangle

class Laser:
    """ Represents a Laser in the Galaga Game """

    def __init__(self, parent_ship):
        """ Create the laser """
        self.rectangle = GameObjectRectangle(.5, 5)

        self.rectangle.setCenterX(parent_ship.rectangle.getCenterX())
        self.rectangle.setBottom(parent_ship.rectangle.top())

        self.xVelocity = 0
        self.yVelocity = -1

    def timer(self):
        """ Handle a timer event """
        self.tryMove(self.rectangle.x+self.xVelocity, self.rectangle.y+self.yVelocity)
        
    def offScreen(self):
        """ Return if the laser is off the screen """
        return self.rectangle.bottom() <= 0

    def tryMove(self, newX, newY):
        """ Try to move the ship to a new location """
        self.rectangle.x = newX
        self.rectangle.y = newY
        TheGameEngine.updateUI()