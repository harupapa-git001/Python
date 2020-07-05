'''
    メソッドのオーバーライド「オーバーライド」は継承したクラスで継承元のクラスのメソッドを「上書き」する手法です。
    前章にてコンストラクタであまり説明をせずにオーバーライドを使いましたが、もう少ししっかり解説したいと思います。
    まず、そもそも何のためにオーバーライドを使うかということなのですが、一般的には後述する「ポリモーフィズム」を実現するためです。
    ポリモーフィズムについての解説で、オーバーライドのメリットやどういう場面で使うかといったことを扱うため、ここではとりあえずオーバーライドの文法的な話のみに留めます。

    まず、以下のクラスParentがあるとしましょう。

 '''

class Parent:
    def __init__(self):
        print("Parent __init__()")
        
    def fun1(self):
        print("Parent fun1()")
        
    def fun2(self):
        print("Parent fun2()")
        
'''
    そしてこれを継承するChildというクラスを作ります。

'''

class Child(Parent):
    def __init__(self):
        print("Child __init__()")
        
    def fun1(self):
        print("Chilc fun1()")

'''
    見てわかるようにChildはParentを継承するという宣言を1行目で行い、コンストラクタ__init__と親が持つfun1()というメソッドと同じ名前のメソッドを再定義しています。
    
    一方fun2()については再定義していません。
    それぞれのメソッドでは何が呼ばれたかを分かるように print文を使っています。

'''

c = Child()

c.fun1()

c.fun2()

'''
    見てもらうとわかりますが、Childで再定義したコンストラクタやメソッドはChildの処理が呼び出され、再定義していないメソッドは親のものがそのまま呼びだされていることがわかります。
    ちなみに、Childのコンストラクタをなくすと親のコンストラクタを呼び出します。
    コンストラクタもメソッドなので、メソッドfun1()、fun2()の動きと全く同じ原理です。

'''

class Child(Parent):
    '''
    def __init__(self):
        print("Child __init__()")
    '''
    
    def fun1(self):
        print("Chilc fun1()")
        
c = Child()

'''
    さて、このあたりでいったんオーバーライドの動きについてまとめてみましょうか。

    子クラスで再定義したメソッドは子クラスのものを呼び出し、再定義していない場合は親クラスのメソッドを呼び出します。
    当然ながら、子クラスだけしか持たないメソッドを親クラスのインスタンスは呼び出せません。

'''

'''
    オーバーライドされた親メソッドの呼び出し
    
    先ほどのオーバーライドの例ですが、若干困ったところがあります。
    それは「オーバーライドしたいのだけれども、親の処理を呼び出す必要がある」という場合です。少し難しくなるのですが、例をあげてみましょう。
    たとえば「あるテキスト情報をデータベース・サーバーに登録する」必要があるとします。
    ただ、その入力方法にはいくつかの選択肢があり、ひとつはコンソールを使ったもの、もうひとつはWebからの入力(HTTPREST)であるとします。
    
    まず継承を使わない一番愚直な実装はそれぞれの入力方法ごとにクラスを作り、そのなかでデータベース・サーバーへの接続と書き込み処理を記述するというものです。
    ただ、よく考えてもらうとわかるようにデータベースへの登録処理は両方のクラスでほとんど同じになるため、あまり賢い実装方法だといえません。
    これを解消するために今回は親クラスにデータベースの処理は任せ、子クラスは異なるinput方法にのみ対応するという設計をしたとしましょう。
    
    これは以下の図のようになります。

Register:                   Console Register
    __init__(IP)        ⬅️        __init__(IP)
    register(text)      ⬅️       register()
    
                            Web Register
                        ↖️        __init__(IP)
                        ↖️        　register(http)


    ConsoleRegisterクラスはコンソールへの入力をデータベースに登録し、WebRegisterはHTTPからの入力をデータベースに登録します。

        ただ、その登録自体は親クラスのメソッドを利用するという形式です。

    また、データベース・サーバもIPアドレスを持ちますので、その登録もそれぞれ必要です。

    ただ、その管理は親にすべて任せることとしましょう。図を見てもらうとわかると思いますが、子クラスの初期化にしろ、メソッドの呼び出しにしろ、いずれにしても「親クラスの同名のメソッド」を呼び出す必要があることがわかります。
    ただ、先ほどのParent、Childの例を見てもらうとわかるように、子クラスでメソッドをオーバーライドすると、親クラスのメソッドは呼びだされません。
    この制約を解除する方法、つまり「オーバーライドした子クラスのメソッド」が「オーバーライドされた親クラスのメソッド」を呼び出す方法について扱います。

    では実際にサンプルを使って説明してみましょう。

'''

class Register:
    def __init__(self,dbip):
        self.dbip = dbip
        
    def register(self, text):
        print('write "{}" to DB Server at {}'.format(text, self.dbip))
        
class ConsoleRegister(Register):
    def __init__(self, dbip):
        super().__init__(dbip)  # call parent method
        
    def register(self):
        text = "input from Console"
        
        super().register(text)   # call parent method
        
class WebRegister(Register):
    def __init__(self, dbip):
        super().__init__(dbip)  # call parent method
        
    def register(self):
        text = "input from REST"
        
        super().register(text)  # call parent method
        
c = ConsoleRegister("10.0.0.1")

c.register()

w = WebRegister("10.0.0.1")

w.register()

'''
    見てもらうとわかると思いますが、親クラスでデータベースへの処理を概念化した処理をさせています。
    そして、子クラスはそれぞれ親クラスのメソッドをオーバーライドして独自の入力メソッドを作っていますが、そのなかで親クラスのメソッドを呼び出しています。
    
    ”call parent method”とコメントしてある箇所です。
    このように書けばオーバーライドされて上書きされている親クラスのメソッドも呼び出せると覚えておいて下さい。
    ちなみに子のメソッドfun1()からオーバーライドされている親のメソッドfun2()を呼び出すといった使い方もできます。
    ただ、あまりにそのような使い方をするとコードが読みにくくなるので、設計レベルで改めたほうがいいかもしれません。
    そもそもfun2をオーバーライドするのではなく、別のメソッド名のものにしたり、後述するデリゲーションを使うべき状況かもしれないです。
    なお、親クラスのメソッドの呼び出しは関数 super()を使う以外の方法もあります。
    たとえば親クラスの名前に続いてメソッドを書くことでもオーバーライドされたメソッドを呼び出すことができます。

'''

class Register:
    def __init__(self, dbip):
        self.dbip = dbip
        
    def register(self, text):
        print('write "{}" to DB Server at {}'.format(text, self.dbip))
        
class ConsoleRegister(Register):
    def __init__(self, dbip):
        Register.__init__(self, dbip)   # call parent method
        
    def register(self):
        text = "input from Console"
        
        Register.register(self, text)   # call parent method
        
c = ConsoleRegister("10.0.0.1")

c.register()

'''
    Python2ではこの書き方はよく用いられていましたが、python3の場合は親クラスの名前を指定しなくても親クラスのメソッドが呼び出せるため、先ほどの super()を使った呼び出しのほうが一般的です。

'''
