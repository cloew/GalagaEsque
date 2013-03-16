from PySide.QtCore import QBasicTimer, Qt
from PySide.QtGui import QColor, QFrame, QImage, QMatrix, QPainter, QTransform, QWidget

class Board(QFrame):
    
    BoardWidth = 12
    BoardHeight = 9
    Speed = 300

    def __init__(self, parent):
        super(Board, self).__init__()

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()

        self.unscaled_ship = QImage("hero_ship.png")
        matrix = QMatrix()
        matrix = matrix.rotate(180)
        self.unscaled_ship = self.unscaled_ship.transformed(matrix)
        
        self.scaled_ship = self.unscaled_ship.scaled(self.squareWidth(), self.squareHeight(), Qt.KeepAspectRatio)
        
        #self.c = Communicate()
        #self.nextPiece.setRandomShape()

    def shapeAt(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]

    def setShapeAt(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape

    def squareWidth(self):
        return self.contentsRect().width() / Board.BoardWidth

    def squareHeight(self):
        return self.contentsRect().height() / Board.BoardHeight

    def start(self):
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        #self.c.msgToSB.emit(str(self.numLinesRemoved))

        self.timer.start(Board.Speed, self)

    def pause(self):
        
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        
        if self.isPaused:
            self.timer.stop()
            #self.c.msgToSB.emit("paused")
        else:
            self.timer.start(Board.Speed, self)
            #self.c.msgToSB.emit(str(self.numLinesRemoved))

        self.update()

    def paintEvent(self, event):
        
        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        x = self.curX
        y = self.curY
        self.drawSquare(painter, rect.left() + x * self.squareWidth(),
            boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(), 1)

    def keyPressEvent(self, event):
        
        if not self.isStarted: # or self.curPiece.shape() == Tetrominoes.NoShape:
            QWidget.keyPressEvent(self, event)
            return

        key = event.key()
        
        if key == Qt.Key_P:
            self.pause()
            return
        if self.isPaused:
            return
        elif key == Qt.Key_Left:
            self.tryMove(self.curX - 1, self.curY)
        elif key == Qt.Key_Right:
            self.tryMove(self.curX + 1, self.curY)
        elif key == Qt.Key_Down:
            self.tryMove(self.curX, self.curY-1)
        elif key == Qt.Key_Up:
            self.tryMove(self.curX, self.curY+1)
        # elif key == Qt.Key_Space:
        #     self.dropDown()
        # elif key == Qt.Key_D:
        #     self.oneLineDown()
        else:
            QWidget.keyPressEvent(self, event)

    def timerEvent(self, event):
        
        if event.timerId() == self.timer.timerId():
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
            self.update()
        else:
            QFrame.timerEvent(self, event)

    def clearBoard(self):
        """  """
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(None)

    def tryMove(self, newX, newY):
        
        x = newX
        y = newY
        if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
            return False

        self.curX = newX
        self.curY = newY
        self.update()
        return True

    def drawSquare(self, painter, x, y, shape):
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        painter.drawImage(x, y, self.scaled_ship)

        # color = QColor(colorTable[shape])
        # painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
        #     self.squareHeight() - 2, color)

        # painter.setPen(color.lighter())
        # painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        # painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        # painter.setPen(color.darker())
        # painter.drawLine(x + 1, y + self.squareHeight() - 1,
        #     x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        # painter.drawLine(x + self.squareWidth() - 1, 
        #     y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)