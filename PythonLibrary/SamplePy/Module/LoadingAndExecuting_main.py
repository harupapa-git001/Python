'''
    モジュールの読み込みと実行Pythonはモジュールを読み込む際に実行をしています。そのため、先程までのような関数のみのモジュールを importしても全く影響はありませんが、特定の処理をするコードを書くとそれが実行されてしまいます。例えば以下の関数を定義しているモジュール util.pyですが、これを importするだけで 4行目が実行されて testと出力されてしまいます。

    def test():
    print("test")

'''

import util

util.test()

'''
    そのため、モジュールとして読み込まれることを想定して開発された Pythonのプログラムファイルは実行されるコードを含まないべきです。
    モジュールを読み込んだ際になんらかの初期化処理が必要な場合でも関数などとして提供するほうが行儀はいいです。
    なぜなら importをする側は importをするだけで勝手になんらかの処理をすると想定していないからです。
    ただ、モジュールがプログラムの起点になることもあれば importされることもあるという場合は「起点となる場合はある処理をする」一方、「モジュールとして呼び出される場合はそれをしない」という実装が必要なことがあります。
    
       これを実現するには特殊な変数 __name__を使います。
    これは特殊属性(詳細は本シリーズの下編にて扱います)と呼ばれる高度なトピックなのですが、難しいことは考えずにこれにはモジュール名が入っていると認識して下さい。
    たとえば util.pyをモジュールとして読み込めば utilとなりますし、testmodule.pyを読み込めば testmoduleとなります。
    ただし、一つ例外がありプログラムの起点となるプログラムはモジュール名がファイル名ではなく __main__となります。


    せっかくなので実際に試してみます。以下の3つのファイルで実行してみてください。

    hello.py(実行ファイル)
    nice.py(呼び出しファイル)
    world.py(呼び出しファイル)
'''
