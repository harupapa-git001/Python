'''
    例外クラス以前お話したPythonの継承について思い出してください。
    
    継承では、親クラスに大まかな実装を行い、子クラスにより詳細な実装をするのでした。
    
    たとえば親クラスが「車クラス」だとすると、子クラスは「乗用車クラス」「トラッククラス」「スポーツカークラス」といったかたちで差分を実装します。この継承は例外処理にも関わってきます。
    
    先ほど深い説明なしにexceptを以下のように使いました。

    exceptException:
       print('4:insideofexcept(catch)scope')

 exceptの後にあるExceptionは例外処理のためのクラスです。
 
 実はこのException を継承したクラスはさまざまあり、たとえばIO(入出力)のエラーを扱うためのOSError (Python2では IOError)やリストの範囲外にアクセスした場合に発生する IndexErrorなどとなります。
 
 これはちょうどExceptionが先ほどの説明の車クラスにあたり、OSErrorが乗用車クラス、IndexErrorがトラッククラスにあたります。
 
 このエラークラスとその使い方について覚えておいてもらいたいことは3つあります。
 
  ひとつめは「発生したエラーの種類に応じて呼び出されるエラーのクラスが異なる」ということです。
  
  たとえば、上記のIOErrorは当然ながらIO系の処理が失敗した際に利用されますが、まったく関係ないエラーである0による除算では利用されません。
  
  ふたつめは「exceptに親クラスを指定した場合は子クラスのエラーも対応できる」ということです。
  
  たとえばOSErrorの例外は親クラスであるExceptionでも対応可能です。これは先程のサンプルの 「exceptExceptionas e」の eにExceptionクラスではなく ZeroDivisionErrorのクラスのインスタンスが入っていたことでも分かります。
  
  そして、最後は「エラーをキャッチするexceptは複数書くことができる」という点です。
  
  複数書いた場合は先頭から順にチェックしていき、最初にマッチした処理が実行されます。
  
  どのexceptもマッチしなければ例外処理が実行できずにエラーでプログラムそのものが停止してしまいます。これは後ほど実例を示します。

 さっそくコードを書きながら確かめてみましょう。
 
 まず、以下のコードがあります。exceptが2つあり、それぞれOSErrorとExceptionと記載されています。
 
 2つだけでなく、好きなだけexceptを書くことができます。

'''

try:
    f = open("helloworld.txt", "r")
    
except OSError:
    print("os error")
    
except Exception:
    print("exception")

'''
    今回は存在しないファイルhelloworld.txtを読み込もうとしてエラーを発生させます。
    
    これはOSErrorが発生します。さっそく実行してみます。

    $ python3 test.py
    
    os error
    
    表示された'oserror'を見てわかるように、1番目のexceptが呼び出されています。
    
    'exception'という表示がないことから、2番目のexceptは呼び出されていないことがわかります。
    
    これは「最初にマッチした処理が実行」されるという仕組みがあるからです。
    
    次に発生させるエラーを0除算に変えてみます。

'''

try:
    5 / 0
    
except OSError:
    print("os error")
    
except Exception:
    print("exception")
    
'''
    これを実行すると以下のようになります。
    
    #python3 test.py
    
    exception
    
    先ほどと異なり、2番目のexceptが呼び出されています。
    
    これは1番目のexceptが、発生したエラーにマッチしておらず、無視されたためです。
    
    今回はOSErrorが1番目に指定されていますが、5/0で発生したエラーはOSErrorではなくZeroDivisionErrorなので、マッチしません。
    
    ただ、2番目のExceptionはZeroDivisionErrorの親クラスなのでマッチし、2番目のexceptが呼び出されています。
    
    エラークラスの親子関係は継承でお話した特殊属性の __base__を使うことで簡単に調べることができます。

'''

'''
>>> 5 / 0
Traceback (most recent call last):
    File"<stdin>", line 1 , in <module>
ZeroDivisionError: division by zero

#ZeroDivisionErrorの親はArithmeticError

>>> ZeroDivisionError.__base__
<class"ArithmeticError">

#ArithmeticErrorの親はException

>>>ZeroDivisionError.__base__.__base__
<class "Exception">

上記のようにZeroDivisionErrorが Exceptionの子クラスであることがわかります。

また、先ほど言ったように、どのexceptの例外クラスもマッチしないとエラーになります。試しに2番目のexceptを削ってみます。

'''

'''ex1

try:
    5 / 0
    
except IOError:
    print("io error")
    
print(1)

'''

