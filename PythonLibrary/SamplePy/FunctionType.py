#関数の定義

def test():
    return 1
    
print("call test: {}".format(test()))

print("type test: {}".format(type(test)))


#関数を変数に代入

test2 = test

print("call test2: {}".format(test2()))

print("type test2: {}".format(type(test2)))

'''
    型が'function'とでていて、関数型であることがわかります。
    そしてオブジェクトであるため変数への代入もできており、なおかつそれを呼び出すこともできます。
    しかし、関数も型だとわかったところで、実際にどのように使うか想像がつかないかもしれません。

        関数渡し（FunctionPassing.py）をご参照ください。
'''
