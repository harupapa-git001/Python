'''
    １５．logging
    
    "logging"はログ出力をするためのライブラリです。
    
    ログはデフォルトではコンソールに表示されますが、ファイルに出力させることもできます。

'''
#ログの出力

import logging

#ログの出力

logging.warning("これはログです")

#ログをファイルに出力

import logging

#出力先をファイルに変更する

logging.basicConfig(filename = "logging.log")

logging.error("これはログです")    #下記注意事項をお読みください

#出力レベルの変更

import logging

#出力レベルの変更（デフォルトレベルはWARNING）

logging.basicConfig(level = logging.DEBUG)

logging.debug("これは出力されます")

'''
    ※loggingとloggerなどの間に様々な不具合要素があるため、ログ関係の処理は調べてから行ってください。
    
    （logging ライブラリが標準のものから logzero という3rd partyのものに変わっています。＜検索サイト内更新日2018/8/31＞）
    
'''
