import tkinter as tk
import tkinter.messagebox as msg

root = tk.Tk()

#ボタンクリック時に呼び出す関数

def showAlert():
    res = msg.askokcancel(" タイトル", edt.get())
    
    if(res == True):
        lbl["text"] = "ok"
        
root.title("MyGUIApp")

#UIパーツの生成

edt = tk.Entry(root,width = "10")
btn = tk.Button(root, text = "click!", command = showAlert)
lbl = tk.Label(root)

#UIパーツを左から順に配置
#tk.TOP（デフォルト）、tk.LEFT、tk.RIGHT、tk.BOTTOMが指定可能

edt.pack(side = tk.LEFT)
btn.pack(side = tk.LEFT)
lbl.pack(side = tk.LEFT)

root.mainloop()

'''
    例の通り、イベントはクラス生成の際に"command"で指定します。
'''
