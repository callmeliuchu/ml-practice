# -*- coding:utf8 -*
data_set = [[(3,3),1],
            [(4,3),1],
            [(1,1),-1]
           ]


w = (0,0)
b = 0
rate = 0.01

def multi(w,x):
    s = 0
    for v1,v2 in zip(w,x):
        s += v1*v2
    return s

def scale(x,rate):
    return (v*rate for v in x)

def add(x1,x2):
    return [v1+v2 for v1,v2 in zip(x1,x2)]



for i in range(100):
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
