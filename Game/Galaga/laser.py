from PySide.QtCore import Qt
from PySide.QtGui import QImage, QMatrix

from Game.Core.game_engine import TheGameEngine
from Game.Core.game_object_rectangle import GameObjectRectangle

class Laser:
    """ Represents a Laser in the Galaga Game """

    def __init__(self):
        """ Create the hero ship """
        self.rectangle = GameObjectRectangle(.5, 5)

        self.rectangle.setCenterX(50)
        self.rectangle.setCenterY(50)

        self.xVelocity = 0
        self.yVelocity = 0

    def timer(self):
        """ Handle a timer event """
        self.tryMove(self.rectangle.x+self.xVelocity, self.rectangle.y+self.yVelocity)

    def tryMove(self, newX, newY):
        """ Try to move the ship to a new location """
        self.rectangle.x = self.getValidPosition(newX, self.rectangle.width)
        self.rectangle.y = self.getValidPosition(newY, self.rectangle.height)
        TheGameEngine.updateUI()

    def getValidPosition(self, newPosition, laserSize):
        """ Return if the new Position is a valid Position """
        if newPosition < 0:
            return 0
        elif newPosition + laserSize > 100:
            return 100 - laserSize
        else:
            return newPosition
