
class GameObjectRectangle:
    """ Represents a rectangle of a Game Object """

    def __init__(self, xSize, ySize):
        """ Create the Rectangle of the Game Object """
        self.x = 0
        self.y = 0

        self.width = xSize
        self.height = ySize

    def __repr__(self):
        return "Position({0},{1}), Size({2}, {3})".format(self.x, self.y, self.width, self.height)