print ("Please input your　name.")
#x = raw_input() 2系
x = input('>>')
print ("あなたは" + x + "さんですね？よろしければy：訂正するならz:を入力:")

y = input('>>')

if y == "y":
    print (x + "さんこんにちは")
else :
    print("ログインできません")
