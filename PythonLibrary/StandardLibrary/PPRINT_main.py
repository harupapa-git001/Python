'''
    ３．pprint
    
    "pprint"はデータ構造を見やすい形で出力するためのライブラリです。
    
    名前の由来は「prettyprinter」だそうです。

'''

from pprint import pprint

#data = [(i, {"nya": "NYA-", "wan": "WA-N"}) for i in range(3)] #下記表記法（"と'の違い）に注意（デバッグに苦戦しました）

data = [(i, {"nya': 'NYA-", "wan': 'WA-N"}) for i in range(3)]

# printで出力
    
print(data)
    
# pprintで出力
    
pprint(data)

'''
    ※必ずPPRINT_main.pyのないディレクトリでターミナル（pythonコマンド実行）やpprintをimportしてください。
    
    ターミナル上でこのPPRINT_main.pyファイルは読み込めません。（PPRINT.pyファイルが同じディレクトリにある時はモジュールとして読み込めます）
'''

from pprint import pprint

data = [(i, {"nya': 'NYA-", "wan' : 'WA-N"}) for i in range(3)]

pprint(data)

pprint(data, compact = True)
