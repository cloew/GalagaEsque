from enemy_ship import EnemyShip
from hero_ship import HeroShip
from laser import Laser

from Game.Core.game_engine import TheGameEngine

class Level:
    """ Represents a level in the Galaga Esque Game """
    SCORE_PER_HIT = 10
    SCORE_TO_WIN = 100
    
    def __init__(self):
        """ Initialize the level """
        self.ship = HeroShip()
        self.enemy = EnemyShip()
        self.lasers = []
        self.score = 0
        self.over = False

    def performGameCycle(self):
        """ Runs a single iteration of the Game """
        for laser in self.lasers:
            laser.timer()
            if laser.offScreen():
                self.lasers.remove(laser)
        self.ship.timer()
        self.enemy.timer()
        
        for laser in self.lasers:
            if self.enemy.hit(laser):
                self.lasers.remove(laser)
                self.score += Level.SCORE_PER_HIT
                if self.score >= Level.SCORE_TO_WIN:
                    self.over = True
                    TheGameEngine.stop()
        
    def addLaser(self):
        """ Add a laser to the screen """
        self.lasers.append(Laser(self.ship))