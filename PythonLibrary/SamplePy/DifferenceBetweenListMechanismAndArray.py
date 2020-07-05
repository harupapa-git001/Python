'''
    リストの仕組みと配列との違いここではCやJavaの「配列」とPythonのリストの比較を通して、Pythonのリストがどのようなものか説明します。
    Pythonでは配列相当のものがないので必ずしも学ぶ必要はないかと思いますが、この違いはプログラミング一般において重要なため、Cや Javaを学ばれたことがないかたも一読していただくといいと思います。

    CやJavaの配列は「メモリ」上に連番でデータを格納するスペースを用意するのに対して、「リスト」はバラバラの複数のデータ間を順序を持って結びつけることで実現されています。
    
    　　　Pythonのリストは、CやJavaのVectorやListに相当する型です。
    Pythonのリストはまるで配列のように利用されますが、CやJavaの配列とは大きく異なります。
    たとえば純粋な配列では、「要素(配列やリストの中にあるデータ)」の間に 新しいデータを挟み込むことはできません。
    そのため、配列に入っている要素を詰め替えるなどしてデータを追加します。

    一方、リストはN1番目の要素とN番目の要素の間に新しいデータを挟み込むことができます。
    配列ではメモリ上に要素を連番で格納するためのスペースを用意するのに対し、リストは以下の図のようにバラバラに用意された要素間を順に結びつけることで実現されているためです。

    Javaの配列のコードを確認してみます。

'''

'''

int a[] = {0, 1, 2};

System.out.println(a[1]); //２番目の要素の値を取得-> 1

System.out.println(a.length); //aの配列長を取得-> 3

a[1] = 10;

1[3] = 3; //Error

'''

'''
    1行目では要素数3のint型の配列の変数を宣言し、それに代入しています。
    
    前記事でお伝えしたように、Javaの変数には型があるのでしたね。
    a[x]とすると配列aのx番目の要素にアクセスできます。そして、a.lengthとすることで配列長が取得できます。
    
    4行目では配列の2番目の要素に値を代入しています。
    ただ、5行目では配列長3の4番目の要素に値を代入しようとしているのでエラーとなってしまいます。
    
    次にPythonのリストを使ってみます。
    Pythonの変数には型がないので、特に型を指定していない変数aに[0,1,2]という3要素のリストをそのまま代入しています。
    
    2行目ではリストの中身を確認しています。
    
    そして3行目では配列長を取得しています。

'''

a = [0, 1, 2]

print(a[1])

#２番目の要素の値を取得-> 1

print(len(a))

#aの配列長を取得-> 3

a[1] = 10;

a.append(3)

#print(len(3))  #エラー文

'''
    異なるのは5行目です。
    配列は配列長を超えて要素を代入することができませんが、リストはリスト長を伸ばすことができます。
    Pythonではリストをまるで配列のように使いますが、両者はあくまでも別物という認識を持っておく必要があります。
    
'''