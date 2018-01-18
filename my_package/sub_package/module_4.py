import sys
from abc import ABCMeta, abstractmethod

class human(metaclass=ABCMeta):
    def __init__(self, race):
        self.race = race

    def selfIntro(self):
        print("I'm %s" % self.race)
        
    @abstractmethod
    def doSpecificWork(self):
        pass

class male(human):
    def __init__(self, race):
        super(male, self).__init__(race)
        self.gender = "male"
        
    def selfIntro(self):
        print("I'm %s %s" % (self.race, self.gender))
        
    def doSpecificWork(self):
        print("%s do hunting" % self.gender)

class female(human):
    def __init__(self, race):
        super(female, self).__init__(race)
        self.gender = "female"
        
    def selfIntro(self):
        print("I'm %s %s" % (self.race, self.gender))
        
    def doSpecificWork(self):
        print("%s do collecting" % self.gender)
    
class children:
    def __init__(self):
        self.age = "children"
    
class boy(male, children):
    def __init__(self, race):
        male.__init__(self, race)
        children.__init__(self)
        
    def selfIntro(self):
        print("I'm %s %s %s" % (self.race, self.gender, self.age))