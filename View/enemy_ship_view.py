from PySide.QtCore import Qt
from PySide.QtGui import QImage, QMatrix

class EnemyShipView:
    """ Represents the Graphical view of the Hero's ship """

    def __init__(self, ship_model):
        """ Initialize the ship view """
        self.ship_model = ship_model
        self.scaled_ship = None

    def loadShipImage(self, width, height):
        """ Load the ship image """
        self.unscaled_ship = QImage("hero_ship.png")

        xScaledSize = width*self.ship_model.rectangle.width/100
        yScaledSize = height*self.ship_model.rectangle.height/100
        
        self.scaled_ship = self.unscaled_ship.scaled(xScaledSize, yScaledSize)
        self.update = True

    def draw(self, painter, window):
        """ Draw the image """
        if self.scaled_ship is None:
            self.loadShipImage(window.contentsRect().width(), window.contentsRect().height())

        painter.drawImage(self.ship_model.rectangle.x*window.contentsRect().width()/100, self.ship_model.rectangle.y*window.contentsRect().height()/100, self.scaled_ship)
        self.update = False