'''
    ３．イテレータ
    
    イテレータは「リストなどの複数の要素をもったデータ型に対して、順番にデータを取り出す機能を提供するモノ」です。
    
    例えば、リスト型のデータがfor文を使って順に要素を取り出すことができるのはこのイテレータのおかげなのです。
    
    まずはこのイテレータがどんなモノなのかを例で見てみましょう。

'''

'''ex1
#イテレータ

lst = ["shiro", "tanaka", "masaru"]

i = iter(lst)   #①

print(next(i))  #②

print(next(i))

print(next(i))

print(next(i))  #③

'''

'''
    この例で着目して欲しいポイントは３点あります。
    
    まず①の行ではiter関数でリストをイテレータ化しています。
    
    この関数はリストに限らず、辞書やタプルなどでも同じように扱えます。
    
    次に②ではnext関数でイテレータから要素を取り出しています。

    実行結果の通り、next関数はイテレータから順に値を取り出します。
    
    最後に③の行では実行した際に"StopIteration"と言う例外が発生しています。
    
    この例外はイテレータから取り出す値が存在しない場合に発生します。
    
    以上がイテレータの基本的な動きです。
    
    こららを踏まえて、次はfor文とイテレータの関係について見てみましょう。
    
    もう勘付いている人も多数いるでしょうが、for文では内部でイテレータを使ってループ処理を実現しています。
    
    例えば次のようなfor文があるとします。

    lst = ["shiro", "tanaka", "masaru"]

    for i in lst:
        ~略~
        
    ザックリ大まかに説明すると、このfor文は内部で次ように動いています。
    
    ・"lst"をイテレータに変換する
    ・イテレータから要素を取り出して"i"に格納する
    ・ブロック内の処理を実行する
    ・StopIterationが発生したらループを終了する
    ・StopIterationはfor文の中で「握り潰す」
    
    いかがでしょうか、イテレータが「何モノなのか」と言うことは理解してもらえたでしょうか？
    
    続いて、自前のクラスにイテレータを実装する方法も覚えておきましょう。
    
    イテレータは次の仕様を満たせば実装することができます。
    
    ・"__iter__"メソッドを定義する
    ・"__next__"メソッドを定義する
    ・適切に"StopIteration"例外を発生させる
    
    具体的な例は次の通りです。

'''
#イテレータの実装

class Nya:
    def __init__(self, max):
        self._max = max

    def __iter__(self):
        self._n = 0
        
        return self

    def __next__(self):
        res = self._n
        
        if res > self._max: raise StopIteration

        self._n += 1
        
        return res

nya = Nya(2)

for i in nya:
    print(i)    #0、1、2と順に表示
    
nya = Nya(3)

for i in nya:
    print(i)    #0、1、2、3と順に表示

'''
    この例では、0～インスタンス化の際に渡した値までを順番に取り出すイテレータを実装しています。
    
    これまで説明して来たイテレータの仕様を踏まえた上で、
    
    ・"__iter__"メソッドはインスタンスがイテレータに変換された際に呼び出される
    ・"__next__"メソッドはイテレータが値を取り出そうとする都度呼び出される
    
    このようにイメージ付けすれば動作は問題なく理解できると思います。
    
    イテレータの基本は以上です。
    
    アイデア次第で非常に便利な使い方ができる仕組みなので、しっかりと理解しておきましょう。
    
    なお、イテレータが実装されているオブジェクトは「iterable（イテラブル）なオブジェクト」と呼ばれるのでこれも覚えておきましょう。

'''
