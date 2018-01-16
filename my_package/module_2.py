env_var = True

class Module_2:
    num_of_instances = 0
    
    def __init__(self):
        Module_2.num_of_instances+=1
        self.type = "Module_2 instance"
    
    def showType(self): #bound to instance and can only be called from instance
        print("I'm "+self.type)
        
    def method_1(self):
        print(self.type+" calls method_1")
        
    def method_2(self):
        print(self.type+" calls method_2")
    
    @classmethod
    def class_method(classs): #bound to class but can be called from both class and instance
        '''
        假如我们想仅实现类之间交互而不是通过实例？
        我们可以在类之外建立一个简单的函数来实现这个功能，但是将会使代码扩散到类之外，这个可能对未来代码维护带来问题
        现在我们要做的是在类里创建一个函数，这个函数参数是类对象而不是实例对象
        '''
        
        print("number of instances: "+str(classs.num_of_instances))
        
    @staticmethod
    def static_method(): #not bound to instance & class and can be called from both
        '''
        通常，有很多情况下一些函数与类相关，但不需要任何类或实例变量就可以实现一些功能
        比如设置环境变量，修改另一个类的属性等等...这种情况下，我们也可以使用一个函数，一样会将代码扩散到类之外（难以维护）
        现在我们使用@staticmethod, 我们可以将所有代码放到类中
        '''
        
        if env_var:
            print("environment variable is True")
        else:
            print("environment variable is False")