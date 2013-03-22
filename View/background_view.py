from PySide.QtCore import Qt
from PySide.QtGui import QImage

class BackgroundView:
    """ Represents the Graphical view of the Background """

    def __init__(self):
        """ Initialize the backgroound view """
        self.scaled_background = None
    
    def loadBackgroundImage(self, width, height):
        """ Load the ship image """
        xScaledSize = width
        yScaledSize = height
        
        self.unscaled_background = QImage("Space_Background_bigger.gif")
        self.scaled_background = self.unscaled_background.scaled(xScaledSize, yScaledSize)

    def draw(self, painter, window):
        """ Draw the image """
        if self.scaled_background is None:
            self.loadBackgroundImage(window.contentsRect().width(), window.contentsRect().height())

        painter.drawImage(0, 0, self.scaled_background)