class MyClass:
    def method2(self):
        print("self type: {}".format(type(self)))
        print("self ref: {}".format(self))
        
instance = MyClass()

print("instance type: {}".format(type(instance)))

print("instance ref: {}".format(instance))

#method2を呼び出して中身を確認
instance.method2()
