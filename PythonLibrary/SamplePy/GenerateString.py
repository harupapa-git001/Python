'''
    文字列の生成テキストを整形して文字列を作ることはよくあります。たとえば、文字列型の名前と数値型の年齢を合わせて「名前 :年齢」とするには以下のようにすればできます。

'''

text = "taro" + " : " + str(35)

print(text)

'''
    上記は文字列の結合を使って文字列を生成しています。数値型と文字列は直接結合できないため、数値35はstr()関数を使って一旦文字列にしています。3つの文字列ぐらいであれば結合を使うことで文字列を作れますが、あまりに長くなってくると結合で文字列を作るのは非常に見苦しくなってきます。結合の代わりに、文字列にテキストや数字を埋め込むという手法で文字列を生成することができます。これを実現する formatメソッドを使うと非常にシンプルに文字列を作ることができます。

'''

text = "{} : {}".format("taro", 35)

print(text)

'''
    文字列のformat関数(メソッド)の引数に {}に対応する文字列なり数値なりを与えています。
    ひとつ目の{}がfortmatメソッドの1つめの引数に対応し、2番目の{}が2番目の引数に対応、といった具合で文字列に引数を埋め込んでいきます。
    私はそれほど利用しませんが、この formatはもっと複雑な使い方もできます。
    たとえば {}の中に数字やキーワードを埋め込むことで引数の何番目をそこに埋め込むかを調整できます。

'''

print("{0} {2} {1} {0}".format("a", "b", "c"))

print("{user} : {age}".format(user = "taro", age = 35))

'''
    上記のように同じ引数を何度も埋め込むこともできます。キーワード引数を使うこともできます。
    さらに formatメソッドは文字列に埋め込む「フォーマット(形式)」も調整できます。フォーマットを指定するには「:」のあとにフォーマットを指定する書式を書きます。
    かなり細かく調整できますが、いくつか便利なものだけ紹介します。まず数字の桁の調整です。

'''

#５桁

print("{:5}".format(50))

print("{:5}".format(255))

#５桁（左寄せ）
print("{:<5}".format(255))

print("{:>5}".format(50))

#５桁（０埋め）
print("{:05}".format(50))

print("{:05}".format(255))

#位置指定やキーワードとの併用
print("{ab: 05} {cd: 05}".format(ab = 50, cd = 255))

'''
    コロンの後に数字を指定することで表示される桁数を調整できます。0を指定する桁数の前に付けることで0埋めされます。数値型の表示を調整することもよくあります。

'''

#整数、少数
print("{:d}, {:f}".format(5, 5.5))

print("{:.3f}, {:.5f}".format(5.5, 5.5))

#３桁区切り
print("{:,}, {:10,}, {:010,}".format(111111, 111111, 111111))

#基数変換（２進数、８進数、１０進数、１６進数）
print("{0: b}, {0: o}, {0: d}, {0: x}".format(100))

'''
    formatメソッドに似た書式化演算子(%)も Python3 では利用できます。
    書式化演算子は formatメソッドより気軽に使えますが、そのぶん単純なことしかできません。

    ベースとなる文字列に値を一つだけ埋め込む場合はそれを %記号の後におきます。
    そして複数の値を埋め込む場合は %記号のあとに埋め込む要素をタプルにまとめて配置します。例えば以下のようになります。

'''

text = "hello %s" % "HELLO"

print(text)

text = "hello %s python %s" % ("HELLO", 1)

print(text)

'''
    ベースとなる文字列の「%s」の箇所に値が埋め込まれていることがわかります。
    この %sはどのような形で値が埋め込まれるかを指定する「変換指定子」と呼ばれており、%sは文字列、%dは整数、%fは少数として利用されます。

'''

print("hello %s python" % (5.5))

print("hello %d python %f" % (5.5, 5.5))

'''
    formatメソッドと書式化指定子は奥が深く、様々な使い方ができます。ただ、込み入った使い方は頻繁には利用されないため、必要になったタイミングでドキュメントなどを参照すれば問題ないと思います。
    C言語などの printfに慣れているかたは書式化演算子のほうが書式を見慣れているため魅力的に見えるかもしれません。
    ただ、今後の Pythonは formatメソッドを主流としていく見込みなので、可能であれば formatメソッドを使うようにしてください。
    リストに含まれる複数の文字列を「特定の文字列」で結合していくことも可能です。
    
       これはちょうど先程のsplitメソッドの逆です。
    2次元配列(リストにリストが入っている)に格納された情報をCSV形式でファイルに書き出したりする際に便利な手法です。

'''

a = ["1", "taro", "35", "male"]

print(", ".join(a))

print(''.join(a))