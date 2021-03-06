'''
    関数の高度な使い方
    
    本章では関数の高度なトピックについて扱います。
    
    正直なところ本章の内容は初心者にはかなり難しいのですが、Pythonの初心者であっても既存ライブラリなどを利用する場面は多くあるため「こういう機能がある」というレベルでは知っておいたほうがいいです。
    
    本トピックは下編で扱うか悩んだのですが、難易度が高いわりに利用する頻度が高いためここで扱わせていただきます。
    
    難しければ斜め読みしていただき、ある程度 Pythonのプログラムが書けるようになってから読み直してみて下さい。

'''

'''
    関数内の関数
    
    Pythonの関数は実は関数の中に入れ子構造にすることができます。
    
    例えば以下のような使い方ができます。

'''

def test1():
    a = 10
    
#def test2(x, y):    #def　test2(x, y):を入れ子にしていないとNoneが返る＜print(test2(5, 6))は11が返る＞
#    return x + y

#    return a + test2(5, 6)

    def test2(x, y):
        return x + y
        
        return a + test2(5, 6)

print(test1())

#print(test2(5, 6)) #def test2(x, y):をインデントで入れ子にするとエラー

'''
    上記の例では関数 test1()の中で関数 test2()を定義し、それを使っています。
    
    今回のサンプルのような短い関数であればこのような使い方は不要ですが、より複雑な処理を関数で行う場合は処理を綺麗に分類するために内部で関数を定義して使うことがあります。

'''

'''
    関数オブジェクト
    
    先程もお伝えしましたがPythonは関数自体もオブジェクトです。
    
    そのため、変数に関数を代入し、それを利用することができます。

'''

def test1():
    print("test1")
    
a = test1

a()

'''
    変数に代入できるということは関数の引数として使えるということです。
    
    詳細は中編にて取り扱いますが、関数を使う関数である高階関数というものもあります。

'''

def apply_list(fun, list_):
    for i in list_:
        fun(i)
        
def print_double(x):
    print(x * 2)
    
list_ = [1, 2, 3, 4, 5]

apply_list(print_double, list_)

'''
    再帰関数
    
    再帰関数は自分自身を呼び出す関数です。
    
    forや while文でループ処理をしますが、再帰関数も似たように「同じ処理を何度も繰り返す」場面で使われます。
    
    たとえば配列から一番大きな要素を取得する処理は以下のように書けます。

'''

def get_max(list_, max_):
    #リスト長が０なら最大値を返す
    
    if(len(list_) == 0):
        return max_
        
    #リストから値を取り出し最大値の更新
    
    value = list_.pop()
    
    if(value > max_):
        max_ = value
        
    #次のリストの要素をチェック
    
    return get_max(list_, max_)
    
list_ = [5, 9, 10, 3, 5]

max_ = get_max(list_, 0)

print(max_)

'''
    コメントを読んでもらうと何をやっているか分かるかと思いますが、ようするにリストから1つの要素を取り出して、それが現在の最大値より大きければ最大値を更新する作業を繰り返し実行しています。
    
    関数が同じ関数をどんどん呼んでいき、深くまで戻っていくようなイメージです。
    
    最終的に探索し終えたら、最大値を return文で返し、深くもぐった関数呼び出しを今度は上に戻っていき、最初の get_max関数の呼び出しもとに値を返します。
    
    はっきり言うとこのコードは悪い再帰関数です。
    
    再帰関数としては分かりやすいのでとりあげたのですが、同じことを for文で実現した以下のコードのほうがはるかに分かりやすいです。

'''

list_ = [5, 9, 10, 3, 5]

max_ = 0

for i in list_:
    if i > max_:
        max_ = i
        
print(max_)

'''
    このコードがどういう処理をしているかについてはあえて説明する必要はないと思います。
    
    実はこの再帰関数なのですが、ループ文にはない特徴があります。
    
    それは繰り返しではなく「木構造の呼び出し」に向いているということです。

    本書の冒頭で説明した「あるディレクトリ配下を書き出す」という再帰の例を思い出して下さい。それは以下のようなコードでした。

'''

import os

def list_file(path, indent_level):
    #ディレクトリ名を表示
    
    print("{}[{}]".format(""*indent_level, path))
    
    #ディレクトリ内のファイルとディレクトリを全てループで確認

    for file_name in os.listdir(path):
        if(file_name.startswith(".")): continue
        
        abs_filepath = path + "/" + file_name
            
        if(os.path.isdir(abs_filepath)):
            #ディレクトリだったのえ、そのディレクトリをチェックする
            
            list_file(abs_filepath, indent_level + 1)
            
        else:
            #ファイルだったので、ファイル名を表示
            
            print("{}- {}".format(""*indent_level, file_name))
            
list_file("/python", 0)

'''
    先程の最大値を得る再帰関数と同様に関数 list_file内で関数 list_fileを呼び出しています。
    
    ただ、両者の大きな違いは list_file内での list_file関数の呼び出しは必ずしも1回ではなく、状況に応じて任意の数に変わるということです。
    
    そして呼び出された毎の各関数はそれぞれ状態を維持し続けています。

    単純にグルグル回す場合はループを使い、複雑な木構造のような処理をしないといけない場合は再帰関数を使うというのが一般的な使い分けとなります。
    
    それほど利用する機会は多くないとは思いますが、覚えておいて下さい。

'''
