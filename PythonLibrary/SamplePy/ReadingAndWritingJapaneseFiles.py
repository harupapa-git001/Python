'''
    日本語ファイルの読み書きファイルの入出力にはcodecsパッケージのopen関数を使うのが簡単です。
    
    これを使って文字コードを指定してファイルをオープンすると、通常のファイル入出力の手順と大差なくマルチバイト文字を扱えます。
    
    具体的には readをすると文字コードを意識してファイルのテキストを読み込んでユニコードの文字列を返し、writeでユニコードの文字列を書き出すとそれが指定された文字コードでファイルに書かれます。
    
    以下にこの流れを記載します。

    上記の「ファイル名」は読み書きするファイル名を相対パスなり絶対パスなりで指定し、「モード」は通常の open関数と同じで r,w,rw,aなどを指定します。
    
    そして最後の「文字コード」で読み書きするファイルのエンコードを指定します。
    
    この open関数のみ文字コードを意識する必要がありますが、それ以外の readや writeは今までのファイルの読み書きと同じです。
    
    ShiftJisとして読み込みを行えば、readをすれば ShiftJisとしてファイルの中身を読み込んで、それをユニコードの文字列として返します。
    
    書き出しも同様です。
    
    実際にコードで確認してみます。
    
    文字コードutf8で書かれた以下のファイル utf8.txtを作成してください。

    このファイルを読み込み処理するコードは以下となります。

'''

import codecs

f = codecs.open("utf8.txt", "r", "utf-8")

for line in f:
    print(line, end = '')

f.close()

'''
    先程説明したようにcodecs.open関数の第一引数でファイル名を指定し、第二引数でオープンのモード(今回はread)を選択、そして第三の引数でファイルの文字コードを指定しています。それ以外は通常のファイル読み込みと同じです。

    変数 lineに格納されているファイルから読み込まれたデータは通常の文字列型です。
    
    読み込んだあとは文字コードを気にする必要は一切ありません。
    
    次に書き込みをしてみます。
    
    このutf8のファイルをShift-JISで書きだしてみます。

'''

import codecs

fin = codecs.open("utf8.txt", "r", "utf-8")

fout = codecs.open("sjis.txt", "w", "sjis")

for line in fin:
    fout.write(line)
    
fin.close()

fout.close()

'''
    ファイルのオープン時にオープンモードをwにすることで書き込みファイルとして開いています。
    
    オープンしたファイルに対してUnicode文字列をwriteしてあげればファイルに文字列が追加されます。
    
    結果を確認してみます。
    
    ファイルのエンコーディングの判定をしてみます。

'''

'''
#ターミナルで確認してください。（nkfコマンドはインストールをしないと使えないので注意してください。）
$ （入力部→）nkf --guess utf8.txt

UTF-8(LF)

$ （入力部→）nkf --guess sjis.txt

Shift_JIS(LF)

'''

'''
    書き込みファイルsjis.txtの文字コードがShiftJisと判定されています。
    
    UTF8のファイルを読み取り、それを解釈、ShiftJisとして書き込むという動作がうまく動いています。
    
    なお上記の nkfコマンドはインストールをしないと使えないので注意してください。

'''
