from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def register(self, observer):
        pass
    
    @abstractmethod
    def unregister(self, observer):
        pass
    
    @abstractmethod
    def notifyObservers(self):
        pass
    
class StockGrabber(Subject):
    def __init__(self):
        self.observers = []
        self.apple_price = 0
        self.google_price = 0
    
    def register(self, observer_to_add):
        self.observers.append(observer_to_add)
    
    def unregister(self, observer_to_delete):
        #observer_index = self.observers.index(observer_to_delete)
        print("Delete Observer %d" % (observer_to_delete.observer_id))
        self.observers.remove(observer_to_delete)
        
    
    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.apple_price, self.google_price)
            
    def setApplePrice(self, new_price):
        self.apple_price = new_price
        self.notifyObservers()
        
    def setGooglePrice(self, new_price):
        self.google_price = new_price
        self.notifyObservers()