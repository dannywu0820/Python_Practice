class Module_2:
    def __init__(self):
        self.type = "Module_2 instance"
    
    def showType(self):
        print("I'm "+self.type)
        
    def method_1(self):
        print(self.type+" calls method_1")
        
    def method_2(self):
        print(self.type+" calls method_2")