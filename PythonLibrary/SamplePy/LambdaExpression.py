'''
    ８．lambda式
    
    ６．関数でも説明しましたが、lambda式（ラムダ式）は「関数を式として扱う」ための仕組みです。
    
    これはPython固有の仕組みではなく、関数型プログラミングが可能な言語には比較的用意されています。
    
    そしてこれも前述していますが、Pythonではlambda式を"lambda引数:戻り値"の書式で扱います。
    
    引数は省略可能で、複数個指定することも可能です。

'''
#lambda式

#引数なしのlambda式

hello = lambda: "hello!"

hello()

print(hello())

#引数がひとつのlambda式

increment = lambda x: x + 1

increment(10)

print(increment(10))

#引数が二つのlambda式

multipl = lambda x, y: x * y

multipl(2, 3)

print(multipl(2, 3))

'''
    続いて、lambda式と組み込み関数を使った実践的なテクニックをいくつか紹介します。
    
    ■filter関数の利用
    
    filter関数はリストなどから要素を抽出するための関数です。
    
    この関数は、第一引数に要素内の各値に対して処理を行うための関数を、第二引数にリストなどの要素を指定します。
    
    そして、第一引数に指定する関数は使い捨てであることが多いため、ここにlambda式を指定することで記述の無駄を減らすことができます（要するに無名関数として利用すると言うことです）。

'''
#filter関数とlambda式

#filter関数のみ

def check(v):
    return True if v > 250000 else False
    
salary = [250000, 300000, 350000]

high_salary = list(filter(check, salary))

print(high_salary)  #[300000, 350000]

#filter関数とlambda式

salary = [250000, 300000, 350000]

high_salary = list(filter(lambda s: s > 250000, salary))

print(high_salary)  #[300000, 350000]

'''
    ■map関数の利用

    map関数はリストなどの要素に一律同じ処理を行うための関数です。
    
    この関数でもfilterと同じようにlambda式を使うことで記述が簡潔になるケースがあります。

'''
#map関数とlambda式

#map関数のみ

def tax(v):
    return v * 1.08
    
tax_exclusion = [1000, 1500, 2000]

tax_included = list(map(tax, tax_exclusion))

print(tax_included) #[1080.0, 1620.0, 2160.0]

#map関数とlambda式

tax_exclusion = [1000, 1500, 2000]

tax_included = list(map(lambda t: t * 1.08, tax_exclusion))

print(tax_included) #[1080.0, 1620.0, 2160.0]

'''
    ■sorted関数の利用sorted関数はリストなどの要素をソートするための関数です。
    
    この関数は"key"と言う引数にソートに使う関数を指定できるので、その際にlambda式を利用することができます。

'''
#sorted関数とlambda式

#sorted関数のみ

def fnc(v):
    return v[1] #[(6, 1), (8, 2), (2, 3), (4, 4)]

before = [(6, 1), (2, 3), (4, 4), (8, 2)]

after = sorted(before, key = fnc)

print(after)

#sorted関数とlambda式

before = [(6, 1), (2, 3), (4, 4), (8, 2)]

after = sorted(before, key = lambda v: v[1])

print(after)    #[(6, 1), (8, 2), (2, 3), (4, 4)]
