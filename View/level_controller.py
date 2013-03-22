from level_view import LevelView

from Game.Core.game_engine import TheGameEngine
from Game.Galaga.level import Level

from PySide.QtCore import Qt

class LevelController:
    """ It's the controller for a Level """

    def __init__(self, application):
        """ Initialize the Level Controller """
        self.application = application
        self.level = Level()
        self.window = LevelView(application, self.level)

    def run(self):
        """ Run the controller """
        self.application.setCentralWidget(self.window)
        TheGameEngine.start(self.window, self)

    def performGameCycle(self):
        """ Perform a single Game Cycle """
        self.level.performGameCycle()

    def keyPressed(self, key):
        """ Called when the Game Engine gets a keyPressed event """
        if key == Qt.Key_Left:
            self.level.ship.left()
        elif key == Qt.Key_Right:
            self.level.ship.right()
        elif key == Qt.Key_Down:
            self.level.ship.down()
        elif key == Qt.Key_Up:
            self.level.ship.up()
        elif key == Qt.Key_Space:
            if len(self.level.lasers) < 10:
                self.level.addLaser()
                self.window.addLaser()

    def keyReleased(self, key):
        """ Called when the Game Engine gets a keyReleased event """
        if key == Qt.Key_Left:
            self.level.ship.releaseLeft()
        elif key == Qt.Key_Right:
            self.level.ship.releaseRight()
        elif key == Qt.Key_Down:
            self.level.ship.releaseDown()
        elif key == Qt.Key_Up:
            self.level.ship.releaseUp()