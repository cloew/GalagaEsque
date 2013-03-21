from level_view import LevelView

from Game.Core.game_engine import TheGameEngine
from Game.Galaga.level import Level

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