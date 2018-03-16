from AbstractEnemyShip import EnemyShip

class Rocket(EnemyShip):
    def __init__(self, ship_factory):
        super(Rocket, self).__init__()
        self.ship_factory = ship_factory
        
    def build(self):
        print("Build Enemy Ship")
        self.weapon = self.ship_factory.addGun()
        self.engine = self.ship_factory.addEngine()