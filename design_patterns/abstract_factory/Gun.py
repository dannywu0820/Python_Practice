from abc import ABCMeta, abstractmethod

class Gun(metaclass=ABCMeta):
    @abstractmethod
    def toString(self):
        pass
    
class UFOGun(Gun):
    def toString(self):
        return "1000 damage"
    
class RocketGun(Gun):
    def toString(self):
        return "10 damage"