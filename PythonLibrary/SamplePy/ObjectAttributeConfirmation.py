dir("text")

print(dir("text"))

'''
    オブジェクトの属性の確認先ほどの anaオブジェクトには name,ageといったインスタンス変数や get_age()といったメソッドが存在しましたが、これらはオブジェクトが持つ「属性」と呼ばれるものです。
    この属性としてどのようなものがあるかは dir関数を使うことで確認できます。dir関数の引数としてオブジェクトを与えると、属性の一覧をリスト形式で返してくれます。たとえば文字列型の属性であれば以下のようになります。

    オブジェクトのメソッド名を忘れてしまった際などに dir関数を使ってどういうものがあるか確認できます。ぜひ活用してみてください。

'''