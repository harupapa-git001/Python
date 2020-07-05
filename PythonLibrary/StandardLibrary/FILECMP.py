'''
    １３．filecmp
    
    "filecmp"はファイルやディレクトリを比較するためのライブラリです。
    
    ファイルの比較には"cmp"関数を使用します。

'''
#ファイルの比較

'''
■nya.txt

12345

あいうえお

ABCDE

■wan.txt

2345

あいうえお

ABCDF

'''

import filecmp

print(filecmp.cmp("nya.txt", "wan.txt"))

'''
    例の通り、"cmp"関数は比較対象が同じであればTrueを、異なればFalseを返却します。

'''
