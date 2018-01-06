import traceback

variable_1 = "Hello, I'm varaible_1"

def function_1():
    return "Hello, I'm function_1"

class Module_1:
    def __init__(self):
        self.type = "Module_1 instance"
    
    def showType(self):
        print("I'm "+self.type)
        
    def method_1(self):
        print(self.type+" calls method_1")
        
    def method_2(self):
        print(self.type+" calls method_2")
        
    def method_3(self, input_number):
        try:
            print("-----[Exception Hnadling]-----")
            if input_number == 1:
                raise ValueError
            elif input_number == 2:
                raise EOFError
            else:
                raise SyntaxError
        except ValueError:
            print("'exception' block: ValueError")
        except (EOFError, KeyboardInterrupt):
            print("'exception' block: EOFError/KeyboardInterrupt")
        except:
            traceback.print_exc()
        else:
            print("'else' block: execute if no exception happened")
        finally:
            print("'finally' block: execute no matter what")