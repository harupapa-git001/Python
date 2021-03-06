'''
    ドキュメンテーション
    
    オブジェクト指向は外部に必要な部分だけ見せることが重要です。
    
    外部に対して適切に「このクラスやメソッドはどう使うか」を適切に提示できなければ、利用者はコードを読まないと何をどうすればそのクラスを使えるか分かりません。
    
    本章で「docstring」を使ってドキュメントを書く方法を学びます。
    
    docstringに適切なコメントを書くことで利用者はソースコードを読まなくてクラスやメソッドの使い方が把握できます。
    
    なお、docstringはクラス以外でも使えるテクニックですので、クラス以外についても扱います。

    このドキュメンテーションですが、主に以下の箇所にて使われます。
    
    ・モジュール
    ・クラス
    ・関数、メソッド
    
    一番簡単な関数を使ってドキュメントの書き方を紹介します 。
    
    関数のdocstringは def宣言の後にトリプルクオテーションで記載します。
    
    以下にサンプルを記載します。

'''

'''
#mymodule.py

def test_function(x, y):
    """ドキュメントを試す関数
    
    引数:
        x(int):ひとつ目の引数
        
        y(str):ふたつ目の引数
        
        返り値:
            str:引数を結合した文字列
            
        """
        
        return str(x) + y
        
'''

'''
    上記は自作モジュール mymoduleに定義した「整数型と文字列型の引数を受け取り、それを結合した文字列を返す関数」です。
    
    見てもらうと分かるように関数の定義の直後に「この関数が何をするか」という説明がトリプルクオテーションでされています。
    
    ドキュメントの書き方にはいくつかの流派がありますが、いずれにせよ以下のことは説明する必要があります。
    
    なにを目的とした関数か
    引数の詳細
    返り値の詳細
    注意点(もしあれば)
    
    上記のサンプルコードを見てもこれらが書かれていることが分かります。
    
    この関数の説明はコードを読んだ時にも明確にわかりますが、ツールを使うことでコードファイルを読まずに確認することもできます。
    
    例えばプロンプトにてこの関数を利用したいとしましょう。
    
    その際、以下のようにすればこの関数のドキュメントを確認できます。

'''
#qボタンを押すことでこのヘルプは抜けられます。

import mymodule

help(mymodule.test_function)    #ヘルプ画面で出力

'''
    実は関数に限らずドキュメントはオブジェクトの特殊属性 __doc__に文字列として格納されており、help関数はそれを読み取っています。

'''
print(mymodule.test_function.__doc__)   #ターミナル画面で出力

'''
    次にモジュールのドキュメントです。
    
    関数のドキュメントと同じくトリプルクオテーションで定義します。
    
    定義する位置は文字コードやシバンの後になり、実際のコード(例えば import文など)の前となります。
    
    モジュールのドキュメントに記載すべき内容は以下のとおりです。
    
    ・コードの管理者の署名
    ・変更履歴など
    ・何を目的としたモジュールか
    ・引数を受け取るのであればどう利用するか
    ・注意点
    
    コードの管理者や変更履歴はモジュールが長くメンテされることを考えた場合に必要です。
    
    たとえばバグなどがあった場合は管理者に連絡をとることができます。
    
    その他は先程の関数とそれほど変わりません。
    
    スクリプトとして呼び出す際の引数に関してはコードを読まなくても分かるように記載することが必須です。
    
    最後にクラスのドキュメントですが、これはそのクラスの目的などを記載します。関数とそれほど変わりません。
    
    ドキュメントの書き方は様々なものがあります。
    
    共同作業をするのであればチームでフォーマットを統一することが望ましいため、事前に話し合っておくことをおすすめします。

'''
