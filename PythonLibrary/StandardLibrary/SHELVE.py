'''
    ４．shelve
    
    "shelve"はオブジェクトをファイルに保存して永続化するためのライブラリです。
    
    このライブラリを使うと辞書のようにキー／バリュー形式で手軽にデータを扱うことができます。

'''
#mydb.dbというファイルを新規作成され、val1 val2 val3という出力結果を出します。

#データの永続化

import shelve

with shelve.open("mydb") as db:
    #データの保存
    
    db["key1"] = "val1"
    
    db["key2"] = "val2"
    
    db["key3"] = "val3"
    
    #データの読み込み
    
    print(db["key1"], db["key2"], db["key3"])

'''
    shelveオブジェクトは辞書と同じようにデータの読み書きができます。
    
    また、shelveオブジェクトは辞書がサポートしている全てのメソッドをサポートしています。
    
    続いて、"shelve.open"メソッドはファイル名の他にもいくつかの引数を持っています。
    
    このメソッドの書式はshelve.open(filename,flag='c',protocol=None,writeback=False)です。
    
    "protocol"と"writeback"はひとまず置いておき、"flag"については次の仕様を覚えておきましょう。


    "r"         #ファイルを読み込み専用で開く
    
    "w"         #ファイルを読み書き用で開く
    
    "c"         #ファイルを読み書き用で開く（存在しない場合は作成する）
    
    "n"         #常に読み書き用の新規ファイルを作成する
    
'''
