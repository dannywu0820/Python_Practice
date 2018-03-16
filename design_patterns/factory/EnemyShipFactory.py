from UFOEnemyShip import UFOEnemyShip
from RocketEnemyShip import RocketEnemyShip

class EnemyShipFactory:
    def __init__(self):
        pass
    
    def makeEnemyShip(self, ship_type):
        new_enemy_ship = None
        
        if ship_type == "U":
            new_enemy_ship = UFOEnemyShip()
        elif ship_type == "R":
            new_enemy_ship = RocketEnemyShip()
        else:
            pass
        
        return new_enemy_ship