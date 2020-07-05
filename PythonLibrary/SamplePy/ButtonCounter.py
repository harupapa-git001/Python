'''
import tkinter
font = ("Helevetica", 32, "bold")
label = tkinter.Label(text = "これがテキストの内容です", font = font, bg = "red")
label.pack()
label.mainloop()
'''
#上記がラベル表示
#下記がボタンがクリックされた回数
import tkinter

'''
    #tkinterインスタンスの生成
    root = tkinter.Tk()
'''
#TK_SILENCE_DEPRECSTION = 1
counter = 0
font = ("Helevetica", 32, "bold")
button = tkinter.Button(font = font, text = str(counter))

def clicked():
    global counter, button
    counter = counter + 1
    button.config(text = str(counter))
    
button.config(command = clicked)
button.pack()
button.mainloop()

'''
    tkinterで使える主なウィジェットは次の通りです。
    
    Frame
        複数のパーツを格納する
        
    Label
        文字列を表示する
        
    Message
        複数行の文字列を表示する
        
    Button
        ボタン
        
    Radiobutton
        ラジオボタン
        
    Checkbutton
        チェックボタン（チェックボックス）
        
    Listbox
        リストボックス
        
    Scrollbar
        スクロールバー
        
    Scale
        スケール（スライダーバー）
        
    Entry
        改行不可のテキストボックス
        
    Menu
        メニュー
        
    Menubutton
        メニューボタン
'''