'''
    これを実行すると以下のようになります。
    
    $ python3 test.py
    
    Traceback (most recent call last):
        File "test.py", line 2, in <module>
        5 / 0
    ZeroDivisionError: division by zero
    
    最後の'print(1)'に対応する出力がないことから、グローバルレベルでプログラムの処理が打ち切られていることがわかります。
    
    発生するエラーの種類によってさまざまな例外処理を切り替える必要がある場合は、このように複数のexceptを使って例外処理を実装すると簡単です。
    
    なお、先ほど言ったように前のexceptにマッチしたら、後のexceptはチェックされません。そのため、以下のコードで2番目のexceptIOErrorが呼び出されることは絶対にありません。

    except Exception:
        print("exception")
        
    except IOError:
        print("io error")
        
    前のexceptになんにでもマッチするものを書いてしまうと、例外はすべてそこで処理されてしまいます。
    
    つまり、前のexceptほどキャッチできる対象が小さい子クラスの例外クラスを書き、後半ほど大きな範囲をカバーできる親クラスの例外クラスを書く必要があるということです。
    
    Pythonのプログラムは簡潔であるべき場合が多いため、このような複数の exceptを書くテクニックは必ず必要という場面でなければ使う必要はありません。
    
    ただ、例外処理で対応すべきでない「バグ」を例外で拾ってしまって埋もれることを防ぐ必要があるため、全てを Exceptionや BaseException(一番広範囲の例外)で拾うのではなく、適切な例外クラスを指定するようにしてください。
    
    例外はバグに対応するためにあるものではありません。

'''

'''
    カスタム例外クラスの作成今までは既存の例外クラスのみを利用していましたが、自分で例外クラスを作りそれを使うことも可能です。
    
    自分で作った例外クラスはraiseとともに使うのですが、既存の例外クラスよりも「自分がわざと発生させた例外」を扱うには行儀がいいです。
    
    なぜなら既存の例外クラスは本来の利用用途があり、それは自分が意図的に発生させた例外とは目的が異なるからです。
    
    さっそく例外クラスを作って、使ってみます。

'''

class MyError(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)
        
try:
    raise MyError("my error happens")
    
except MyError as e:
    print(type(e))
    
    print(e)

'''
    Exceptionクラスを継承してMyErrorクラスを作っています。名前は基本的には「なんとかError」とするのが通例です。
    
    継承の詳細は割愛しますが、正直なところ名前以外のコードは完全にコピペするか、もしくはコンストラクタの引数あたりを少しいじる程度になると思います。
    
    そして raiseで発生されたこのクラスの例外はexceptで同じ例外クラス(もしくは親クラス)を指定してエラーをキャッチしています。
    
    エラーの名前が適切であれば、かなり行儀がいいコードだと思います。
    
    これを実行すると以下のような出力が得られます。
    
    <class '__main__.MyError'>
    'my error happens'
    
    基本的には既存の例外クラスとほぼ同じ使い方です。
    
    自分で例外クラスを作る場合でも、あまり複雑な実装をせずに名前だけで区別するのが通例のようです。
    
    ただ、どの例外クラスを継承して自分の例外クラスを作るかには気を配る必要があります。
    
    例えば計算エラー関係の例外クラスを自分で作るのであれば、それを IOErrorから作るのは間違った判断です。
    
    難しいことを考えたくないのであれば、とりあえず Exceptionを継承することにしてください。

'''

'''
    例外クラスの体系
    
    例外クラスは BaseExceptionを起源として様々なものが存在しています。
    
    数が多いので全てを覚える必要はないのですが、おおまかな体系だけは把握することが望ましいです。
    
    以下に Python3の例外クラスの継承関係の図を示します。
    
    BaseException、Exception、OSError、lookupErrorが覚えておきたい例外クラスです。
    
    BaseException - Exception       - ArithmeticError - ZeroDivisionError
                  |                 |                 |
                  - SystemExit      |                 - OverflowError
                  - keybordinterrupt- OSError         - FileNotFoundError
                  |                 |                 -TimeoutError
                                    - lookupError     - indexError
                                    |                 -keyError
                                    
    図を見ていただくとわかりますが BaseExceptionから派生した例外クラスは Exception以外にもいくつかあります。
    
    ただ、それらの名前は Errorで終わっていないことがわかります。
    
    これらの例外は基本的に例外処理の対象とはしません。
    
    例外処理のメインとなるのは Exceptionクラスの子クラスとなり、一部の例外はあるもののそれらには共通して「なんとかError」という名前がついています。
    
    例外処理をする際は、このクラスの継承関係を意識しながら「処理したい例外もしくはその親クラス」で例外を処理するようにしてください。
    
    実は例外クラスを省略して try/catchを使うことができます。
    
    ただ、その場合は暗黙的に BaseExceptionを対象として例外処理がされるため、可能な限り利用は避けて下さい。
    
    例えば以下のコードですとpythonのプログラムを終了する exit関数ですら例外として処理されてしまいます。
    
'''

