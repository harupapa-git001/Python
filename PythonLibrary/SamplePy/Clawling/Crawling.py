'''ex1
#urllib.requestモジュールを使ったクローリング

from urllib.request import urlopen

#HTTPResponse型のクラスを取得する

f = urlopen("https://github.com/DavidBruant/Map-Set.prototype.toJSON")

#型の確認

print(type(f))

#HTTPヘッダの取得

print(f.getheader("Content-Type"))

#ステータスコード

print(f.status)

#HTTPレスポンス

print(f.read().decode())

'''

'''ex2
#エンコーディングの判定

from urllib.request import urlopen

#HTTPResponse型のクラスを取得する

f = urlopen("https://www.python.jp/")

#エンコーディング種類の取得（デフォルトをutf-8に）

enc_type = f.info().get_content_charset(failobj = "utf-8")

#HTTPレスポンスのデコード

data = f.read().decode(enc_type)
print(data)

'''

#ex3
#エンコーディングの判定その２

import re

from urllib.request import urlopen

f = urlopen("https://www.python.jp/")
content = f.read()

#HTTPレスポンスの先頭1024バイトをASCII文字列にデコード
#（ascii範囲外の文字はU + FFFDに置き換える）

decode_str = content[:1024].decode("ascii", errors = "replace")

#reモジュールを使って正規表現

match = re.search(r"charset = ['\n']?([\w-] + )", decode_str)

if match:
    enc_type = match.group(1)

else:
    enc_type = "utf-8" #charsetが明示されてない場合はutf-8
    
data = content.decode(enc_type)
print(data)

'''
    先の例と実行結果に変化はありませんが、これでより一層確実に動作するようになりました。
    
    やっていることは単純で、・metaタグはHTMLの前半に記載されるため、先頭1024バイトを判断材料とする・とりあえずASCII文字列にデコード、範囲外の文字への例外対策もしておく・正規表現を使ってcharsetの値を取得する（※）これだけです。
    
    ※match.group(1)は「マッチしたうちの最初のグループ」を取得します



'''
