import matplotlib.pyplot as plt
fig = plt.figure()

# 1行2列の左
labels = ["A", "B", "C", "D", "E", "F"]
x = range(0, 6)
y = [10, 20, 30, 40, 50, 60]
ax1 = fig.add_subplot(1, 2, 1)
ax1.bar(x, y, tick_label = labels) 
ax1.set_title("graph1")

# 1行2列の右
labels = ["E", "D", "C", "B", "A"] 
y = [10, 20, 30, 40, 50] 
ex = [0, 0, 0, 0, 0.1] 
ax2 = fig.add_subplot(1, 2, 2)
ax2.pie(y, explode = ex, labels = labels, autopct = '%1.1f%%', startangle = 90) 
ax2.set_title("graph2")

# グラフを表示する
plt.show()
