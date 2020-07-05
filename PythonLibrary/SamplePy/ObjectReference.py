a = [1, 2, 3]

b = a

a.append(4)

print("a: " + str(a))

print("b: " + str(b))

'''
    リストのオブジェクトに対して appendメソッドを呼び出すと、リストの末尾に要素を追加することができます。
    appendしたあとの print出力を見ると変数 aに格納されているリストオブジェクトのデータがアップデートされています。
    そして変数bに格納されているリストオブジェクトは変数aのものと同じなので、変数b自体に対しては操作をしていないのに中身が変わっていることがわかります。
    変数に対する操作は変数が格納しているオブジェクトに対する操作だといえます。
    その変数にどのオブジェクトが入っているかは常に意識するようにしてください。
    自分が意図していないところでオブジェクトが操作されてしまっていて、使うときに問題がおきるというのはよくあるトラブルです。


'''