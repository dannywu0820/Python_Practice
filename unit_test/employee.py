class Employee:
    raise_amount = 1.05
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.pos = 'white collar'
    
    def getPos(self):
        return self.pos
    
    def setPos(self, new_pos):
        if isinstance(new_pos, int):
            raise ValueError('Position can\'t be integer')
        else:
            self.pos = new_pos
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def applyRaise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    