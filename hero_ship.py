from PySide.QtCore import Qt
from PySide.QtGui import QImage, QMatrix

from game_object_rectangle import GameObjectRectangle

class HeroShip:
    """ Hero Ship """
    MAX_SPEED = 5
    MIN_SPEED = -5

    def __init__(self, squareSize):
        """ Create the hero ship """
        self.rectangle = GameObjectRectangle(10, 10)

        self.xVelocity = 0
        self.yVelocity = 0

        self.update = False

    def timer(self):
        """ Handle a timer event """
        self.tryMove(self.rectangle.x+self.xVelocity, self.rectangle.y+self.yVelocity)

    def up(self, maxX, maxY):
        """ Move the ship Up """
        self.yVelocity = self.getNewVelocity(self.yVelocity, self.MIN_SPEED)

    def down(self, maxX, maxY):
        """ Move the ship Down """
        self.yVelocity = self.getNewVelocity(self.yVelocity, self.MAX_SPEED)

    def left(self, maxX, maxY):
        """ Move the ship Left """
        self.xVelocity = self.getNewVelocity(self.xVelocity, self.MIN_SPEED)

    def right(self, maxX, maxY):
        """ Move the ship Right """
        self.xVelocity = self.getNewVelocity(self.xVelocity, self.MAX_SPEED)

    def releaseUp(self):
        """ Move the ship Up """
        self.yVelocity = self.getNewVelocity(self.yVelocity, self.MAX_SPEED)

    def releaseDown(self):
        """ Move the ship Down """
        self.yVelocity = self.getNewVelocity(self.yVelocity, self.MIN_SPEED)

    def releaseLeft(self):
        """ Move the ship Left """
        self.xVelocity = self.getNewVelocity(self.xVelocity, self.MAX_SPEED)

    def releaseRight(self):
        """ Move the ship Right """
        self.xVelocity = self.getNewVelocity(self.xVelocity, self.MIN_SPEED)

    def getNewVelocity(self, velocity, change):
        """  """
        newVelocity = velocity + change
        if newVelocity > self.MAX_SPEED:
            newVelocity = self.MAX_SPEED
        elif newVelocity < self.MIN_SPEED:
            newVelocity = self.MIN_SPEED
        return newVelocity

    def tryMove(self, newX, newY):
        """ Try to move the ship to a new location """
        if self.validPosition(newX, self.rectangle.width):
            self.rectangle.x = newX

        if self.validPosition(newY, self.rectangle.height):
            self.rectangle.y = newY
        self.update = True

    def validPosition(self, newPosition, shipSize):
        """ Return if the new Position is a valid Position """
        return not (newPosition < 0 or newPosition + shipSize > 100)
