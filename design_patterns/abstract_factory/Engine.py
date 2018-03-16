from abc import ABCMeta, abstractmethod

class Engine(metaclass=ABCMeta):
    @abstractmethod
    def toString(self):
        pass
    
class UFOEngine(Engine):
    def toString(self):
        return "10 mph"
    
class RocketEngine(Engine):
    def toString(self):
        return "1000 mph"