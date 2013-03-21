from enemy_ship import EnemyShip
from hero_ship import HeroShip

class Level:
    """ Represents a level in the Galaga Esque Game """

    def __init__(self):
        """ Initialize the level """
        self.ship = HeroShip()
        self.enemy = EnemyShip()

    def performGameCycle(self):
        """ Runs a single iteration of the Game """
        self.ship.timer()
        self.enemy.timer()