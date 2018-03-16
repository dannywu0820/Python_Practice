from abc import ABCMeta, abstractmethod

class EnemyShip(metaclass=ABCMeta):
    def __init__(self):
        self.name
        self.damage
    
    def getName(self):
        return self.name
    
    def setName(self, new_name):
        self.name = new_name
    
    def getDamage(self):
        return self.damage
        
    def setDamage(self, new_damage):
        self.damage = new_damage
    
    def followHeroShip(self):
        print("%s is following the hero" % (self.getName()))
    
    def attackHeroShip(self):
        print("%s is attacking the hero with %d damage" % (self.getName(), self.getDamage()))
        
    def doAll(self):
        self.followHeroShip()
        self.attackHeroShip()
    
    