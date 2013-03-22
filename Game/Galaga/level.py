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

    def performGameCycle(self):
        """ Runs a single iteration of the Game """
        for laser in self.lasers:
            laser.timer()
            if laser.offScreen():
                self.lasers.remove(laser)
        self.ship.timer()
        self.enemy.timer()
        
        for laser in self.lasers:
            if laser.rectangle.collide(self.enemy.rectangle):
                self.lasers.remove(laser)
        
    def addLaser(self):
        """ Add a laser to the screen """
        self.lasers.append(Laser(self.ship))