try:
    exit()
    
except:
    print("error")
    
'''
    自分が意図していない例外処理が働いてしまわないように注意をしてください。
'''

'''
    高度な例外処理例外処理の場合分け例外処理の文法は tryexceptだけでなく、elseとfinallyがあります。
    
    それぞれtryやexceptと同じような構文を持っており、その役割を簡単に説明すると以下のようになります。
    
    else:例外が発生しなかった場合のみ処理される
    finally:例外が発生してもしなくても処理される

    正直なところ、elseと finallyの使いどころはあまり多くないのですが、elseは例外が発生しなかった場合の処理に使い、finallyは必ず実施したい処理がある場合に使います。
    
    使いどころがなかなか難しく、私は「あえてこの処理をします」という表明の目的以外では両者を使いません。
    
    たとえば、オープンしたファイルをfinallyでクローズするということは言語を問わずよく実施されますが、try/catchを抜けた箇所でのクローズでもだいたいカバーできます。
    
    ただ、finallyにあえてクローズ処理を書くことで、「このtry/catchでファイルの資源を開放することを保証します」ということが、ほかの人にも伝わるようになります。
    
    elseと finallyがどのように動くかコードで確認してみます。テスト用のコードは以前利用したものとほぼ同じですが、今回はelseとfinallyが追加されています。

'''

try:
    print("1: start of try")
    
    5 / 0
    
    print("2: end of try")
    
except Exception:
    print("3: erro happens")
    
else:
    print("4: erro doesn't happen")
    
finally:
    print("5: finally")

'''
    注目して欲しいのは、例外が発生したあとにどの処理が実行されているかということです。
    
    とりあえず実行してみます。
    
    #python3 test.py
    1:startoftry
    3:errorhappens
    5:finally
    
    例外が発生して、exceptの処理とfinallyの処理が実行されていることがわかります。
    
    一方 elseの処理は実行されていないことも分かります。
    
    次に、例外を発生させなくした場合です。
    
    0による除算をコメントアウトします。

'''

try:
    print("1: start of try")
    
    # 5 / 0
    
    print("2: end of try")
    
except Exception:
    print("3: erro happens")
    
else:
    print("4: erro doesn't happen")
    
finally:
    print("5: finally")

'''
    これを実行すると以下のようになります。
    
    #python3 test.py
    
    1: start of try
    2: end of try
    4: erro doesn't happen
    5: finally
    
    今度はexceptが呼ばれなくなり、代わりにelseが呼ばれています。一方、finallyはまたもや呼ばれています。
    
    それほど複雑な動きではないと思うので、elseとfinallyの話はこのあたりで終わりとします 。

'''

'''
    スタックトレースtry/exceptで例外をキャッチできることはわかりました。
    
    ただ、やみくもに例外をキャッチするのは正直なところあまり行儀はよくないので、「正しくエラーをキャッチ」してあげる必要があります。
    
    たとえば、以下のコードがあるとしましょう。

'''

try:
    5 / 0
    
    a = [1, 2, 3]
    
    print(a[3])
    
except Exception:
    print("error happens")
    
