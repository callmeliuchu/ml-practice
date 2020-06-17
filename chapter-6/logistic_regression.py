# -*- coding:utf8 -*
import numpy as np
import matplotlib.pyplot as plt
import math

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=9, xmin=0)
plt.ylim(ymax=9, ymin=0)
# 画两条（0-9）的坐标轴并设置轴标签x，y

x1 = np.random.normal(2, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
y1 = np.random.normal(2, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的y轴坐标


x2 = np.random.normal(7.5, 1.2, 300)
y2 = np.random.normal(7.5, 1.2, 300)






colors1 = '#00CED1'  # 点的颜色
colors2 = '#DC143C'
area = np.pi * 4 ** 2  # 点面积
# 画散点图




plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='类别A')
plt.scatter(x2, y2, s=area, c=colors2, alpha=0.4, label='类别B')

plt.legend()








def multi(w,x):
    s = 0
    for v1,v2 in zip(w,x):
        s += v1*v2
    return s

def scale(x,rate):
    return (v*rate for v in x)

def add(x1,x2):
    return [v1+v2 for v1,v2 in zip(x1,x2)]


def h(x):
    return math.exp(x)/(1.0+math.exp(x))


data_set = []
for (v1,v2) in zip(x1,y1):
    data_set.append([[v1,v2],1])

for (v1,v2) in zip(x2,y2):
    data_set.append([[v1,v2],0])

rate = 0.001
w = [0.1,0.3,0.2]

for i in range(100000):
    k = 0
    gap = [0,0,0]
    flag = True
    for [x1,x2],y in data_set:
        xi = [1,x1,x2]
        p = h(multi(xi,w)) - y
        gap = add(gap, scale(xi, p))
        flag = False
    w = add(w, scale(gap, -rate / len(data_set)))
    # if flag:
    #     break

    # gap = scale(gap,1/len(data_set))
    # w = add(w,scale(gap,-rate))

# r = [v/w[0] for v in w]
# print(r)
print(w)
p1 = [0,-w[0]/w[2]]
p2 = [-w[0]/w[1],0]
print(p1)
print(p2)
plt.plot(p1, p2, linewidth='0.5', color='#000000')




plt.show()

