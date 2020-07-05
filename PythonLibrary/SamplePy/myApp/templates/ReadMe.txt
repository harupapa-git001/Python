４．テンプレートを使う

前節ではDjangoの手軽さを伝えられたかと思いますが、その反面「レスポンスのHTMLを都度プログラムに書くのは面倒だ」と感じませんでしたか？しかし、安心してください。

Djangoはデザインなどの静的な要素を予め「テンプレート」として用意しておくことができます。

テンプレートを利用するには、まずはテンプレートを保存するフォルダを決める必要があります。

これはプロジェクトの作成時に自動生成された"settings.py"（urls.pyと同じフォルダに生成されています）の「TEMPLATES」部に指定します。

具体的には次のように指定します。

settings.py修正前

〜略〜

TEMPLATES = [
  {        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {

            context_processors': [
                django.template.context_processors.debug',
                django.template.context_processors.request',
                django.contrib.auth.context_processors.auth',
                django.contrib.messages.context_processors.messages',
	    ],
	 },
  },
]

〜略〜

settings.py修正後

〜略〜

TEMPLATES = [
  {        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'DIRS': [os.path.join(BASE_DIR, 'templates'),
	],
        'APP_DIRS': True,
        'OPTIONS': {
            context_processors': [
                django.template.context_processors.debug',
                django.template.context_processors.request',
                django.contrib.auth.context_processors.auth',
                django.contrib.messages.context_processors.messages',
	    ],
	 },
  },
]

〜略〜

"settings.py"を修正したら、次は保存先に指定したフォルダを生成します。

修正を加えた「os.path.join(BASE_DIR,'templates'),」は「プロジェクトフォルダ下のtemplatesフォルダ」を意味するので、その通りにフォルダを作ります。

テンプレートフォルダを作ったら、その中にテンプレートファイルを配置します。

今回は"temp.html"と言う名前で次のような内容のファイルを配置します。


temp.html

<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF8">
  <title>HelloWorld</title>
</head>
<body>
  <h1>HelloWorld</h1>
</body>
</html>

テンプレートファイルが用意できたら、最後に"views.py"を次のように修正します。

views.py

from django.http.response import HttpResponse

from django.shortcuts import render

def hello_world(request):

	return render(request, "temp.html")


"views.py"の修正点は

・render関数のインポート
・render関数を使ってテンプレートファイルを読み込む

この２点です。

これらの修正を加えたら、サーバを起動してブラウザで「http://127.0.0.1:8000/」にアクセスしてみましょう。

問題なく各ファイルの用意、修正ができていれば無事に「HelloWorld」が表示されるはずです。

テンプレートの基本的な使い方は以上です。
 
