
from PySide.QtCore import Qt
from PySide.QtGui import QImage, QMatrix

from Game.Core.game_engine import TheGameEngine
from Game.Core.game_object_rectangle import GameObjectRectangle

class EnemyShip:
    """ Enemy Ship """
    MAX_SPEED = .2
    MIN_SPEED = -.2

    def __init__(self):
        """ Create the hero ship """
        self.rectangle = GameObjectRectangle(5, 10)

        self.rectangle.setCenterX(50)
        self.rectangle.setCenterY(10)

        self.xVelocity = EnemyShip.MIN_SPEED
        self.yVelocity = 0

    def timer(self):
        """ Handle a timer event """
        self.tryMove(self.rectangle.x+self.xVelocity, self.rectangle.y+self.yVelocity)

    def tryMove(self, newX, newY):
        """ Try to move the ship to a new location """
        self.rectangle.x = self.getValidPosition(newX, self.rectangle.width)
        self.rectangle.y = self.getValidPosition(newY, self.rectangle.height)
        TheGameEngine.updateUI()

    def getValidPosition(self, newPosition, shipSize):
        """ Return if the new Position is a valid Position """
        if newPosition < 0:
            self.xVelocity = EnemyShip.MAX_SPEED
            return 0
        elif newPosition + shipSize > 100:
            self.xVelocity = EnemyShip.MIN_SPEED
            return 100 - shipSize
        else:
            return newPosition
