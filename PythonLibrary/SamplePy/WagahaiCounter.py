import urllib.request

data = urllib.request.urlopen("http://www.python.org")

#coding: utf-8
#import urllib.request

print ("データをダウンロード中です...")

wagahai = urllib.request.urlopen("http://www.aozora.gr.jp/cards/000148/files/789_14547.html")

wagahai2 = wagahai.read()

#wagahai3 = unicode(wagahai2, "shift-jis", errors = "ignore")
#wagahai3 = wagahai2.decode("utf-8", errors="ignore")

wagahai3 = wagahai2.decode("shift-jis", errors = "ignore")

def wordcount(data, w):
       
        n = data.count(w)
        print ("「{0}」は{1}回出てきました。\n".format(w,n))
        
while True:
            print ("「吾輩は猫である」の中で探したい言葉を入力してください。")
            print ("検索を中止する場合は「終わり」と入力してください。")
            
#            word = raw_input()
            word = ""
            word = input('>>')
            
            if word == "終わり":
                print ("ありがとうございました。またのお越しを。")
                
                quit()
                
            else:
                wordcount(data = wagahai3, w = word)
