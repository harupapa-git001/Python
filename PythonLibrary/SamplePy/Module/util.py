# util.py

def say_hello():
    print("hello!")
    
def say_python():
    print("python!")
    
'''
    上記が呼び出される側の Pythonのプログラムです。2つの関数が定義されています。
    
        そしてutil_main.pyがそれを呼び出す側の Pythonのプログラムです。

'''# Reload_main.pyで呼び出すクラス

def reload_hello():
    print("hello!" * 3)
    
def reload_python():
    print("python!" * 3)

# LoadingAndExecuting_main.pyで呼び出すクラス

def test():
    print("test")
