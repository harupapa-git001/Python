'''
    None型
    
    None型は「値がない」ということを表明する特別な型です。
    
    たとえば返り値がない関数の結果を取得しようとしたら、以下のように None型が取得できます。

'''

a = print("hello")

print(a)

'''
    Noneは C言語や Javaの nullに相当するもので、たまに関数やメソッドから期待されるオブジェクトの代わりに返されることがあります。
    
    少し高度になるのですが、たとえばある関数内の複雑な処理(例えばネットワークやデータベースへの接続など)に失敗した際に、「Noneを返す」もしくは「例外を発生させる」とことで処理が失敗したことを示すことができます。
    
    Noneを返す実装の場合、返り値がNoneであれば失敗したことがわかり、そうでなければ成功したということが分かります。
    
    Noneか否かの判定には is演算子を使うことが推奨されています。
    
    理由が高度になるため説明は割愛しますが、==演算子での判定は推奨されません。

'''

'''

return_value = 関数()

if(return_value is None):
    失敗した愛の処理
    
else:
    成功した際の処理

'''