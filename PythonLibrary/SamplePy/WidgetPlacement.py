import tkinter as tk

root = tk.Tk()

#タイトルバーの表示、画面サイズの設定
root.title("MyGUIApp")
root.geometry("300x200")#横幅、縦幅の設定（単位はpx）

#ウィジェットの生成

btn = tk.Button(root, text = "click!", width = "5")
lbl = tk.Label(root, text = " ラベル", foreground = "#ff0000", background = "#0000ff")
edt = tk.Entry(root, width = "5")
valB = tk.BooleanVar()
valB.set(True)
chk = tk.Checkbutton(root, text = " チェック", variable = valB)
vall = tk.IntVar()
vall.set(0)
rdo1 = tk.Radiobutton(root, text = "項目１", variable = vall, value = 0)
rdo2 = tk.Radiobutton(root, text = "項目２", variable = vall, value = 1)
rdo3 = tk.Radiobutton(root,text = "項目３", variable = vall, value = 2)

btn.place(x = 100, y = 200) #位置を指定して配置
lbl.grid(row = 0, column = 0)
edt.grid(row = 1, column = 0)
chk.grid(row = 1, column = 1)
rdo1.grid(row = 2, column = 0)
rdo2.grid(row = 2, column = 1)
rdo3.grid(row = 2, column = 2)

root.mainloop()

'''
    例の通り、ラジオボタンとチェックボタンの初期値（チェック　ON／OFF）の指定は少し特殊です。
    
        それぞれtkinterが提供sルウオブジェクト経由で値を設定する必要があり、直接値を指定すると正常に動作しないので注意が必要です。
'''
