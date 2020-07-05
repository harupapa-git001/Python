'''
    ５．threading
    
    "threading"は複数スレッドの実行（並列処理）を手軽に扱うためのライブラリです。
    
    並列処理したい関数を引数に設定して"threading.Thread"クラスのインスタンスを作ると、start関数で処理を実行させることができます。

'''
#並列処理

import time

import threading

def fnc():
    for i in range(0, 4):
        time.sleep(1)
        
        print("count", i)
        
thread1 = threading.Thread(target= fnc)

thread2 = threading.Thread(target = fnc)

thread1.start()

time.sleep(0.1)

thread2.start()

'''
    この処理は"threading.Thread"クラスを継承した自作クラスを使う方法でも実現できます。
    
'''
#スレッド用クラスの作成

import time

import threading

class My_Thread(threading.Thread):
    def __init__(self):
        super(My_Thread, self).__init__()
        
    def run(self):
        for i in range(0, 4):
            time. sleep(1)
            
            print("count", i)
            
thread1 = My_Thread()

thread2 = My_Thread()

thread1.start()

time.sleep(0.1)

thread2.start()

'''
    並列処理の規模が小さければ前者、複雑であれば後者での実装が良いでしょう。

'''
