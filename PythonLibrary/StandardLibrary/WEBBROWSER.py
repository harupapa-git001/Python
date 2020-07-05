'''
    ９．webbrowser
    
    "webbrowser"はブラウザアプリケーションでURLを開くためのライブラリです。
    
    使い方は至ってシンプルで、単純にURLを開くだけなら"open"関数を呼び出すだけでOKです。

'''

#URLを開く

import webbrowser

#google検索のトップページが開く
webbrowser.open("https://www.google.co.jp/")

#ポケモン図鑑のトップページも＜新規タブで＞開く（開きたくない場合は文頭に#でコメントアウト）
webbrowser.open_new_tab("https://zukan.pokemon.co.jp")

#Apple公式トップページが開く（既にブラウザが起動している場合はタブとして開く、あるいは第2引数の指定(0~2)で開くということですが、当環境では起動していなくてもタブとして開いています）
webbrowser.open("https://www.apple.com/jp/", new = 1, autoraise = True)
    
'''
    "open"関数は端末のデフォルトブラウザで指定されたURLを表示します。
    
    この関数について、公式ドキュメントには「できるだけ既存のウィンドウを再利用する」旨の記載があり、"new"と言う引数を使うことでこの挙動を変更できるよう説明されていますが（新しいウィンドウやタブで開く）、筆者としては引数を指定しても結局はOSとブラウザに依存するように感じています。ですので、新しいウィンドウで表示したい場合は"open_new"関数を、新しいタブで表示したい場合は"open_new_tab"関数を使うようにしましょう。
    
    なお、これらの関数でも環境次第では期待通りに動作しないこともありますので、「必ずこの通りに動作すること」を前提とする設計は避けるようにしてください。
    
    （公式ドキュメントにも、これらに関数には「可能であればそのように動作する」旨が記載されています）

'''

'''
    次に、このライブラリではデフォルトに設定されていないブラウザでURLを開くこともできます。
    
    これには"get"関数に対象としたいブラウザアプリの「絶対パス」を指定します。
    
    例えばWindowsでIEを使いたい場合は次のような記述になります。

'''

'''

import webbrowser

#Windows Internet Explorer使用時に実行
browser = webbrowser.get("C:¥ProgramFiles¥Internet Explorer¥iexplore.exe")

browser.open("https://www.google.co.jp/")

'''
