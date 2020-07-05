class MyClass:
    def __init__(self):
        self.a = 0
        b = 0
        
    def set_a(self, value):
        self.a = value
        
    def get_a(self):
        return self.a
        
    def set_b(self, value):
        b = value
        
    def get_b(self):
        return b

#インスタンス変数aにメソッドset_aで値をセットしget_aでそれを取得
instance = MyClass()
instance.set_a(3)
print(instance.get_a())

#変数bに同じことをするとエラーになる（インスタンス変数とメソッド内の変数は違うと言う答え）<'''の前にそれぞれ#を付ければコメント行となりエラーが確認できる>
'''
instance.set_b(5)
print(instance.get_b())
'''
