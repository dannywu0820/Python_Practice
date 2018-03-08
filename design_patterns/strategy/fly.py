from abc import ABCMeta, abstractmethod

class FlyType(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass
    
class CanFly(FlyType):
    @classmethod
    def fly(self):
        print('CanFly')
        
class CanNotFly(FlyType):
    @classmethod
    def fly(self):
        print('CanNotFly')