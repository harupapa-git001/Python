'''
    文字列型のメソッド
    
    先にお伝えしたように文字列型もオブジェクトであるためメソッドが利用できます。
    ただ、文字列型に対してメソッドを呼び出した場合は「呼び出し元の文字列オブジェクトは変更されない」という規則があります。
    例えば次にお話する文字列の置き換えも、置き換えメソッドを呼び出した文字列は変更されず、メソッドの返り値として変更された文字列オブジェクトがかえってくるという動きをします。
    これは全ての文字列型のメソッドに共通した特徴なので必ず覚えておいて下さい。
    
    　　文字列型のメソッドを使ってテキストの置き換え処理をしてみます。
     テキストエディタなどである特定のキーワードを別のキーワードに置き換えることがあるかと思いますが、それと同じ要領です。

'''

text = "hello world python"

text1 = text.replace("o", "O")

print(text)

print(text1)

'''
    文字列.replace(置き換える文字列,置き換えられる文字列)とすると、変換された文字列が返されます。
    
       例にもあるように、元の文字列自体は変化していません。
    
     1文字だけを変更することもできますし、文字列を変更することもできます。

        文字列の検索もそれほど難しくはありません。
     検索には「存在の確認」と「位置の確認」の2つの使い方があり、それぞれ次のようになります。

'''

text = "hello world python"

print("wor" in text)

print("wOr" in text)

print(text.find("wor"))

print(text.find("wOr"))

print(text.find("o"))


'''
    inについてはlistでの使い方と同じで、「Ain B」の場合は「AがBに含まれていれば Trueを返す」という動きをします。
    ’helloworldpython’というテキストに ‘wor’は含まれているので Trueとなっています。
    
       findメソッドについては最も左側にあるマッチした位置を返します。
    そのため、'o'は何個もありますが、一番左の位置となっています。マッチしない場合は-1が返ってきます。

    findメソッドに似たメソッドで startswithと endswithがあります。
    名前から分かるかもしれませんが、前者は「この文字列から始まっていればTrue」、後者は「この文字列で終わっていればTrue」という動きをします。

'''

text = "hello world python"

print(text.startswith("hell"))

print(text.startswith("hellO"))

print(text.endswith("hon"))

print(text.endswith("hOn"))

'''
    それほど使う場面は多くないのですが、findメソッドのオプションである第二引数を指定することで前側を指定した数だけ飛ばして途中から検索することもできます。
    
       右側から探索をする rfindというメソッドも利用できます。

'''

text = "hello world python"

print(text.find("o", 10))

print(text.rfind("o"))


'''
    次に文字列の前後からの特定の文字の削除メソッド stripです。よく利用するのは、前後の空白や改行コード、タブなどを取り除く場合などでしょう。

'''

text = "hello world \n"

print(text.strip())

print(text.strip(" hell"))

'''
    strip関数に引数を指定しないと文字列の前後の空白文字(空白とタブ、改行)が取り除かれます。
    
       引数に文字列を指定すると、その文字列が取り除かれます。
    この strip()関数はファイル読み込み処理とともに「改行コードを取り除く」ことによく使われることがありますので覚えておいて頂いたほうがいいかもしれません。

    左側の文字だけを取り除く場合は lstrip、右側だけの場合は rstripメソッドを使います。

'''

text = " hello world \n"

print(text.strip())

print(text.lstrip())

print(text.rstrip())

'''
    また、文字列を splitメソッドで特定の区切り文字で分割して文字列のリストにすることもできます。
    改行コードで分割する場合は split(‘\n’)とすることもできますし、splitlines()という専用のメソッドもあります。

'''

text = "1, taro, 35, male"

print(text.split(","))

text = "hello\nworld\npython"

print(text.splitlines())

print(text.split("\n"))

'''
    上記サンプルにあるようなコンマ「,」記号での文字列の分割は CSV(Excel出力)やログの解析あたりでよく使うテクニックです。
    たとえば以下ではトリプルくおテーションで作ったCSV形式のテキストを、まず改行コードで分割して1行ずつににして、各行においてコンマでテキストを区切っています。

'''
# text内のトリプルクォーテーションで改行をした場合、2, jiro, 29, maleの前後や3, hanako, 23, femaleの前などに改行を連続して入れると出力に影響します。＜taro:35のみになる＞

text = '''1, taro, 35, male
2, jiro, 29, male
3, hanako, 23, female'''

for line in text.split("\n"):
    elems = line.split(",")
    
    print(elems[1].strip() + ":" + elems[2].strip())

'''
    この例のように CSVの要素に空白が含まれているのであれば、先ほどの strip関数と組み合わせて前後の空白を取り除いて整形してあげてもいいかもしれません。
    「オブジェクトを返す関数やメソッド」に対してメソッドを呼び出しているようなコードはよくありますが、それは上記と同じように「作成されたばかりのオブジェクトのメソッドを呼ぶ」ということをしています。
    
       例えば以下の様なコードにです。

'''

print("hello world python".replace("he", "HE").replace("py", "PY"))

'''
    これは分かりやすく書けば以下のようになります。

'''

a = "hello world python"

b = a.replace("he", "HE")

print(b.replace("py", "PY"))

'''
    メソッドをチェーン上に並べるのは長くなりすぎなければ積極的に活用するべきだと思います。
    ただ、例えばマイナーなメソッドを呼び出したりバグを生んだりしそうな場所での利用は避けて頂いたほうが無難です。
    メソッドをチェーン上に並べた場所でエラーが発生すると、そのエラー原因の特定が困難な場合があります。
    
       他には文字列の大文字、小文字の変換あたりもよく使います。

'''

a = "Hello Python"

a.lower()

print(a.lower())

a.upper()

print(a.upper())
