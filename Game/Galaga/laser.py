from PySide.QtCore import Qt
from PySide.QtGui import QImage, QMatrix

from Game.Core.game_engine import TheGameEngine
from Game.Core.game_object_rectangle import GameObjectRectangle

class Laser:
    """ Represents a Laser in the Galaga Game """

    def __init__(self, x, y):
        """ Create the hero ship """
        self.rectangle = GameObjectRectangle(.5, 5)

        self.rectangle.setCenterX(x)
        self.rectangle.setCenterY(y)

        self.xVelocity = 0
        self.yVelocity = -1

    def timer(self):
        """ Handle a timer event """
        self.tryMove(self.rectangle.x+self.xVelocity, self.rectangle.y+self.yVelocity)

    def tryMove(self, newX, newY):
        """ Try to move the ship to a new location """
        self.rectangle.x = newX
        self.rectangle.y = newY
        TheGameEngine.updateUI()