class MyClass:
    def __init__(self):
        print("constructor")
    
    def method1(self,a):
        print(a)
        
instance = MyClass()

instance.method1("hello")
