'''
    エスケープ記号最後に文字列で使われる特殊記号についてお話します。
    
    特殊記号はプログラム中で意味を持ってしまう特別な記号のことです。
    
    たとえば「'」という記号は文字列を作成する際に利用する特別な記号です。
    
    そのほかにはビープ音なども記号に分類されます。
    これらは文法的な理由やそもそもそれを表現する記号がキーボードのキーにないことから、「これは XXですよ」という特別なルールにもとづいて文字列に表記します。
    そのルールに利用されるのがエスケープ記号と呼ばれるもので半角のバックスラッシュ「\」(英語キーボード)か、半角の円記号「¥」(日本語キーボード)を利用します。
    このエスケープ記号の後に特別な文字を続けることで、それが特別な意味を持つのです。
    
       たとえば「'」とビープ音は以下のように記載できます。

'''

print("escape sample1 \'.")

print("escape sample2 \a.")

print("escape sample1 \n.")

print("escape sample1 \\.")