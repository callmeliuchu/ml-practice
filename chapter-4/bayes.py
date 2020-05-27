# -*- coding:utf8 -*
data_set = [[1,'S',-1],
            [1,'M',-1],
            [1,'M',1],
            [1,'S',1],
            [1,'S',-1],
            [2,'S',-1],
            [2,'M',-1],
            [2,'M',1],
            [2,'L',1],
            [2,'L',1],
            [3,'L',1],
            [3,'M',1],
            [3,'M',1],
            [3,'L',1],
            [3,'L',-1]]

from collections import defaultdict
result = defaultdict(int)
y_result = defaultdict(int)
for d in data_set:
    y_result[d[-1]] += 1


for d in data_set:
    for num in range(len(d)-1):
        key = (num,d[num],d[-1])
        result[key] += 1/y_result[d[-1]]

x = [2,'S']

for y in y_result:
    p = 1
    for index in range(len(x)):
        num = x[index]
        p = p*result[(index,x[index],y)]
    p = p*y_result[y]/len(data_set)
    print('y-->',y,'p-->',p)



