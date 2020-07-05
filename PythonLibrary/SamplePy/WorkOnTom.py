class Manager:
    def __init__(self):
        self.tom = Engineer()
    def work_a(self):
        result = self.tom.add(5,3)
        print(result)
    def work_b(self):
        result = self.tom.add(8,4)
        print(result)
class Engineer:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
        
bob = Manager()
bob.work_a()
bob.work_b()
