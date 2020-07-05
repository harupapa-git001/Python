'''
    ２．クラス
    
    どんな言語でも言えることですが、クラスの理解を深めるためには多数の「仕様」を覚えなければならず、それはもちろんPythonでも例外ではありません（他の言語よりはだいぶシンプルではありますが）。
    
    順に説明していくので、１つずつしっかりと身に付けてください。
    
    ■クラスの定義
    
    クラスは"class"キーワードに続けて名前を指定して定義します。
    
    Pythonにおける最小限のクラスは次の通りです。

'''

'''
#最小限のクラス

#クラス宣言

class Nya:
    pass
    
#インスタンス化

nya = Nya()

'''

'''
    ■メソッドメソッドは通常の関数と同じように記述しますが、関数と違って第一引数で「自身のインスタンス」を必ず受け取るようにしなければなりません（Javaの"this"に相当するモノです）。この引数は慣例的に"self"と言う名前にします。

'''
#メソッド

class Nya:
    def shout(self, word):
        print(word * 2)
        
nya = Nya()

nya.shout("にゃー")    #にゃーにゃー

'''
    ■コンストラクタとデストラクタ
    
    コンストラクタは"__init__"、デストラクタは"__del__"と言う名前のメソッドとしてそれぞれ記述します。

    両者とも通常のメソッドと同じく第一引数には"self"を指定します。

'''
#コンストラクタとデストラクタ

class Nya:
    def __init__(self):
        print("インスタンスが生成されました")
        
    def __del__(self):
        print("インスタンスが破棄されました")
        
#インスタンス生成

nya = Nya() #インスタンスが生成されました

#インスタンス破棄

del nya     #インスタンが破棄されました

'''
    ■インスタンス変数
    
    インスタンス変数は"self.変数名"の形式で扱います。
    
    予め宣言しておく必要はありません。

'''
#インスタンス変数

class Nya:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print("Hello {}!".format(self.name))
        
shiro = Nya("shiro")

shiro.greet()   #Hello shiro!

masaru = Nya("masaru")

masaru.greet()  #Hello masaru!

'''
    ■クラス変数クラス変数はクラスの中で通常の変数と同じように扱います。

'''
#クラス変数

class Nya:
    version = 1.01
    
print(Nya.version)  #1.01

'''
    ■継承
    
    クラスの継承は"classクラス名(基底クラス名):"と言う形式で行います。
    
    基底クラス名をカンマで区切って複数クラスの継承（多重継承）も可能です。

'''
#クラスの継承

class Nya:
    def shout(self):
        print("nya!")
        
#Nyaクラスを継承する

class Wan(Nya):
    pass
    
class Piyo():
    def greet(self):
        print("piyo!")
        
#NyaクラスとPiyoクラスを継承する

class Boo(Nya, Piyo):
    pass
    
wan = Wan()

wan.shout() #nya!

boo = Boo()

boo.shout() #nya!

boo.greet() #piyo!

'''
    ■カプセル化
    
    プロパティやメソッドの名前を"__"（_を2つ）から始めるとprivateなメンバとなります。

'''
#カプセル化

class Nya:
    def __init__(self, name):
        self.__name = name
        
    def greet(self):
        print("Hello {}!".format(self.__name))
        
shiro = Nya("shiro")

shiro.greet()   #Hello shiro!

#print(shiro.__name) #これはNG

'''
    ■ドキュメンテーション文字列
    
    関数と同じく、クラスにもドキュメンテーション文字列を含めることができます。
    
    ドキュメンテーション文字列はクラスとインスタンスのどちらからも参照することができます。

'''
#ドキュメンテーション文字列

class Nya:
    '''\
    このクラスは
    
    サンプルです
    '''
    pass
    
print(Nya.__doc__)

nya = Nya()

print(nya.__doc__)
