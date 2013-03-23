from level_view import LevelView

from Game.Core.game_engine import TheGameEngine
from Game.Galaga.level import Level

from PySide.QtCore import QCoreApplication, Qt

class LevelController:
    """ It's the controller for a Level """
    MAX_LASERS = 10
    
    def __init__(self, application):
        """ Initialize the Level Controller """
        self.application = application
        self.paused =  False
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
            if len(self.level.lasers) < LevelController.MAX_LASERS:
                self.level.addLaser()
                self.window.addLaser()
        elif key == Qt.Key_Return or key == Qt.Key_Enter:
            if self.level.over:
                QCoreApplication.instance().quit()
            else:
                if self.paused:
                    self.paused = False
                    TheGameEngine.startTimer()
                else:
                    self.paused = True
                    TheGameEngine.stop()
        

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