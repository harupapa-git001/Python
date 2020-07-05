'''ex1 Pillowを使ってデスクトップ上の画像をリサイズし保存する。
#pika.jpgをDesktopに置いて6行目パスを指定した状態で実行してください。
#実行後にpika_resize.jpgがデスクトップ上に作成されれば完成です。
#RGB指定はex2を参照してください。


from PIL import Image

#既存のファイルをreadモードで読み込む

img = Image.open("/Users/user/Desktop/pika.jpg", "r")

#リサイズ
resize_img = img.resize((256, 256))

#リサイズ後の画像を保存
resize_img.save("pika_resize.jpg", "JPEG")

'''

'''ex2 テキストを画像として出力する
#テキストが右寄りですので中央に合わせてください。

from PIL import Image, ImageDraw

#画像オブジェクトの生成
#サイズと背景色を指定
text_canvas = Image.new("RGB", (50, 40), (255, 255, 255))

draw = ImageDraw.Draw(text_canvas)

#テキストの書き込み
#座標、テキスト、テキストの文字色
draw.text((29, 15), "pika", fill = "#00ff00")

#画像として保存
text_canvas.save("pika_save.jpg", "JPEG")

'''
#ex3　画像の合成
#52行目と53行目のコメントを入れ替えてcanvasの幅を確認してください。
#pika.jpgとmyu.jpgのサイズが違うのでリサイズしてください。


from PIL import Image

#既存画像を読み込む

pika = Image.open("pika.jpg", "r")
myu = Image.open("myu.jpg", "r")

#マージに利用するベースの画像の生成

#canvas = Image.new("RGB", (600, 320), ( 180, 255, 180))
canvas = Image.new("RGB", (600, 300), ( 255, 255, 255))

#リサイズする
#pika = pika.resize((256, 256))
#myu = myu.resize((256, 256))

#座標(0, 0) と (0, 100)に既存画像を貼り付ける

canvas.paste(pika, (0, 0))
canvas.paste(myu, (300, 0))

#画像の保存
canvas.save("pika_myu.jpg", "JPEG")
