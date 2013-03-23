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
        self.window.keyPressEvent = self.keyPressed
        self.window.keyReleaseEvent = self.keyReleased
        self.startTimer()
        
    def startTimer(self):
        """ Start the Game Timer """
        self.timer.start(GameEngine.Speed, self.object)
        
    def stop(self):
        """ Stop the game engine game timer """
        self.timer.stop()

    def timerEvent(self, event):
        """ Run the Game Timer Loop """
        self.controller.performGameCycle()

    def updateUI(self):
        """ Set the UI to update """
        self.window.update()

    def keyPressed(self, event):
        """ Called when the window has a key pressed """
        self.controller.keyPressed(event.key())

    def keyReleased(self, event):
        """ Called when the window has a key released """
        self.controller.keyReleased(event.key())

TheGameEngine = GameEngine()