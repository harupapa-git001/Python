'''
    11. MarkupSafe
    
    "MarkupSafe"は文字列をXML/HTML形式にエスケープして出力するためのライブラリです。
    
    本書ではバージョン1.0を扱います。
    
    #インストール
    
    ■Windows
    
    pip install markupsafe
    
    ■macOS
    
    pip3 install markupsafe
    
    このライブラリでは、文字列のエスケープの他にも文字列をマークアップ用に変換させることもできます。
'''
#エスケープとマークアップ

from markupsafe import Markup, escape

#エスケープ

print(escape("<script>alert(document.cokie);</script>"))

#マークアップ

tmpl = Markup("<p>%s</p>")

print(tmpl % "hoge > fuga")

