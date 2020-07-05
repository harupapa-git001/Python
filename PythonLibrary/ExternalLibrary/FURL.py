'''
    8. furl
    
    "furl"はURLを扱うための外部ライブラリで、標準ライブラリの"urllib"などを使うよりも便利だという意見をよく耳にします。
    
    本書ではバージョン1.0.1を扱います。
    
    #インストール
    ■Windows
    
    pip install furl
    
    ■macOS
    
    pip3 install furl
    
    基本的な使い方は次のとおりです。
'''
#furlの利用

from furl import furl

#URLのパース

url = "https://user:pass@host:1234/parent/child?hoge=fuga&boo=piyo"

f = furl(url)

print("①", f.url)

print("②", f.scheme, f.username, f.password, f.host, f.port, f.path, f.query)

#パスをセグメントで分割する

print("③", f.path.segments)

#パスにセグメントを追加する

f.path.add("added")

print("④", f.url)

#セグメントの一部を削除する

del f.path.segments[1]

print("⑤", f.url)

#クエリパラメータを変更する

f.query.params["hoge"] = "abcd"

print("⑥", f.url)

#クエリパラメータを追加する

f.add(args = {"param": ["123"]})

print("⑦", f.url)

#クエリパラメータを削除する

f.remove(args = "boo")

print("⑧", f.url)

'''
    例の通り、URLのパースだけではなく、手軽にURLやパラメータの書き換えが行える点がこのライブラリの主な特徴です。
'''
