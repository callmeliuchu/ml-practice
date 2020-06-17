# -*- coding:utf8 -*


import numpy as np
import matplotlib.pyplot as plt
import random
import operator

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=9, xmin=0)
plt.ylim(ymax=9, ymin=0)
# 画两条（0-9）的坐标轴并设置轴标签x，y

x1 = np.random.normal(1, 0.6, 100)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的x轴坐标
y1 = np.random.normal(1, 0.6, 100)  # 随机产生300个平均值为2，方差为1.2的浮点数，即第一簇点的y轴坐标


x2 = np.random.normal(7, 0.6, 100)
y2 = np.random.normal(7, 0.6, 100)



xi = np.random.normal(4, 0.6, 100)
yi = np.random.normal(4, 0.6, 100)


colors1 = '#00CED1'  # 点的颜色
colors2 = '#DC143C'
colorsi = '#DC1FFF'

area = np.pi * 4 ** 2  # 点面积
# 画散点图




plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='类别A')
plt.scatter(x2, y2, s=area, c=colors2, alpha=0.4, label='类别B')
plt.scatter(xi, yi, s=area, c=colorsi, alpha=0.4, label='类别D')

plt.legend()



data_set = []
for (v1,v2) in zip(x1,y1):
    data_set.append([v1,v2])

for (v1,v2) in zip(x2,y2):
    data_set.append([v1,v2])


def distance(v1,v2):
    return sum((val1-val2)**2 for val1,val2 in zip(v1,v2))**0.5

def average(data_set):
    arr = []
    for j in range(len(data_set[0])):
        tmp = sum(data_set[i][j] for i in range(len(data_set)))/len(data_set)
        arr.append(tmp)
    return arr



def kmeans_func(data_set,k):
    arr = []
    for j in range(len(data_set[0])):
        tmp = [data_set[i][j] for i in range(len(data_set))]
        min_val = min(tmp)
        max_val = max(tmp)
        arr.append((min_val,max_val))

    k_arr = []
    for _ in range(k):
        point = [min_val + (max_val - min_val)*random.random() for min_val,max_val in arr]
        k_arr.append(point)

    for _ in range(1000):
        tag_arr = [None] * len(k_arr)
        for data in data_set:
            distance_arr = []
            for point in k_arr:
                distance_arr.append(distance(data,point))
            min_index, min_number = min(enumerate(distance_arr), key=operator.itemgetter(1))
            if not tag_arr[min_index]:
                tag_arr[min_index] = []
            tag_arr[min_index].append(data)
        next_k_arr = []
        for data in tag_arr:
            if data is None:
                next_k_arr.append(average(data_set))
            else:
                next_k_arr.append(average(data))

        # print(next_k_arr)
        if k_arr == next_k_arr:
            print('结束')
            break
        else:
            k_arr = next_k_arr
    return k_arr



def run():
    for i in range(2):
        k_arr = kmeans_func(data_set,3)
        x3 = [data[0] for data in k_arr]
        y3 = [data[1] for data in k_arr]
        colors3 = '#000{}{}{}'.format(i,i,i)
        plt.scatter(x3, y3, s=np.pi * 4 ** 4, c=colors3, alpha=0.4*i, label='类别C')
    plt.show()






run()




