#ex1 時刻付きログの表示を目指す。まずは現在時刻表示とスリープ時間の設定。
#timeモジュールをインポート
import time

#現在時刻を得る
print(time.ctime())
"Wed Aug 24 08:37:28 2016"

#x秒間スリープする
print(time.ctime()); time.sleep(5);
print(time.ctime())

#ex2-1 write_logメソッドを呼ばれるリスト型のインスタンス変数のlogに与えられたログを時刻付きで追加し、get_logメソッドが呼ばれると、追加されてきたログ全てを改行コードで結合して文字列として返す。（secretary.pyに書かれることを想定）
import time

class Secretary:
    def __init__(self):
        self.log = []
    
    def write_log(self, text):
        self.log.append("{}: {}".format(time.ctime(), text))
        
    def get_log(self):
        return "\n".join(self.log)

#ex3（ex2-2） secretary.pyを読み込んで処理（ex1、ex2をsecretary.pyに移動の形を想定）
import time

from secretary import*

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
