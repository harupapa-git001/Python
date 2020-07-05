'''
    モジュールのリロードモジュールを開発している際にモジュールのコードを更新しても、それを importしている側は昔のコードのモジュールを保持し続けます。
    新しいコードのものを参照して欲しい場合はそのモジュールを「リロード」することが必要で、それは以下のように行います。

        import imp
        
        imp.reload(モジュール名)
        
        モジュール impの reloadという関数を使うことでモジュールのリロードができます。実際に先ほど作成した utilモジュール(util.py)を使いながらこの挙動を確認してみます。

'''

import util

util.say_hello()

# reload前に再度importで出力確認

import util

util.say_hello()

# reloadして実行

import imp

imp.reload(util)

util.reload_hello()

util.reload_python()

