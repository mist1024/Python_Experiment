import matplotlib.pyplot as plt
import random
position=0      #定义初始位置
walk=[position]     #生成步进walk的列表
for i in range(1000):       #1000次循环
    step=1 if random.randint(0,1) else -1       #确定每次随机漫步的步数
    position+=step      #随机步进累积和
    walk.append(position)


plt.plot(walk)        #画出折线图
plt.show()