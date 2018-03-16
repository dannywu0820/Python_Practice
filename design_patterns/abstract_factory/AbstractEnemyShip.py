from abc import ABCMeta, abstractmethod

#abstract class in Java
class EnemyShip(metaclass=ABCMeta):
    def __init__(self):
        self.name = ""
        self.weapon = ""
        self.engine = ""
    
    def getName(self):
        return self.name
    
    def setName(self, new_name):
        self.name = new_name
    
    def getInfo(self):
        return ("["+self.name+"]\n"+"weapon: "+self.weapon.toString()+"\n"+"engine: "+self.engine.toString()+"\n")
    
    @abstractmethod
    def build(self):
        pass