'''
１．pyperclip
"pyperclip"はクリップボード操作を行うためのライブラリです。

本書ではバージョン1.6.0を扱います。

    #インストール
    ■Windows
    
    pip install pyperclip
    
    ■macOS
    
    pip3 install pyperclip

    このライブラリは"copy"関数でクリップボードへのコピーを行い、"paste"関数でクリップボードの内容を取得します。

'''
#クリップボードの操作

import pyperclip

#クリップボードに値をコピーする

pyperclip.copy("hello pyperclip!")

#クリップボードから値を取得する

print(pyperclip.paste())

'''
    この例では何に面白みも感じられませんが、アイデア次第では様々な用途のプログラムを作ることができます。

'''

import pyperclip

#クリップボードの値を取得する

val = pyperclip.paste()

#改行ごとにsplitする

print(val.splitlines())
