# -*- coding:utf8 -*
from collections import defaultdict
import math
def createDataSet():
    """
创建数据集

    :return:
    """
    dataSet = [[u'青年', u'否', u'否', u'一般', u'拒绝'],
               [u'青年', u'否', u'否', u'好', u'拒绝'],
               [u'青年', u'是', u'否', u'好', u'同意'],
               [u'青年', u'是', u'是', u'一般', u'同意'],
               [u'青年', u'否', u'否', u'一般', u'拒绝'],
               [u'中年', u'否', u'否', u'一般', u'拒绝'],
               [u'中年', u'否', u'否', u'好', u'拒绝'],
               [u'中年', u'是', u'是', u'好', u'同意'],
               [u'中年', u'否', u'是', u'非常好', u'同意'],
               [u'中年', u'否', u'是', u'非常好', u'同意'],
               [u'老年', u'否', u'是', u'非常好', u'同意'],
               [u'老年', u'否', u'是', u'好', u'同意'],
               [u'老年', u'是', u'否', u'好', u'同意'],
               [u'老年', u'是', u'否', u'非常好', u'同意'],
               [u'老年', u'否', u'否', u'一般', u'拒绝'],
               ]
    labels = [u'年龄', u'有工作', u'有房子', u'信贷情况']
    # 返回数据集和每个维度的名称
    return dataSet, labels


dataSet,labels = createDataSet()



def cal_h(data_list):
    count = defaultdict(int)
    for data in data_list:
        count[data[-1]] +=1
    s = 0
    for k,v,in count.items():
        p = v/len(count)
        h = -p*math.log2(p)
        s += h
    return s





for item in dataSet:
    print(item)

for label in labels:
    print(label)