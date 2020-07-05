'''
    クラスの特殊属性今までも利用してきたようにクラスやインスタンスには特殊な変数やメソッドがあります。
    
    例えば def__init__(self)として定義されたメソッドはコンストラクタとして動くという「特殊な決まり」があります。
    
    その他にも継承でお話したように __class__というインスタンス変数はクラス名を返します。
    
    実はPythonではアンダースコア2つで囲われた変数やメソッドは特別な意味を持っています。
    
    そして、そういったメソッドはオーバーライドをすることができます。
    
    以下にサンプルコードを記載します。

'''

class Customer:

    def __init__(self, name, age):
        self.name = name
        
        self.age = age
        
    def print_info(self):
        print("name: " + self.name)
        
        print("age: " + str(self.age))

'''
    まず上記のクラス Customerがあるとします。
    
    インスタンス変数として nameと ageを持ち、それらを表示するためのメソッド print_infoもあります。
    
    このクラスの情報を表示しようと思ったら print_infoメソッドを呼び出す必要があり、print文にこのオブジェクトを渡しても自分が期待するような出力は得られません。

'''

c = Customer("taro", 25)

c.print_info()

print(c)

'''
    print文の出力を見てもらうと分かりますが、たんにオブジェクトの場所を表示しているだけです。
    
    この挙動を変えるために特殊メソッド __str__()をオーバーライドします。
    
    先に説明しましたが継承を明示的にしていないクラスは objectというクラスを継承しています。
    
    __str__()は objectにてアドレス番地を出力するように実装されているので、自分のクラスでその挙動を上書きします。

'''

class Customer:
    def __init__(self, name, age):
        self.name = name
        
        self.age = age
        
    #特殊メソッドのオーバーライド
    
    def __str__(self):
        return "name:{}, age:{}".format(self.name, self.age)
        
c = Customer("taro", 25)

print(c)

'''
    新しく __str__()メソッドを定義したことで str()関数で文字列化した場合に返される値が定義したフォーマットとなり、print文もその恩恵に預かります。
    
    特殊属性の詳細は高度な話題となるため後編にて詳細を扱いますが、そのようなものが存在しているということは覚えておいて下さい。

'''
