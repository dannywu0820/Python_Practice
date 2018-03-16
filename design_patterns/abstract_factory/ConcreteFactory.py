from AbstractFactory import EnemyShipFactory
from Gun import UFOGun, RocketGun
from Engine import UFOEngine, RocketEngine

class UFOFactory(EnemyShipFactory):
    def addGun(self):
        return UFOGun()
    
    def addEngine(self):
        return UFOEngine()
    
class RocketFactory(EnemyShipFactory):
    def addGun(self):
        return RocketGun()
    
    def addEngine(self):
        return RocketEngine()