'''ex1

import re

with open("ex3.html") as f:
    html = f.read()
    
#href属性の中身を抜き出す

for row in re.findall(r"<a.*?</a>", html, re.DOTALL):
    url = re.search(r"'<a href=""(.*?)"">", row).group(1)

print(url)

# url = re.search(r'<a href=''(.*?)''>', row).group(1)
AttributeError: 'NoneType' object has no attribute 'group'

#上記問題を解決してください

'''

'''
    ご覧の通り、正規表現を使っているだけで特に難しいことはしていません。
    しかしこの実装は効率が悪く、何よりカッコ悪いですよね。そこでBeautifulSoupと言う素晴らしい外部ライブラリを導入してみます。
    BeautifulSoupはスクレイピングをするためのモジュールで、非常に多くのユーザに利用されています。
    世の中のWebサイトはHTMLタグが正しく書かれていない場合（閉じタグが無いなど）があるため、正規表現に頼っていると思わぬ痛い目に遭うことも考えられますが、BeautifulSoupはそのような場合でもキチンと処理をしてくれる非常に頼りになる存在です。

    インストールは次のコマンドで行います。
    
    pip3 install beautifulsoup4
    
    見ての通り、今回はバージョン4を使用します。
    これより前のバージョンはPython3に対応していないので注意してください。


'''

#Beautiful Soupを使ったスクレイピング

from bs4 import BeautifulSoup

with open("ex3.html") as f:
    html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    
    tags = soup.find_all("a")
    
    for tag in tags:
        print(tag.get("href"))
