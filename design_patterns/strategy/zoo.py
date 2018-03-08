from fly import CanFly, CanNotFly

class Animal:
    def __init__(self, gender, fly_type):
        self.gender = gender
        self.fly_type = fly_type
        
    def setFlyAbility(self, new_fly_type):
        self.fly_type = new_fly_type
        
    def tryToFly(self):
        self.fly_type.fly()
    
class Dog(Animal):
    def __init__(self, gender, sound):
        super(Dog, self).__init__(gender, CanNotFly())
        self.sound = sound
    
class Bird(Animal):
    def __init__(self, gender, sound):
        super(Bird, self).__init__(gender, CanFly())
        self.sound = sound