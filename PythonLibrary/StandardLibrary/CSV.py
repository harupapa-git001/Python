'''
    ８．csv
    
    "csv"はCSVファイルを扱うためのライブラリです。
    
    単純なCSVファイルの読み書き程度なら、わざわざ外部ライブラリを導入せずともこれで十分です。

'''

'''
#CSVファイルの書き込み

import csv

try:
    #ファイルを開く
    
    with open("nya.csv", "w") as csvfile:
        
        #writerオブジェクトの作成
        
        writer = csv.writer(csvfile, lineterminator = "\n")
        
        #内容の書き込み
        
        writer.writerow(["a", "b", "c"])
        
        writer.writerow(["あ", "い", "う"])
        
except FileNotFoundError as e:
    print(e)
    
except csv.Error as e:
    print(e)
   
'''
'''
    "writer"関数でCSVファイルのwriterオブジェクトを取得し（lineterminatorは改行コードを指定します）、"writerow"関数で内容を書き込みます。
    
    CSVの書き込みでエラーが発生した場合は"csv.Error"でキャッチできます。

'''
#CSVファイルの読み込み

import csv

try:
    #ファイルを開く
    
    with open("nya.csv", "r") as csvfile:
    
        #readerオブジェクトの作成
        
        reader = csv.reader(csvfile, lineterminator = "\n")
        
        #内容の読み込み
        
        for r in reader:
            print(r)    #デバッグに苦戦しました
            
except FileNotFoundError as e:
    print(e)
        
except csv.Error as e:
    print(e)

'''
    CSVファイルの読み込みには"reader"関数でreaderオブジェクトを取得します。
    
    ポイントは書き込み処理と大差ありません。なお、読み書き共に区切り文字やクォート文字等の細かな指定も可能なので、必要であればそれらは公式ドキュメントをご覧ください。

'''
