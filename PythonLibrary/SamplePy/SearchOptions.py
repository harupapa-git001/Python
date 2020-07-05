import re

pattern = r"nya"
text = "nya-nya-Nya-"
res = re.findall(pattern, text, re.IGNORECASE)
print(res)


#上と同じ結果を得る

res = re.findall(pattern, text, re.I)
print(res)

'''
    Pythonで使用可能な検索オプションは次の通りです。
    
    ASCII, A
        \w, \b, \s,　そして\dなどをそれぞれのプロパティを持つASCII文字だけにマッチさせる
        
    IGNORECASE, I
        大文字小文字を区別しない
        
    MULTILINE, M
        ^ や $ に作用して複数行にマッチングさせる
        
    DOTALL, S
        . を改行を含む任意の文字にマッチするようにする
        
    VERBOSE, X
        冗長な正規表現を利用できるようにする
'''
