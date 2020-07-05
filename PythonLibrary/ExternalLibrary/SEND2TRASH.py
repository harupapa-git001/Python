'''
    ２．send2trash
    
    "send2trash"はファイルをゴミ箱へ移動するためのライブラリです。
    
    本書ではバージョン1.4.2を扱います。
    
    #インストール
    
    ■Windows
    
    pip install send2trash
    
    ■macOS
    
    pip3 install send2trash

    標準ライブラリでファイルの削除を行うと文字通り「削除」されてしまいますが、このライブラリを使うことでゴミ箱への移動が可能になります。
    
    使い方は至ってシンプルで、"send2trash"関数に対象のファイルを指定するだけでOKです。
    
    なお、このライブラリではプラットフォームの差を意識する必要はありません。

'''
#デスクトップにtrash.txtを作成して実行してください（削除されます）
#ファイルのゴミ箱移動

from send2trash import send2trash

send2trash("/Users/user/Desktop/trash.txt")




















