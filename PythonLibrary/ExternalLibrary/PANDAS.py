'''
    6. pandas
    
    "pandas"はデータ分析用の外部ライブラリです。
    
    本書ではバージョン0.22.0を扱います。
    
    #インストール
    
    ■Windows
    
    pip install pandas
    
    ■macOS
    
    pip3 install pandas
    
    このライブラリは実に多様な「分析」を行うことが可能ですが、本書ではpandasuを使ってCSVファイルを扱う方法を紹介します。
    
    単純なファイルの読み書き程度であれば先に説明した"csv"を利用すべきですが、読み込んだファイルの内容をもとに色々な処理を行いたい場合はpandasの方が有利な場面が多いでしょう。
    
'''
#CSVファイルの書き込み

import pandas as pd

#データフレームの作成

df = pd.DataFrame([
    ["001", "nya", "神奈川"],
    ["002", "wan", "沖縄"],
    ["003", "piyo", "スペイン"]],
    columns = ["ID", "名前", "出身地"])
    
#CSVファイルの作成

df.to_csv("pandas.csv", index = False)

'''
    pandasでは"DataFrame"関数で「データフレーム」を作ってそれをもとにCSVファイルを作成します。
    
    データフレームを作成する際、"columns"を指定しないと先頭行が自動的に「ヘッダ」として扱われます。
    
    また、"to_csv"メソッドでCSVファイルを作成する際は、"index = False"を指定しないと行の先頭にインデックスが付与されます。
    
'''
#CSVファイルの読み込み

import pandas as pd

#CSVファイルを読み込む

data = pd.read_csv("pandas.csv")

print(data)

#特定の値を取得する

val = data.loc[1, ["名前"]]

print(val[0])

#インデックスカラムを指定する

data = pd.read_csv("pandas.csv", index_col = "ID")

print(data)

'''
    CSVファイルは"read_csv"関数で読み込みます。
    
    この関数は自動的に先頭行を「ヘッダ」として解釈するので、ヘッダがないファイルの場合には引数に"header = None"を指定します。
    
    また、"index_col"でインデックスカラムを指定しないと行の先頭に自動的にインデックスが付与されます。
'''
