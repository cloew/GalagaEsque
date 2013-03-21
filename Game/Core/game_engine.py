from PySide.QtCore import QBasicTimer, QObject

class GameEngine:
    """ Represents the engine for managing the game """
    Speed = 10

    def __init__(self):
        """ Instantiate the Game Engine """
        self.timer = QBasicTimer()
        self.window = None
        self.object = QObject()
        self.object.timerEvent = self.timerEvent

    def start(self, window):
        """ Start the Game Engine """
        self.window = window
        self.timer.start(GameEngine.Speed, self.object)

    def timerEvent(self, event):
        """ Run the Game Timer Loop """
        self.window.callback(self.windowWidth(), self.windowHeight())

    def windowHeight(self):
        """ Returns the Window Height """
        return self.window.contentsRect().height()
    
    def windowWidth(self):
        """ Returns the Window Width """
        return self.window.contentsRect().width()

TheGameEngine = GameEngine()