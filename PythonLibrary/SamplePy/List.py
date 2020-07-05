#リストで抑えておきたいメソッド
'''
    .append
    .extend
    .insert
    .remove
    .pop
    .clear
    .index
    .count
    .sort
    .reverse
    .copy
'''

a = [1, 2]

a.append(3)             #リストの末尾に指定した要素を追加する

print(a)#
a.extend([3, 4])        #指定したリストを連結する

print(a)#

a.insert(1, "x")     #位置を指定して要素を挿入する

print(a)#

a = [1, 2, 3]

a.remove(1)             #初の要素を削除する　※該当する要素がない場合はエラーとなる
print(a)#

print(a.pop(1))         #指定した位置に存在する要素を取り出して返却する

print(a)

a = [1, 2]

a.clear()               #全ての要素を削除する

print(a)#

a = ["a", "b", "c"]

a.index("b")            #指定した値を持つ要素のインデックスを返却する

print(a.index("b"))#

a = ["a", "b", "a"]

a.count("a")            #指定した値を持つ要素の件数を返却する

print(a.count("a"))#

a.sort()                #リスト内の要素をソートする

print(a)#

a = ["a", "b", "c"]

a.reverse()             #リスト内の要素を反転する

print(a)#

b = a.copy()            #リストのシャローコピー（浅いコピー）を返却する

a.clear()

print(a)

print(b)

'''
    同じ値をaに入れた後のそれぞれの処理の結果の推移を追ってください
    
    .sortと.reverseは配列内の要素をそのまま並べ替えている事に注目
'''
