# -*- coding:utf8 -*

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



image = Image.open(r'test.png')
# plt.imshow(image)
# plt.show()

image_arr = np.array(image)
# print(image_arr)
# print(image_arr.shape)
# np.reshape(image_arr,(574,1024))
# print(image_arr)
t = np.array([0.299, 0.587, 0.114])
res = []
for d in image_arr:
    # print(len(d))
    arr = []
    for d1 in d:
        arr.append(np.dot(d1,t))
        # print(np.dot(d1,t))
    res.append(arr)

res = np.array(res)
print(res)
plt.imshow(res)


from numpy import linalg


u,e,v=linalg.svd(res)
print(e[:10])

image_file = u'speed.png'
def svd_restore(sigma, u, v, K):
    K = min(len(sigma)-1, K)            #当K超过sigma的长度时会造成越界
    m = len(u)
    n = v[0].size
    SigRecon = np.zeros((m, n))         #新建一int矩阵，储存恢复的灰度图像素
    for k in range(K+1):                #计算X=u*sigma*v
        for i in range(m):
            SigRecon[i] += sigma[k] * u[i][k] * v[k]
    SigRecon = SigRecon.astype('uint8') #计算得到的矩阵还是float型，需要将其转化为uint8以转为图片
    Image.fromarray(SigRecon).save("svd_" + str(K) + "_" +image_file) #保存灰度图


# new_im = Image.fromarray(res)
# new_im.show()
print(len(res))
index = 10
for i in range(10):
    svd_restore(e,u,v,index)
    index += 2

