
#ex1 コンストラクタでログファイルのパスを設定し、write_logをすると新しいログを追記し、get_logをするとファイルを読み出して今までのログを返します。

import time

class Secretary:
    def __init__(self):
        self.logfile = "_log.txt"
        
    def write_log(self, text):
        log = "{}: {}\n".format(time,ctime(), text)
        f = open(self.logfile, "a")
        f.write(log)
        f.close()
        
    def get_log(self):
        f = open(self.logfile, "r")
        log = f.read()
        f.close()
        return log
        
#ex2
import time

#WorkOnSara.pyのex1、ex2をsecretary.pyに書くことを想定
#from secretary import*
from WorkOnSara import* #Pickle.pyとコード被りがある事を確認

class Manager:
    def __init__(self):
        self.sara = Secretary()
        
    def work_a(self):
        self.sara.write_log("hello")
        time.sleep(5)
        self.sara.write_log("hey")
        
    def work_b(self):
        print(self.sara.get_log())
        
bob = Manager()
bob.work_a()
bob.work_b()

'''
    __pycache__フォルダはひとつだけ残して残りは全て消してください
'''
