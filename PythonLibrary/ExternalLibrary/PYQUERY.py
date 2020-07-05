'''
    9. PyQuery
    
    "PyQuery"はjQueryライクなAPIを提供するライブラリです。
    
    本書ではバージョン1.4.0を扱います。

    #インストール

    ■Windows
    
    pip install PyQuery
    
    ■macOS
    
    pip3 install PyQuery
    
    jQueryの基礎知識があれば、このライブラリはWebスクレイピングの強力な味方になってくれると思います。
    
    基本的な使い方は次のとおりです。
'''
#PyQueryの利用

from pyquery import PyQuery as pq

html = '''
<ul>
    <li id = "nya">item1</li>
    <li>item2</li>
    <li>item3</li>
    <li>item4</li>
</ul>
'''

#インスタンスの生成

dom =pq(html)

#CSSセレクタの利用

print("①", dom("#hoge"))

#DOMの操作

dom("li").each(lambda i, node: pq(node).attr(class_ = "fuga"))

print("②", dom)

#スクレイピング

dom = pq("http://www.python.org/about/")

lst = []

for link in dom("a").items():
    url = link.attr["href"]
    
    lst.append(url) if url.startswith("http") else ''

print("③", lst)

'''
    先述の通り、jQueryの知識があればそれぞれの処理で何をしているのかは一目瞭然だと思います。
    
    ※「DOMの操作」の処理にてhtmlクラスを指定する際に"class_"としていますが、これは"class"がPythonの予約後だからです。
    
    Pythonを使ったWebスクレイピングでは"BeautifulSoup"が人気をほこっていますが、案外こちらのライブラリを好む人も多いようです。
    
'''
