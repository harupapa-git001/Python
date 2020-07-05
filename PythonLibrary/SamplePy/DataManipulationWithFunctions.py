'''ex1
#フィルタ処理

def is_even(x):
    return x % 2 == 0
    
filter_object = filter(is_even, range(10))

print(list(filter_object))

'''

'''
    Pythonの filter関数は第一引数に関数を受け取り、第二引数にリストを受け取ります。
    渡された関数をリストの各要素に適用し、Trueとなった要素だけから構成されたフィルターオブジェクトを返します。
    必要であればリスト型にキャストをします。filterという名前が示す通り、リストをフィルタ処理しています。
    
    上記の例ではまず関数 is_evenを宣言しています。
    %は剰余(あまり)をもとめる演算子なので、「引数 xを2で割った余りが0か」ということを返しています。
    filter関数にこの is_evenを第一引数として私、range(10)で 0から9までのリスト(正確にはrange型)を与えると、与えられたリストに対して順番に関数を適用していき Trueとなったものだけから構成されるリストを返します。


'''

'''
    ラムダはこれらの関数を受け取る関数と相性がいいです。
    先ほどの例ではわざわざ偶数判定の関数を定義していましたが、それをラムダに置き換えると以下のようにコードが簡潔になります。


'''


filter_object = filter(lambda x: x % 2 == 0, range(10))

print(list(filter_object))

'''
    ラムダについて知らなければわからないコードですが、ラムダを知っている人にとっては簡潔です。
    自分のコードで使うか使わないかは自分の判断で選べばいいでしょうが、ラムダを使う人は多くいますので少なくとも読めるようにはなっておく必要があります。

'''
