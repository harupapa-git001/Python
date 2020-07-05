'''
    クラスメソッドクラスメソッドはインスタンス化しなくても使えるメソッドです。
    
    今までメソッドを利用する場合はまずクラスからインスタンスを作成し、そのインスタンスからメソッドを呼び出していました。
    
    ただ、その呼び出されるメソッドがその内部でインスタンス変数を使わない場合、そのメソッドはインスタンスに依存しないといえます。
    
    ちょっと難しいのでコードで確認してみます。

'''

class MyClass:
    def __init__(self, a):
        self.a = a
        
    #インスタンスに依存するメソッド
    
    def print_a(self):
        print(self.a)
        
    #インスタンスに依存しないメソッド
    
    def print_hello(self):
        print("hello")
        
'''
    上記クラスはインスタンス変数 aを持ちます。
    
    print_aはそのインスタン変数を使っているので、その結果はインスタンスごとに変わってきます。
    
    たとえば初期化時に 10を与えたインスタンスであれば 10と出力されるでしょうが、5を与えられたインスタンスであれば 5と出力されます。
    
    一方、print_helloメソッドは内部でインスタンスに依存する変数やメソッドを一切使っていないため、このクラスのインスタンスのどれから呼び出されようと結果は必ず同じです。
    
    クラスメソッドは上記のような「どのインスタンスから呼ばれても結果が同じ」というメソッドに使うべきテクニックです。
    
    通常のメソッド(インスタンスメソッド)ではなくクラスメソッドとして定義をするとインスタンス化せずにメソッドを呼び出せます。
    
    クラスメソッドは以下のように定義します。

'''

class MyClass:
    a = "A"
    
    #@を使ってクラスメソッドとして定義
    
    @classmethod
    
    def print_hello(cls):
        print(cls.a)
        
        print(type(cls))

'''
    今までのメソッドと違ってメソッドの定義の前に「@classmethod」というものがあります。
    
    これは実はプロパティと呼ばれている「関数やメソッドがどう動くかを定義する宣言」の1つなのですが、プロパティの詳細は初心者向けではないため下編に譲ります。
    
    現時点ではとりあえずこう使うとだけ覚えておいて下さい。
    
    クラスメソッドの宣言は通常のメソッドでは selfであった箇所が clsになっています。
    
    これは通常のメソッドはインスタンスが第一引数に渡されるのに対し、クラスメソッドはクラス自身が第一引数に渡されるからです。
    
    クラスメソッドの呼び出しは簡単で、「クラス.クラスメソッド()」とするだけです。
    
    上記のサンプルだと以下のようになります。

'''

MyClass.print_hello()

'''
    クラスメソッドはインスタンス(引数selfに入っていた)を受け取れないため、インスタンス変数やインスタンスメソッドは利用できません。
    
    ただ、引数clsを使ってクラス変数や他のクラスメソッドにはアクセスできます。
    
    なお、クラス変数を selfを経由して参照することも可能です。
    
    ただし、これは「同名のインスタンス変数が存在しない場合」のみです。
    
    例えば以下のようなコードがあるとしましょう。

'''

class MyClass:
    a = "A"
    
    def print_self_a(self):
        print(self.a)
        
    def set_self_a(self, a):
        selfa = a
        
    @classmethod
    
    def print_cls_a(cls):
        print(cls.a)
        
    @classmethod
    
    def set_cls_a(cls,a):
        cls.a = a
        
'''
    コードを読んでもらうと分かりますが、以下のような構成となっています。

    ・aというクラス変数がある
    ・インスタンス変数 aに対する set,printがある
    ・クラス変数 aに対する set,printがある
    
    普通に考えると「クラス変数に対する set,printは問題なし。
    
    インスタンス変数に対する printは setされるまでは失敗する」と動きそうなところですが、実はそうは動きません。
    
    先に言ったように「インスタンス変数が存在しない場合は selfからクラス変数を参照できる」ためです。

'''

mc1 = MyClass()

mc2 = MyClass()

mc1.print_self_a()

mc2.print_self_a()

'''
    上記コードの出力を見てもらうとわかるようにインスタンス変数の参照が実質的にクラス変数を見ていることが分かります。
    
    ただ、代入をすると話が変わってきます。

'''

mc1.set_self_a("AA")

mc1.print_self_a()

mc1.print_cls_a()

'''
    インスタンス変数に値を代入すると、インスタンス変数の aとクラス変数の aが同時に存在するようになります。
    
    self.aが新しく代入された値を持っているのに対し、cls.aはもともとの値を持ち続けていることからも分かります。
    
    上記のインスタンス変数への代入は当然ながら別の同一クラスのインスタンスには影響は及ぼしません。

    selfを経由したクラス変数へのアクセスは思わぬトラブルのもとになります。
    
    大文字のため一目で分かり、絶対に上書きがされないクラス定数以外では利用をしないほうがよいでしょう。

'''