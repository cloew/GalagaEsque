from PySide.QtCore import QBasicTimer, QObject

class GameEngine:
    """ Represents the engine for managing the game """
    Speed = 10

    def __init__(self):
        """ Instantiate the Game Engine """
        self.timer = QBasicTimer()
        
        self.window = None
        self.controller = None

        self.object = QObject()
        self.object.timerEvent = self.timerEvent

    def start(self, window, controller):
        """ Start the Game Engine """
        self.controller = controller
        self.window = window
        self.timer.start(GameEngine.Speed, self.object)

    def timerEvent(self, event):
        """ Run the Game Timer Loop """
        self.controller.performGameCycle()

    def updateUI(self):
        """ Set the UI to update """
        self.window.update()

    def windowHeight(self):
        """ Returns the Window Height """
        return self.window.contentsRect().height()
    
    def windowWidth(self):
        """ Returns the Window Width """
        return self.window.contentsRect().width()

TheGameEngine = GameEngine()