# -*- coding:utf8 -*
import random
import numpy as np

def func(x):
    return 2*x + 10*(random.random())


x1 = []
y1 = []
for _ in range(100):
    x = 15*random.random()
    x1.append(x)
    y1.append(func(x))
    print(x,func(x))


import numpy as np
import matplotlib.pyplot as plt










plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xmax=29, xmin=-29)
plt.ylim(ymax=29, ymin=-29)
# 画两条（0-9）的坐标轴并设置轴标签x，y




colors1 = '#00CED1'  # 点的颜色


area = np.pi * 4 ** 2  # 点面积



data_set = []

for x,y in zip(x1,y1):
    data_set.append([x,y])



def process_data_set(data_set):

    for j in range(len(data_set[0])):
        s = 0
        for i in range(len(data_set)):
            s += data_set[i][j]
        average = s / len(data_set)
        for i in range(len(data_set)):
            data_set[i][j] -= average


process_data_set(data_set)


mat = np.mat(data_set)
res = mat.transpose()*mat
print(res)



a,b=np.linalg.eig(res)

print(a)
print(b)

for i in range(2):
    # print(b[:,i])


    pi = (-15*b[:,i].transpose()).tolist()[0]
    pj = (15*b[:,i].transpose()).tolist()[0]

    # print(pi)
    # print(pj)

    xi = [pi[0],pj[0]]
    yi = [pi[1],pj[1]]

    #
    print('-------')
    print(xi)
    print(yi)

    plt.plot(xi, yi, linewidth='0.5', color='#000000')



x1 = [x for x,y in data_set]
y1 = [y for x,y in data_set]





plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='类别A')


# plt.legend()
plt.show()