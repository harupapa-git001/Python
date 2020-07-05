'''
    ７．enum
    
    "enum"は列挙型を扱うためのライブラリです。Python3.4から導入されました。

'''
#列挙型を扱う

from enum import Enum

#定義

class Color(Enum):
    red = 1
    
    green = 2
    
    blue = 3
    
#利用
    
print(Color.blue.name)
    
print(Color.blue.value)
    
#簡略化した定義
    
Language = Enum("Language", "jp en vn")
    
print(Language.jp.name)
    
print(Language.jp.value)

'''
    各々の値には数値以外（文字列やタプルなど）も指定できます。

'''
