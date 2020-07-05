'''
    バイト配列
    
    文字コードだけでなく様々なデータは全て「0,1の羅列」で表現されています。
    
    この0,1の羅列のことをバイト列といい、Pythonはそれを bytesという型で扱います。
    
    バイト列は文字列やリストと似たようなシーケンスとして処理ができますが C言語などと違ってPythonでバイト配列を直接扱う機会は多くないと思います。
    
    ただ、プログラミングの基礎概念として知っておくべき内容であるため、簡単に説明します。
    
    バイト列の宣言は文字列とほぼ同じように行いますが、シングルクオテーション等の前に bと宣言します。
    
    例えば以下のようになります。

'''

b = b"hello world"

print(type(b))

'''
    上記例では ‘helloworld’を文字列としてではなく、バイト列として扱います。
    
    そのため、変数 bは文字列型ではなくバイト型のオブジェクトを持っています。
    
    バイト型のオブジェクトも当然ながらメソッドを持っており、hexを使うとバイト列を 16進数の文字列で返します。

'''
print(b.hex())

'''
    68>h,65>e,6c>l,6c> lというように Ascii表に沿って上記の16進数をアルファベットに変換していくと helloworldになります。
    
    16進数の文字列をbyte型に変換するには bytesクラスの fromhexメソッドを使います。

'''

print(bytes.fromhex("68656c6f20776f726c64"))

'''
    文字列とバイト列の変換は encodeと decodeメソッドを使います。

'''

print("hello world".encode())

print(b"hello world".decode())

'''
    文字列に対してメソッド encode()を呼び出すとバイト列を返し、バイト列に対して decodeメソッドを呼び出すと文字列を返します。

'''