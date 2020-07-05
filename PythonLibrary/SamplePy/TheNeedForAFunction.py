'''ex1

def my_abs(x):
    if(x >= 0):
    
        return x
    
    else:
        return x * -1

        
print(my_abs(5))

print(my_abs(-3.3))

'''

'''ex2

#引数がない関数
def my_func1():
    return 0

#返り値がない関数
def my_func2(x):

    x = x * -1
    
    #値を返す場合にはreturnを使う
    
    #return x

print(my_func1())

print(my_func2(5))

'''

def my_func3(x, y):
    print("A")
    
    if(x > y):
        return x
        
    print("B")
    return y
    
print(my_func3(5, 1))

print(my_func3(2, 4))
