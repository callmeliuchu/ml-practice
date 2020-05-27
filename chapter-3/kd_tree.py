# -*- coding:utf8 -*
data_set = [[7,2],[5,4],[9,6],[2,3],[4,7],[8,1]]


class Node:

    def __init__(self,index,data):
        self.index = index
        self.data = data
        self.left = None
        self.right = None


def create_tree(index,arr):
    if len(arr) == 0:
        return None
    arr = sorted(arr,key=lambda x:x[index])
    dimension = len(arr[0])
    split_num = len(arr)//2
    data = arr[split_num]
    node = Node(index,data)
    split_index = (index+1)%dimension
    node.left = create_tree(split_index,arr[:split_num])
    node.right = create_tree(split_index,arr[split_num+1:])
    return node


root = create_tree(0,data_set)


def dfs(root):
    if root:
        print(root.data)
        dfs(root.left)
        dfs(root.right)

dfs(root)
