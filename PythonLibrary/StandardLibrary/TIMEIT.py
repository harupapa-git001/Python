'''
    １１．timeit
    
    "timeit"はちょっとしたスクリプトの実行時間を計測するためのライブラリです。
    
    引数に指定した処理の実行時間を計測します。

'''
#実行時間の計測

import timeit

print(timeit.timeit("lst = [x for x in range(100)]"))

'''
    引数"setup"を使うと計測開始時に実行する処理を指定できます。
    
    また、"timeit"関数はデフォルトでは指定した処理を１００万回実行して計測するため、この回数を変更するには引数"number"を使います。

'''
#回数を指定して実行時間を計測する

import timeit

print(timeit.timeit("lst = [x for x in range(100)]", setup = 'print("start")', number = 100))
