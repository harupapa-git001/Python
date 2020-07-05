'''
    １４．tempfile
    
    "tempfile"は一時的なファイルやディレクトリを作成するためのライブラリです。
    
    いわゆる「中間生成物」を扱う際などに利用します。

'''

import tempfile

import os

#一時ファイルの作成

with tempfile.TemporaryDirectory() as temp_path:

    print(temp_path)
    
    with open(os.path.join(temp_path, "nya.txt"), "w") as f:
    
        #一時ファイルが存在することを確認
        
        print(os.path.exists(os.path.join(temp_path, "nya.txt")))
        
#一時ファイルが消去されたことを確認

print(temp_path)

print(os.path.exists(os.path.join(temp_path, "nya.txt")))

'''
    "tempfile.TemporaryDirectory"を使うことで一時ディレクトリ用のパスを取得する事ができます。

'''
