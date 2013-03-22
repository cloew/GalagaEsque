from PySide.QtCore import Qt
from PySide.QtGui import QImage

class LaserView:
    """ Represents the Graphical view of a Laser ship """

    def __init__(self, laser_model):
        """ Initialize the ship view """
        self.laser_model = laser_model
        self.scaled_laser = None

    def loadShipImage(self, width, height):
        """ Load the ship image """
        self.unscaled_laser = QImage("laser.png")

        xScaledSize = width*self.laser_model.rectangle.width/100
        yScaledSize = height*self.laser_model.rectangle.height/100
        
        self.scaled_laser = self.unscaled_laser.scaled(xScaledSize, yScaledSize)

    def draw(self, painter, window):
        """ Draw the image """
        if self.scaled_laser is None:
            self.loadShipImage(window.contentsRect().width(), window.contentsRect().height())

        painter.drawImage(self.laser_model.rectangle.x*window.contentsRect().width()/100, self.laser_model.rectangle.y*window.contentsRect().height()/100, self.scaled_laser)