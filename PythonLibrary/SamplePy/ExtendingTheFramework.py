#フレームワーク（手を加えない）

class Calc:

    #初期化でカスタマイズ用の関数定義を受け取り登録
    def __init__(self, operation_list):
        self.operation_dict = {}
        
        for operation_tuple in operation_list:
            (operation, method) = operation_tuple
            self.operation_dict[operation] = method
            
    #イベントドリブンで電卓として動く
    
    def run(self):
        while True:
            print("please input your calculation")
            
            input_text = input()
            words = input_text.split()
            
            if words[0] == "exit":
                return
                
            if len(words) < 3:
                continue
                
            if words[0] not in self.operation_dict:
                continue
                
            #カスタマイズされた関数を呼び出す
            
            fun = self.operation_dict[words[0]]
            print(fun(int(words[1]), int(words[2])))

'''
    このクラスは非常にシンプルですがフレームワークとしてカスタマイズできるようになっています。
    まずコンストラクタでタプルの計算処理の定義 (計算の種類,その計算をする関数)をリストで並べたものを渡します。
    コンストラクタは辞書データにそれを登録しています。
    そしてrunメソッドでは標準入力を読み取り、与えられた計算の種類に応じてその計算をします。
    具体的には標準入力を空白で分解し、その一番目の要素に応じた辞書に登録された計算処理を第二、第三の要素に適用するというものです。
    たとえば文字列として “plus23”を渡すと 2,3に対して plus処理をします。whileTrueで無限ループになっているため、exitと入力されるまでは永遠に計算が続きます。

'''

'''
    次にこのフレームワークを利用するために拡張する処理を自分で定義し、それをコンストラクタで登録します。
    今回はコンストラクタで定義しましたが、「メソッドで定義を追加」ということもよくします。

'''

def add(a, b):
    return a + b
    
def decrease(a, b):
    return a - b
    
calc = Calc([("plus", add), ("minus", decrease)])

'''
    関数として add,decreaseを定義していて、その処理は足し算引き算となります。
    
    そして先程のフレームワーク Calcを初期化する際にそれらを定義にしたがってリスト上のタプルで登録しています。
    
    今回であれば addを plusという名前で登録しています。


'''

calc.run()

'''
    下記の表示をターミナルで確認してみてください。
    
    pleaseinputyourcalculation
    plus2 3
    5
    pleaseinputyourcalculation
    minus5 2
    3
    pleaseinputyourcalculation
    exit

'''

'''
    作成したインスタンスの runメソッドを呼び出すと自分で定義した処理が呼び出せていることが分かります。
    
    同じ要領で掛け算や割り算、もっと複雑な計算も定義できます。
    
    ButtonCounter.pyもGUIのアプリケーションの動きをカスタマイズしたものです。

'''
