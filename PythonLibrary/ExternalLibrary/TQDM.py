'''
    13. tqdm
    
    "tqdm"は進捗バーを表示するためのライブラリです。
    
    本書ではバージョン4.19.5を使用します。
    
    #インストール
    
    ■Windows
    
    pip install tqdm
    
    ■macOS
    
    pip3 install tqdm
    
    このライブラリはループの進捗状況を視覚的に表示したりする際に利用します。
'''
#進捗バーの表示

from tqdm import tqdm

import time

for _ in tqdm(range(10)):
    time.sleep(1)

'''
    例では1秒毎に進捗バーを進めていますが、実際には時間のかかるループ処理に組み込むと良いでしょう。
    
    なお、動作環境によってはtqdmが表示する進捗バーが改行されない事もあるので注意してください。
    
'''
