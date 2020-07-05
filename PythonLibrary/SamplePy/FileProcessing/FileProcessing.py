'''
    ファイル処理ファイル処理については、プログラミングというよりも「OSのファイル処理の方式」をまず理解しておく必要があります。
    
    そのため、最初にファイル処理の概念について説明します。
    
    これがわかってしまえば、その利用はさほど難しくありません。
    
    なお、プログラムがどのようにファイルを扱うかは、OSの仕組みにもとづいているため、多くのプログラミング言語でさほど変わりません。
    
    ファイル処理がOSにおいてどう実現されているかを抽象化すると以下の図のようになります。
    
    実際はもっと複雑ですが、通常のプログラミングではそこまで意識する必要はないので詳細は割愛します。

    まずご存知のようにOSにはディレクトリがあり、それが階層構造を作っています。ファイルはそのディレクトリのなかに保存されています。
    
     ディレクトリやファイルは、サイズなどの情報と共にポインタのようなものを持っていて、それがファイルの実体を指しています。
     
     構造についての話はこれぐらいにして、実際にファイルをどのように処理するか話をしましょう。
     
     OSにおけるファイル処理は主に以下のような流れとなります。

    まず絶対パス(ルートやCドライブなどからのパス)や相対パス(現在いるディレクトリから指し示すパス)を使ってファイルを指定します。それに対して読み、書き、読み書きなどのモードを指定してファイルをオープンします。
    
    そして読み書きなどの必要な処理を繰り返し、処理がすべて完了したらファイルをクローズして終わりです。
    
    読み書きなどの具体的な処理はそれほど難しくありません。
    
    一言でいってしまえば、「テキストファイルは行ごとに処理する」「バイナリファイルは先頭から何バイトめか(位置)を指定して処理する」ことです。たとえば、テキストファイルで以下のものがあるとします。


    world

    python

    java

    この内容にすべて"hello "を加えて画面に表示するというプログラムを書く場合、ループ処理を利用して以下のことを繰り返して処理するのが一般的です。
    
    1. 行の内容を取得
    2. helloに行の内容を追加しprint
    3. 次の行に進む
    
    「テキストファイルは行ごとに処理する」のが基本であることを覚えておいてください。
    
    バイナリファイルの扱いは後ほど簡単に扱いますが、Pythonでそれを専用ライブラリなしにやることはかなり稀かと思います。
    
    私が過去にバイナリファイルを操作した際に利用した言語は Cもしくは ObjectiveCでした。

'''
