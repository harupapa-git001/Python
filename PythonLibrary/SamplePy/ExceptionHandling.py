#例外のハンドリング

try:
    x = 1 / 0

except ZeroDivisionError as e:
    print(e)
    print(type(e))
    
except Exception as e:
    print(e)
    print(type(e))
    
finally:
    print('Finish!!')

'''
    なお、Pythonには多数の例外が用意されていますが、とりあえず抑えておきたい例外の種類は次の通りです。
    （ちなみに"Exception"クラスを指定すると全ての種類の例外を処理できます）

    ImportError         import文でモジュールのロードに失敗
    
    ModuleNotFoundError import文でモジュールが見つからない（ImportErrorのサブクラス）
    
    IndexError          シーケンスの添字が範囲外
    
    KeyError            辞書に指定したキーが存在しない
    
    RuntimeError        分類不能な例外
    
    SyntaxError         構文エラー
    
    IndentationError    インデントが不正な構文エラー（SyntaxErrorのサブクラス）
    
    UnicodeError        Unicodeに関するエンコードまたはデコードのエラー
    
    ZeroDivisionError   ゼロ除算
    
    FileExistsError     存在するファイルやディレクトリを作成しようとした
    
    FileNotFoundError   指定したファイルやディレクトリが存在しない
    
    PermissionError     アクセス権限不足

    最後に、プログラムから明示的に例外を発生させるには"raise"文を使用します。使い方は例で確認しましょう。

'''

try:
    raise RuntimeError("error!!")
    
except Exception as e:
    print(e)
    print(type(e))
