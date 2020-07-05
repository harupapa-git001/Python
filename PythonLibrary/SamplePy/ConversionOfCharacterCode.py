'''
    文字コードの変換先ほど見たように文字コードもバイト列で作られています。
    
    例えば UTF8の文字列を ShiftJisに変換するといった場合、このバイト列の処理が必要になります。
    
    実際は Pythonのライブラリ任せになるのでそれほど難しくありませんが、おおまかに以下のような文字列とバイト列の関係の認識を持ってもらうと分かりやすいです。

    まず Pythonは文字列としてユニコード(UTF8)を持ちます。
    
    一方、バイト列は単なる 0,1の組み合わせですのでどのような文字コードでも持つことができます。
    
    先程説明した文字列の encode及びバイト列の decodeメソッドを文字コードという引数付きで使うことでこの変換ができます。
    
    文字列から ShiftJisの変換は簡単で、単に encodeする際に引数に ShiftJISを指定して ShiftJISのバイト列に変換するだけです。
    
    ShiftJISから EUCJPへの変換も、ShiftJISを引数 shiftjisで decodeし、ユニコードの文字列にし、それから引数 eucjp で encodeしてあげれば EUCJPのバイト列が得られます。
    
    上記変換のサンプルを以下に記載します。

'''

text = "こんにちは"

unicode_bytes = text.encode()

print(unicode_bytes)

print(unicode_bytes.decode())

sjis_bytes = text.encode("sjis")

print(sjis_bytes)

print(sjis_bytes.decode("sjis"))

eucjp_bytes = text.encode("euc-jp")

print(eucjp_bytes)

print(eucjp_bytes.decode("euc-jp"))

'''
    文字列はユニコードであり、エンコードを指定してバイト列を書き出すことで様々な文字コードを表現できる。
    
    それらをエンコードの指定をして読み込むことでPythonのユニコード文字列に変換することができる。
    
    このの流れは日本語以外にもあてはまりますので覚えておいて下さい。

'''
