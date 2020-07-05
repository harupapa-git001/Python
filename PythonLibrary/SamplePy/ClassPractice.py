class MyClass:
    def __init__(self, a, b):
        #外から使うためset, getメソッドを用意
        
        self.__a = a
        #中だけで使う
        self.__b = b
        
    def set_a(self, a):
        self.__a = a
        
    def get_a(self):
        return self.__a

'''
    上記においてインスタンス変数__aは外から操作する必要があるもので、__bは完全に内部の変数だとします。
    その際、__aの値を設定するメソッドset_aと取得するメソッドget_aが実装されています。__bについては外から触れる必要がないので、それらは用意されていません。
        
    このようなことをせずインスタンス変数__aのみ変数aとして直接外に見せることも可能です。ただ、セッターゲッターメソッドを提供することで「setされる値が期待されるものかチェックができる」「返す値が期待されなければ例外を発生させられる」といった使い方ができます。
       
       デコレーターと呼ばれるテクニックで上記を実現する方法もあります。
       
    なお、セッターやゲッターはあくまでも厳密にオブジェクト思考を守る場合に使います。厳格に守ることによってPythonらしい簡潔なコードのメリットが弱くなってしまうので、どこまでルールを順守するかは議論が分かれるところかもしれません。
'''