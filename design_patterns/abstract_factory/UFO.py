from AbstractEnemyShip import EnemyShip

class UFO(EnemyShip):
    def __init__(self, ship_factory):
        super(UFO, self).__init__()
        self.ship_factory = ship_factory
        
    def build(self):
        print("Build Enemy Ship")
        self.weapon = self.ship_factory.addGun()
        self.engine = self.ship_factory.addEngine()