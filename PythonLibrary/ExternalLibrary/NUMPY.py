'''
    5. numpy
    
    "numpy"は高度な数値演算（科学技術計算など）のためのライブラリで、最も有名なPythonライブラリの一つです。
    
    本書ではバージョン1.14.0を使用します。
    
    #インストール
    
    ■Windows
    
    pip install numpy
    
    ■macOS
    
    pip3 install numpy
    
    このライブラリを有効に利用するにはいうまでもなく数学周りの専門知識も必要となります。
    
    そのため、本書ではプログラマーにとっては避けられない「配列」をnumpyで扱う例をいくつか紹介します。

'''
#numpyの使い方

import numpy as np

#一次元配列の生成

arr = np.asarray([1, 2, 3])

print("①", arr)

#二次元配列の生成

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("②", arr)

#平均の取得

print("③", np.mean(arr))

#最大値、最小値の取得

print("④", np.max(arr))

print("⑤", np.min(arr))

#和の取得

print("⑥", np.sum(arr))

#標準偏差の取得

print("⑦", np.std(arr))
