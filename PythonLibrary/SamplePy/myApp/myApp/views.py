'''

from django.http.response import HttpResponse

def hello_world(request):
    return HttpResponse("<html><head><h1>HelloWorld</h1></head>""<body><h3>改行なしタイトルh3フォント</h3>""<p>つなげて表示します</p>""<p>改行は/brです</p></br>""<p>改行すると</br>こんな感じになります</p></br>""<u><b>下線太文字にしました</b></u></br>""<p>HTMLタグリファレンスのリンクを貼り付けて終わりにします。</p></br>""<a>https://www.tagindex.com/html_tag/elements/<a/></body></html>")
    
    return HttpResponse("<a>これは表示されません</a>")
'''

'''
    urls.pyからhello_world(request)クラスが呼び出されます
'''
#templatesフォルダの中から呼び出されます

from django.http.response import HttpResponse

from django.shortcuts import render

def hello_world(request):
    return render(request, "temp.html")
