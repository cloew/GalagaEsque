
class GameObjectRectangle:
    """ Represents a rectangle of a Game Object """

    def __init__(self, xSize, ySize):
        """ Create the Rectangle of the Game Object """
        self.x = 0
        self.y = 0

        self.width = xSize
        self.height = ySize

    def __repr__(self):
        return "Position({0},{1}), Size({2}, {3})".format(self.x, self.y, self.width, selfyheight)
        
    def collide(self, other):
        """ Check if a rectangle collides with another rectangle """
        return self.collideInX(other) and self.collideInY(other)
        
    def collideInX(self, other):
        """ Check if the rectangle's collide in X """
        toTheLeft = self.x+self.width < other.x
        toTheRight = self.x > other.x+other.width
        return not (toTheLeft or toTheRight)
        
    def collideInY(self, other):
        """ Check if the rectangle's collide in Y """
        above = self.y+self.height < other.y
        below = self.y > other.y+other.height
        return not (above or below)
        
    def setCenterX(self, x):
        """ Center the Rectangle on the X Coordinate given """
        self.x = x - self.width/2.0

    def setCenterY(self, y):
        """ Center the Rectangle on the Y Coordinate given """
        self.y = y - self.height/2.0

    def moveToLeft(self):
        """ Move the Rectangle to the left of the screen """
        self.x = 0

    def moveToRight(self):
        """ Move the Rectangle to the right of the screen """
        self.x = 100 - self.width

    def moveToTop(self):
        """ Move the Rectangle to the top of the screen """
        self.y = 0

    def moveToBottom(self):
        """ Move the Rectangle to the bottom of the screen """
        self.y = 100 - self.height