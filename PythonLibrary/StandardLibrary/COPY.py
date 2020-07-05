'''
    ６．copy
    
    "copy"はオブジェクトの浅いコピー（shallowcopy）や深いコピー（deepcopy）を行うためのライブラリです。
    
    それぞれ"copy"関数と"deepcopy"関数で行います。

'''
#オブジェクトのコピー

import copy

#浅いコピー

x = [[1, 2, 3], 4, 5]

y = copy.copy(x)

y[0][0] = 100

print("浅いコピー", x, y)

#深いコピー

xx = [[1, 2, 3], 4, 5]

yy = copy.deepcopy(xx)

yy[0][0] = 100

print("深いコピー", xx, yy)