'''
    このコードではいつものように5/0でエラーが起きますが、それをコメントアウトしてもその後のリストの範囲外へのアクセスでエラーが発生します。
    
    このコードには問題があるためエラーの発生自体は仕方がないのですが、このコードで問題となるのは以下の様な点です。
    
    ・はたして0除算とリストの範囲外へのアクセスを同等に扱うべきか
    ・そもそもこれは「例外処理」で対処するのではなくバグ修正すべき
    
    今回のような短いコードであればすぐに問題は見つかるかもしれませんが、実際にはもっと長く複雑なコードがひとつのtryのカバー範囲になります。
    
    そのため「何が原因で、どこでどのようなエラーが発生したのか」を正確に把握することは難しいです。
    
    単にtry/catchを使うだけでなく、エラーの原因を把握できれば、「何を修正すべき」か、「どのような例外クラスを使うべきか」がよくわかります。
    
    実はこの原因と問題の把握は、try/catchを利用していなければできていました。
    
    たとえば上記コードのtry/catchを外して実行すると、5/0を実行した際に処理の中断とともに以下のようなエラー出力が得られてどこで何が発生していたのか一目でわかります。

    $ python3 test.py
    
    Traceback (most recent call last):
        File "test.py", line 1, in <module>
            5 / 0
    ZeroDivisionError: division by zero
    
    また、a[3]での範囲街のアクセスも以下のようにエラー原因が一目瞭然でわかります。
    
    $ python3 test.py
    
    Traceback (most recent call last):
        File "test.py", line 2, in <module>
            a[3]
    IndexError: list index out of range
    
    こういったエラー出力はスタックトレース(stacktrace)と呼ばれていて、コードのどこでどういうふうに失敗したかを詳細に出力してくれます。
    
    もう少し詳細なトレースを見てみます。
    
    以下のようなコードがあるとしましょう。
    
    分かりやすいように行数付きで書いています。

    1   classA:
    2     deftest(self,b):
    3       returnb.div(0)
    4
    5   classB:
    6     defdiv(self,value):
    7       return5/value
    8
    9   a=A()
10   b=B()
11   value=a.test(b)

このコードを実行すると最終的に 0による割り算が発生してエラーとなってしまいます。実行すると以下のようなエラー出力が得られました。

$ python3 test.py
Traceback (most recent call last):
 File "test.py", line 11, in <module>
    value=a.test(b)
 File "test.py", line 3, intest
    returnb.div(0)
 File "test.py", line 7, indiv
    return 5 / value
ZeroDivisionError: division by zero

このエラーを上から読むと 11行目で “value=a.test(b)”を実行し、3行目で” returnb.div(0)”を実行し、7行目で “return5/value”を実行し、そこで ZeroDivisionErrorとなったことが分かります。

'''

'''
    tracebackモジュール
    
    先ほど説明した「エラーを変数に格納し出力する」ことである程度の詳細を得ることは可能です。
    
    ただ、より詳細を把握したい場合は tracebackモジュールを使ってプログラムを停止することなくスタックトレースを取得すると便利です。
    
    サンプルコードを以下に記載します。

'''

import traceback

print(1)

try:
    print(2)
    
    5 / 0
    
    print(3)
    
except Exception:
    print(4)
    
    #文字列で取得
    
    text = traceback.format_exc()
    
    print(text)
    
    #ファイルに書き込み
    
    f = open("error.log", "a")
    
    traceback.print_exc(file = f)
    
print(5)

'''
    上記では tracebackモジュールの関数を2つ使っています。ひとつめの format_exc()関数はスタックトレースを文字列として返し、2つめのprint_exc()は渡されたファイルオブジェクトにスタックトレースを書き込みます。上記の実行結果は以下となります。

    $ python3 test.py
    1
    2
    4
    Traceback (most recent call last):
     File "test.py", line 6, in <module>
        5 / 0
    ZeroDivisionError: division by zero
    
    5

    また上記スタックトレースと同じ内容が書かれたファイルも作成されています。
    
    プログラムの標準出力ではなくログファイルに出力する際にはこの機能を使うか、もしくは loggingモジュールを使ってエラーの文字列をファイルに書くのがよいと思います。

 '''

'''
    キャッチした例外の丸投げ先に説明したraiseなのですが、もうひとつ別の使い方があります。
    
    それは「exceptの中で呼び出すことで、エラーを呼び出し元で処理してもらう」というものです。
    
    以下のコードを見てください。

'''

def fun1():
    try:
        raise Exception("error in fun1()")
        
    except:
        print("1: fun2 can't handle this error")
        
        #同じエラーを投げる
        
        raise

def fun2():
    try:
        print("2: call fun1")
        
        fun1()
        
        print("3: done")
        
    except Exception as e:
        print("4: catch error which happens in fun1()")
        
        print(e)
        
fun2()

'''
    関数fun2()はfun1()をその内部で呼び出しています。fun1()内部でエラーを発生させて自ら exceptでそれを受け取っていますが、そのexceptの中でraiseをしています。
    
    こうすると同じエラーが再発生するので、実質的に「呼び出し元に処理を依頼する」ことになります。
    
    一応try/exceptでエラーをハンドルしようとしたけれども「ここでは対処しきれないエラーなので、呼び出し元で例外処理をしてもらう」というような場合で同じエラーを再度 raiseします。
    
    これを実行すると以下のような出力になります。

    $ python3 test.py
    
    2: call fun1
    1: fun can't handle this error
    4: catch erro which happens in fun1()
    erro in fun1()
    
    fun1()の中で再度 raiseされたエラーを fun2()が受け取っているので、例外のメッセージがオリジナルのもののままになっています。
    
    なお、例外を処理しきれない場合は raiseで同じものを再度発生させるのではなく別のエラーを raiseさせても構いません。
    
    例えば適切なエラーメッセージに更新して再度 raiseするというのはいいアイデアかもしれません。
    
'''
