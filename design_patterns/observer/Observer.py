from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, apple_price, google_price):
        pass
    
class StockObserver(Observer):
    def __init__(self, observer_id):
        self.observer_id = observer_id
        self.apple_price = 0
        self.google_price = 0

    def update(self, apple_price, google_price):
        self.apple_price = apple_price
        self.google_price = google_price
        
        print("[Observer %d]\nApple: %d\nGoogle: %d" % (self.observer_id, self.apple_price, self.google_price))
        
        