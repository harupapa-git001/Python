a = None

"None" if a is None else "not None"

print(a)

'''
    NoneNoneは「値が存在しない」ことを表すための組み込み"定数"で、言語によっては「null」「nil」などと呼ばれます。
    Noneに何らかの値を代入しようとするとSyntaxErrorとなります（他にもTrueやFalseが同様にエラーになります）。
    
        オブジェクトがNoneかどうかを判定するには"is"演算子を使います。
    "=="で比較している処理も稀に見かけますが、PEP8にも"is"を使うよう記載されているため、これに従っておけば問題ありません。

'''
