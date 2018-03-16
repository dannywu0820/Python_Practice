from abc import ABCMeta, abstractmethod

#an interface in Java
class EnemyShipFactory(metaclass=ABCMeta):
    @abstractmethod
    def addGun(self):
        pass
    
    @abstractmethod
    def addEngine(self):
        pass