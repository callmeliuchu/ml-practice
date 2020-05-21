# -*- coding:utf8 -*
# data_set = [[(3,3),1],
#             [(4,3),1],
#             [(1,1),-1]
#            ]


w = (0,0)
b = 0
rate = 0.0001

def multi(w,x):
    s = 0
    for v1,v2 in zip(w,x):
        s += v1*v2
    return s

def scale(x,rate):
    return (v*rate for v in x)

def add(x1,x2):
    return [v1+v2 for v1,v2 in zip(x1,x2)]





import numpy as np
import matplotlib.pyplot as plt



# matplotlib画图中中文显示会有问题，需要这两行设置默认字体

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=9, xmin=0)
plt.ylim(ymax=9, ymin=0)
# 画两条（0-9）的坐标轴并设置轴标签x，y

x1 = np.random.normal(2, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
y1 = np.random.normal(2, 1.2, 300)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的y轴坐标

data_set = []
for (v1,v2) in zip(x1,y1):
    data_set.append([[v1,v2],-1])


x2 = np.random.normal(7.5, 1.2, 300)
y2 = np.random.normal(7.5, 1.2, 300)

for (v1,v2) in zip(x2,y2):
    data_set.append([[v1,v2],1])

for i in range(10000):
    flag = True
    for x,y in data_set:
        if y*(multi(w,x) + b) <= 0:
            w = add(w,scale(x,rate*y))
            b = b + rate*y
            flag = False
            break
    print(w,b)
    if flag:
        print('结束')
        break


# w[0]*x1 + w[1]*x2 + b = 0
p1 = [0,-b/w[1]]
p2 = [-b/w[0],0]
print(p1,p2)



colors1 = '#00CED1'  # 点的颜色
colors2 = '#DC143C'
area = np.pi * 4 ** 2  # 点面积
# 画散点图
plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='类别A')
plt.scatter(x2, y2, s=area, c=colors2, alpha=0.4, label='类别B')
plt.plot(p1, p2, linewidth='0.5', color='#000000')
plt.legend()
plt.savefig(r'12345svm.png', dpi=300)
plt.show()


