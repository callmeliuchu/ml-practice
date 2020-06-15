# -*- coding:utf8 -*
from collections import defaultdict
import math
from collections import Counter

def createDataSet():
    """
创建数据集

    :return:
    """
    # dataSet = [[u'青年', u'否', u'否', u'一般', u'拒绝'],
    #            [u'青年', u'否', u'否', u'好', u'拒绝'],
    #            [u'青年', u'是', u'否', u'好', u'同意'],
    #            [u'青年', u'是', u'是', u'一般', u'同意'],
    #            [u'青年', u'否', u'否', u'一般', u'拒绝'],
    #            [u'中年', u'否', u'否', u'一般', u'拒绝'],
    #            [u'中年', u'否', u'否', u'好', u'拒绝'],
    #            [u'中年', u'是', u'是', u'好', u'同意'],
    #            [u'中年', u'否', u'是', u'非常好', u'同意'],
    #            [u'中年', u'否', u'是', u'非常好', u'同意'],
    #            [u'老年', u'否', u'是', u'非常好', u'同意'],
    #            [u'老年', u'否', u'是', u'好', u'同意'],
    #            [u'老年', u'是', u'否', u'好', u'同意'],
    #            [u'老年', u'是', u'否', u'非常好', u'同意'],
    #            [u'老年', u'否', u'否', u'一般', u'拒绝'],
    #            ]

    dataSet = [['长', '粗', '男'],
               ['短', '粗', '男'],
               ['短', '粗', '男'],
               ['长', '细', '女'],
               ['短', '细', '女'],
               ['短', '粗', '女'],
               ['长', '粗', '女'],
               ['长', '粗', '女']]

    # labels = [u'年龄', u'有工作', u'有房子', u'信贷情况']
    labels = ['头发', '声音']
    # 返回数据集和每个维度的名称
    return dataSet, labels


dataSet,labels = createDataSet()



def cal_h(data_list):
    count = defaultdict(int)
    for data in data_list:
        count[data[-1]] +=1
    s = 0
    for k,v,in count.items():
        p = v/float(len(data_list))
        h = -p*math.log2(p)
        s += h
    return s


def split_data(data_set,column,value):
    res = []
    for row in data_set:
        if row[column] == value:
            new_row = row[:column]
            new_row.extend(row[column+1:])
            res.append(new_row)
    return res

def choose_best_column(data_set):
    base_h = cal_h(data_set)
    g = 0
    loc = -1

    for i in range(len(data_set[0])-1):
        values = set(row[i] for row in data_set)
        column_h = 0
        for value in values:
            data = split_data(data_set,i,value)
            h = cal_h(data)*len(data)/len(data_set)
            column_h += h
        g_h = base_h - column_h
        if g < g_h:
            g = g_h
            loc = i
    return loc







def create_tree(data_set,labels):
    classes = [row[-1] for row in data_set]
    if len(classes) == classes.count(classes[0]):
        return classes[0]
    if len(data_set[0]) == 1:
        return Counter(classes).most_common(1)[0][0]

    best_split = choose_best_column(data_set)
    label = labels[best_split]
    my_tree = {label:{}}
    values = set(row[best_split] for row in data_set)
    new_labels = labels[:]
    del new_labels[best_split]
    # print(best_split,dataSet)
    for value in values:
        new_data_set = split_data(data_set,best_split,value)
        # print(new_data_set)
        my_tree[label][value] = create_tree(new_data_set,new_labels)
    return my_tree

tree = create_tree(dataSet,labels)
print(tree)




# print(choose_best_column(dataSet))



# print(cal_h(dataSet))
#
# for item in dataSet:
#     print(item)
#
# for label in labels:
#     print(label)


