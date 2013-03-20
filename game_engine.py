from PySide.QtCore import QBasicTimer, QObject

class GameEngine(QObject):
    """ Represents the engine for managing the game """
    Speed = 10

    def __init__(self):
        """ Instantiate the Game Engine """
        self.timer = QBasicTimer()
        self.window = None
        QObject.__init__(self)

    def start(self, window):
        """ Start the Game Engine """
        self.window = window
        self.timer.start(GameEngine.Speed, self)

    def timerEvent(self, event):
        """ Run the Game Timer Loop """
        self.window.callback(self.windowWidth(), self.windowHeight())
        #self.ship.timer(self.windowWidth(), self.contentsRect().height())

    def windowHeight(self):
        """ Returns the Window Height """
        return self.window.contentsRect().height()
    
    def windowWidth(self):
        """ Returns the Window Width """
        return self.window.contentsRect().width()

TheGameEngine = GameEngine()