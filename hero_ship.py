from PySide.QtCore import Qt
from PySide.QtGui import QImage, QMatrix

class HeroShip:
    """ Hero Ship """

    def __init__(self, squareSize):
        """ Create the hero ship """
        self.x = 0
        self.y = 0

        self.xVelocity = 0
        self.yVelocity = 0

        self.loadShipImage(squareSize)

    def loadShipImage(self, squareSize):
        """ Load the ship image """
        self.unscaled_ship = QImage("hero_ship.png")
        matrix = QMatrix()
        matrix = matrix.rotate(180)
        self.unscaled_ship = self.unscaled_ship.transformed(matrix)
        
        self.scaled_ship = self.unscaled_ship.scaled(squareSize[0], squareSize[1], Qt.KeepAspectRatio)
        self.update = True

    def draw(self, painter):
        """ Draw the image """
        painter.drawImage(self.x, self.y, self.scaled_ship)
        self.update = False

    def up(self, maxX, maxY):
        """ Move the ship Up """
        self.tryMove(self.x, self.y-10, maxX, maxY)

    def down(self, maxX, maxY):
        """ Move the ship Down """
        self.tryMove(self.x, self.y+10, maxX, maxY)

    def left(self, maxX, maxY):
        """ Move the ship Left """
        self.tryMove(self.x-10, self.y, maxX, maxY)

    def right(self, maxX, maxY):
        """ Move the ship Right """
        self.tryMove(self.x+10, self.y, maxX, maxY)

    def tryMove(self, newX, newY, maxX, maxY):
        """ Try to move the ship to a new location """
        if self.validPosition(newX, maxX, self.scaled_ship.rect().width() ):
            self.x = newX

        if self.validPosition(newY, maxY, self.scaled_ship.rect().height()):
            self.y = newY
        self.update = True

    def validPosition(self, newPosition, maxPosition, shipSize):
        """ Return if the new Position is a valid Position """
        return not (newPosition < 0 or newPosition + shipSize > maxPosition)
