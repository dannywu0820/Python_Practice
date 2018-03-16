from ConcreteFactory import UFOFactory, RocketFactory
from UFO import UFO
from Rocket import Rocket

class EnemyShipBuilding:
    def makeEnemyShip(self, ship_type):
        new_enemy_ship = None
        
        if ship_type == "UFO":
            ship_parts_factory = UFOFactory()
            new_enemy_ship = UFO(ship_parts_factory)
            new_enemy_ship.setName("UFO Enemy Ship")
        elif ship_type == "Rocket":
            ship_parts_factory = RocketFactory()
            new_enemy_ship = Rocket(ship_parts_factory)
            new_enemy_ship.setName("Rocket Enemy Ship")
        else:
            pass
        
        if new_enemy_ship != None:
            new_enemy_ship.build()
            print(new_enemy_ship.getInfo())
        
        return new_enemy_ship