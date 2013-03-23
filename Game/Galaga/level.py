from enemy_ship import EnemyShip
from hero_ship import HeroShip
from laser import Laser

class Level:
    """ Represents a level in the Galaga Esque Game """

    def __init__(self):
        """ Initialize the level """
        self.ship = HeroShip()
        self.enemy = EnemyShip()
        self.lasers = []
        self.score = 0

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
                self.score += 10
        
    def addLaser(self):
        """ Add a laser to the screen """
        self.lasers.append(Laser(self.ship))