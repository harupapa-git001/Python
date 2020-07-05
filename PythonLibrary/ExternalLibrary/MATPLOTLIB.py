'''
    ４．matplotlib
    
    "matplotlib"はデータをグラフ化するためのライブラリです。
    
    本書ではバージョン2.1.1を扱います。

    #インストール
    
    ■Windows
    
    pip install matplotlib
    
    ■macOS
    
    pip3 install matplotlib

    グラフの表示には"matplotlib.pyplot"モジュールの"plop"関数および"show"関数を使用します。
    
    plot関数は第一引数にX軸に使用する値を、第二引数にY軸に使用する値をそれぞれシーケンシャルな型で指定します。

'''
#グラフの表示

import matplotlib.pyplot as p

x = [1, 2, 3, 4, 5, 6, 7]

y = [9, 1, 5, 8, 6, 2, 4]

p.plot(x, y)

p.show()

'''
    グラフには様々なカスタマイズを施すことができ、複数の線を表示することもできます。
'''
#グラフのカスタマイズ

import matplotlib.pyplot as p

p.plot([1, 2, 3, 4, 5], [9, 1, 5, 8, 6], label = "GraphA")

p.plot([5, 4, 3, 2, 1], [5, 5, 1, 2, 4], label = "GraphB")

#グラフのタイトル

p.title("GraphTitle")

#グラフの軸

p.xlabel("X-Axis")

p.ylabel("Y-Axis")

#ラベルの表示

p.legend()

p.show()
