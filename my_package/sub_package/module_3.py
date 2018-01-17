import sys

class rational:
    class iterator:
        def __init__(self, length):
            pass
        
        def __next__(self):
            pass
        
    '''def __setattr__(self, name, value): #define '.' operator
        print("You use setattr to set %s as %d" % (name, value))
    
    def __getattr__(self, name): #define '.' operator
        print("You use getattr")
        #return self.__dict__[name]'''
    
    def __init__(self, n, d, l):
        self.numer = n
        self.denom = d
        self.length = l
    
    def __str__(self): #return what clients need to see
        return 'Rational: %d/%d' % (self.numer, self.denom)
        
    def __repr__(self): #return what developers need to see
        return 'Numerator: %d\nDenominator: %d' % (self.numer, self.denom)
        
    '''def __setitem__(self): #define '[]' operator
        pass
    
    def __getitem__(self): #define '[]' operator
        pass'''
    
    def __add__(self, another): #define '+' operator
        pass
        
    def __sub__(self, another): #define '-' operator
        pass
        
    def __mul__(self, another): #define '*' operator
        pass
        
    def __truediv__(self, another): #define '/' operator
        pass
        
    def __eq__(self, another): #define '==' operator
        pass
    
    def __del__(self): #define operation before garbage collection
        pass
    
    def __iter__(self):
        return rational.iterator(self.length)