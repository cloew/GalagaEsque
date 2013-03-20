from PySide.QtCore import Qt
from PySide.QtGui import QImage, QMatrix

class HeroShipView:
    """ Represents the Graphical view of the Hero's ship """

    def __init__(self, squareSize, ship_model):
        """ Initialize the ship view """
        self.ship_model = ship_model
        self.loadShipImage(squareSize)

    def loadShipImage(self, squareSize):
        """ Load the ship image """
        self.unscaled_ship = QImage("hero_ship.png")
        matrix = QMatrix()
        matrix = matrix.rotate(180)
        self.unscaled_ship = self.unscaled_ship.transformed(matrix)
        
        self.scaled_ship = self.unscaled_ship.scaled(squareSize[0], squareSize[1], Qt.KeepAspectRatio)
        self.update = True

    def draw(self, painter, window):
        """ Draw the image """
        painter.drawImage(self.ship_model.rectangle.x*window.contentsRect().width()/100, self.ship_model.rectangle.y*window.contentsRect().height()/100, self.scaled_ship)
        self.update = False