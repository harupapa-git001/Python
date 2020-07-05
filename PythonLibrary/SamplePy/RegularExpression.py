import re

#match
#文字列の先頭のみ対象となる
#group()はマッチした値を取得するメソッド

pattern = "nya"
text = "nya-nya-"
res = re.match(pattern, text)
print("[match()の実行結果]")
print(res.group())

#search
#最初にマッチした部分のみが対象となる
#span()はマッチした箇所の開始位置と終了位置をタプルで取得するメソッド
#group()はmatchと同様

res = re.search(pattern, text)
print("\n[search()の実行結果]")
print(res.span(), res.group())

#findall
#戻り値はリストになる

res = re.findall(pattern, text)
print("\n[findall()の実行結果]")

if res:
    print(res)
    
#finditer
#戻り値はイテレータオブジェクトとなるため
#span()やgroup()などのメソッドが利用可能

res = re.finditer(pattern, text)
print("\n[finditer()の実行結果]")

for v in res:
    print(v.span(), v.group())
    
#split
#戻り値はリストになる

res = re.split(",", "nya,n,nya,n")
print("\n[split()の実行結果]")

if res:
    print(res)
    
#sup
#マッチ部分が全て置換対象となる

res = re.sub(pattern, "zz", "nyaonyao")
print("\n[sub()の実行結果]")

if res:
    print(res)

'''
    他の言語では「正規表現 = match」だと思いますが、Pythonでは"search"が最も利用頻度が高いメソッドです。
    
    match(pattern, string)
        文字列の先頭が正規表現とマッチするか判定する
    
    search(pattern, string)
        文字列を走査して正規表現がどこにマッチするか調べる
        
    findall(pattern, string)
        正規表現にマッチする部分文字列全てをリストとして返却する
        
    finditer(pattern, string)
        正規表現にマッチする部分文字列全てをiteratorとして返却する
        
    split(pattern, string)
        正規表現にマッチする部分ごとに分割する
        
    sub(pattern, repl, string)
        正規表現にマッチする部分を置換する
'''
