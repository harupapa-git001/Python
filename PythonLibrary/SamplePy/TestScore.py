class TestClass:
    def print0(self):
        print("0:")
        
    def print1(self, a, b):
        print("1: {} {}".format(a, b))
        
    def get100(self):
        return 100
        
instance = TestClass()
instance.print0()

instance.print1("A", "B")

a = instance.get100()
print(a)
