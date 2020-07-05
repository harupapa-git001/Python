a = 1

b = 2

if a == b:
    print("nya")
    
elif a > b:
    print("wan")
    
else:
    print("boo")

'''
    条件分岐条件分岐は"if"文を使います。
    
    基本的な書き方は次の通りです。

    "elif"は"elseif"の略であり、必要な条件の数だけ繰り返し記述することができます。
    
        また、"elif"と"else"は不要であれば省略できます。
    続いて、if文では「ある範囲に該当するか」の条件を１行で表現することができます。

'''

a = 10

if 0 < a < 10:
    print("nya")
    
else:
    print("wan")

'''
    最後に、if文では"in"演算子を使うことで複雑な条件分岐を簡潔に表現することができます。

'''

a = 3

if a == 1:
    print("nya")
    
elif a in (2, 3):   # aは(2, 3)に含まれる→True ＜3の前に1をつけて13にするとFalseとなり、下段elif a in (3, 4)でTrueとなる＞
    print("wan")
    
elif a in (3, 4):
    print("boo")
    
else:
    print("piyo")
