#関数を呼び出す関数（高階関数）

def fun1(fun, text):
    fun(text)
    
#呼び出される普通の関数

def fun2(text):
    print("fun2: " + text)
    
#高階関数に関数を渡して利用

fun1(fun2, "hello")

'''
    関数fun1は第一引数で関数、第二引数で文字列を受け取ります。
    
    その受け取った関数を自らの関数内で呼び出しており、その引数に第二引数の文字列を渡しています。
    
    上記の例で呼び出される側の関数 fun2は普通の関数ですが、呼び出す側の関数は「高階関数」と呼ばれています。
    
    高階(こうかい)というと分かりにくいですが、ようするに関数が2階建てのように使われているとイメージしてもらえれば分かりやすいかもしれません。
    
    高い階層ということなので3階建て以上もできますが、一般的にはやりません。
    
    サンプルでは高階関数を呼び出していますが、出力を見ると実際に処理をしているのは高階関数内部で呼び出された引数の関数であることがわかります。


'''
