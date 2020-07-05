'''
    10. lxml
    
    "lxml"ハhtmlやxmlを扱うためのライブラリです。
    
    本書ではバージョン4.1.1を扱います。
    
    #インストール
    
    ■Windows
    
    pip install lxml
    
    ■macOS
    
    pip3 install lxml
    
    以下はWebサイトのhtmlから情報を抜き出す例です。
'''
#htmlから情報を抽出する

from urllib.request import urlopen

import lxml.html

#htmlの取得

html = urlopen("http://www.python.org/about/").read()

data = lxml.html.fromstring(html)

#aタグのテキストを取得

anchors = data.xpath("//a")

for a in anchors:
    print(a.text)

'''
    なお、例の通りこのライブラリを使いこなすにはXPath(XMS Path Language)の知識も必要になりますが、これを理解している人にとっては非常に使い勝手の良いライブラリと言えるでしょう。
    
'''
