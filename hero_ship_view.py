
class HeroShipView:
    """ Represents the Graphical view of the Hero's ship """

    def __init__(self, ship_model, square_size):
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

    def draw(self, painter):
        """ Draw the image """
        painter.drawImage(self.x, self.y, self.scaled_ship)
        self.update = False