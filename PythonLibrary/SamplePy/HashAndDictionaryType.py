'''
    ハッシュの仕組み

    セットで使われている重要なコンピュータ技術に、ハッシュ(Hash)と呼ばれているものがあります。集合はハッシュを使わずにでも実現できるでしょうが、PythonのセットはJavaでいうところのHashSetに近いです。
    
    ハッシュは「ハッシュ関数」と呼ばれるものに特定の値(キー)を与えて「ハッシュ値」を得ることで実現されています。
    
    ハッシュ値はある範囲のなかの数値(一般的には0からN)のどれかとなり、同じキーから生成されるハッシュ値は常に同じです。
    
    例えば、キーとして「JohnSmith」をハッシュ関数にかけるとハッシュ値「02」が得られています。
    
    同様に「LisaSmith」をハッシュ関数にかけると「01」となります。そしてハッシュ値の範囲は00から15です。
    
    この性質を考慮したうえで「ある集合に要素Xはあるか」ということをどのようにして実現するか想像してください。
    
    ハッシュを使う場合、たとえば「JohnSmith」を集合に加える際には、ハッシュ値「02」の場所に「JohnSmith」を格納します。
    
    そして「JohnSmith」が存在するかどうかのチェックはハッシュ値「02」の場所に「JohnSmith」がいるかどうか確認すればいいのです。
    
    一方、リストの探索であれば「先頭から末尾まで順に「JohnSmith」かどうかを確認していく」ことが必要です。
    
    リストのサイズが大きければこの探索コストは非常に大きくなります。
    
    「要素」の探索という面においてハッシュはリストに比べるとであるのに比べると随分スマートだと思いませんか。
    
    実際、ハッシュを使った要素の探索は非常に高速です。
    
    ただ、ハッシュも使い方を間違えると効率が悪くなります。
    
    もう一度図を見てください。
    
    よく見ると「JohnSmith」と「SandraDee」は同じハッシュ値に割り当てられています。
    
    これはいわゆる「ハッシュの衝突」と呼ばれており、これが多発すると探索のスピードが遅くなります。
    
    なぜなら「SandraDee」の有無の確認をする際に「01」を見にいって、そこに「JohnSmith」やほかの要素がたくさん入っていると、「01」のなかで「リストの探索」のようにして全部をチェックしていかないといけないからです。
    
    この問題を防ぐためにハッシュ値の範囲は十分な広さを持たせる必要があります。
    
    たとえば今回のように00から15などという範囲は狭すぎるので、これをもっと広げます。
    
    そうすると確率的には衝突は発生しにくくなります。
    
    ただ、通常はこんなことを気にしなくてもPythonがよしなに処理してくれるので大丈夫です。

    辞書型(マップ)辞書型は、別名で連想配列やマップとも呼ばれている型です。
    
    簡単にいってしまえば、重複が許されないキー(Key)とその値(Value)が対応付けられたデータ型です。
    
    「キー」という名前からわかるように、これも内部的にハッシュを使っています。
    
    例をあげて説明しましょう。
    
    果物(Key)と色(Value)の辞書オブジェクトを作るとすると、
    
    ・りんご(Key):赤色(Value)
    ・レモン :黄色
    ・ぶどう :紫
    ・さくらんぼ :赤色

    というペアが作れます。辞書型を使うと「りんご」と指定すれば「赤色」が得られ、「ぶどう」と指定すれば「紫」が帰ってきます。
    
    先ほどのセットと同じように「りんご」というキーは重複が許されずにひとつしか存在することができないため、「りんご :緑色」というペアを改めて登録すると昔のデータは上書きされてなくなってしまいます。
    
    ただ、例にある「りんご」と「さくらんぼ」を見ればわかるように値(Value)の重複は許されています。勘のいいかたであれば辞書型のしくみの想像がついたかもしれませんが、簡単にいってしまうと、セットにおけるハッシュの使い方に「Valueも追加」しているだけです。

    「JohnSmith」をキーとして指定するとハッシュ関数で「02」が得られ、「02」のなかから「JohnSmith」のValueを取得してきます。
    
    それではさっそく辞書型を利用するサンプルプログラムを書いてみます。
    
    まずは辞書オブジェクトの生成です。

'''

a = dict()

print(type(a))

b = {}

print(type(b))

c = {"apple": "red", "lemon": "yellow"}

print(type(c))

'''
    辞書オブジェクトの生成にはdict()関数を使う方法と、リストにおける []に近い {}記号を使うという方法があります。
    
    {}を使う場合はその内部で 「key:value」 という組み合わせをコンマ区切りで列挙すると、そのペアが追加された辞書オブジェクトが得られます。
    
    次に辞書オブジェクトを操作してみます。

'''

a = {"apple": "red", "lemon": "yellow"}

#バリューの取得

print(a["apple"])

#キーを指定したバリューの更新

a["apple"] = "green"

print(a["apple"])

#新しいキーとバリューの組み合わせの追加

a["orange"] = "orange"

print(a["orange"])

#存在しないキーへのアクセス

#print(a["banana"])

'''
    キーを使った値の取得、キーと値のペアの登録を行っています。
    
    リストにおけるインデックス番号がキー名に変わっているだけです。
    
    "辞書オブジェクト[キー]"としてキーを指定することで、対応する値(Value)を参照します。
    
    存在しないキーを参照しようとすると当然エラーとなります。
    
    ただ、存在しないキーを参照した場合に「デフォルト値」を返したいという場合がたまにあります。
    
    そのような場合、getメソッドや setdefaultメソッドを利用します。
    
    getメソッドの第一引数にキーを指定し、第二引数にキーが存在しなかった際に取得されるデフォルト値を指定します。
    
    第二引数がない場合はデフォルト値として Noneが使われます。

'''

a = {"apple": "red", "lemon": "yellow"}

print(a.get("apple", "green"))

print(a.get("banana", "green"))

print(a.get("grape"))

print(a)

'''
    辞書オブジェクトにはキー appleが存在するため、’apple’を getした際はそのバリューである redが返されています。
    
    ただ、存在しないキー ‘banana’を指定した場合はデフォルト値である ‘green’が返されています。
    
    辞書オブジェクト自身は変更されていません。
    
    setdefaultは getとほとんど同じですが、その名前からわかるように辞書オブジェクトがアップデートされます。

'''

a = {"apple": "red", "lemon": "yellow"}

print(a.setdefault("apple", "green"))

print(a.setdefault("banana", "green"))

print(a)

'''
    セットと同じように辞書型もリストと似た操作ができます。例えばキーの存在確認に inを使うことができます。

'''

a = {"apple": "red", "lemon": "yellow"}

print("apple" in a)

print("banana" in a)

'''
    ほかにも、リストに似た特性はあり、popや for文での利用も可能です。

'''

a = {"lemon": "yellow", "apple": "red", "banana": "green"}

print(a.pop("apple"))

print(a)

print(a.popitem())

print(a)

'''
    キー一覧の取得などもよく使います。値一覧の取得はそれほど使わないかもしれないです。

'''

a = {"lemon": "yellow", "apple": "red", "banana": "green"}

print(a.keys())

print(a.values())

'''
    ほかにも辞書型の使い方にはいろいろありますが、まずはこのあたりさえ使いこなせれば十分でしょう。

'''
