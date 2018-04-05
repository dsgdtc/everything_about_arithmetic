#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: 图的划分.py
Author: dsgdtc@163.com
Date: 2017/12/18 21:07
图的联通分量有多少个
解决方案：并 查集，集合划分
UnionFindSet

邹博的处理方式是在第一次查询的时候去循环遍历整个并查集，然后找到待查元素的父节点，压缩路径
下边写的是另一种方法：在创建连接的时候先循环一遍，压缩路径
"""
class UnionFindSet(object):

    parent = [] # 存储每个元素的父节点
    count = 0   # 一共有几组，初始化时各元素单独成组

    def __init__(self, origin_set, n):
        self.count = n # 岛屿的数量
        self.partition_count = n  # 岛屿的分类数量,用的时候可以和self.count合并
        self.origin_items = origin_set # 岛们
        # 初始化的数据结构时，每个元素的父节点都是自己,然后做union
        for i in range(0, n):
            self.parent.append(i)

    def isconnect(self, i, j):

        root_i = self.find(i)
        root_j = self.find(j)
        if root_j == root_j:
            return True
        else:
            return False

        # return self.find(i) == self.find(j)
        
    def find(self, i):
        p_i = self.origin_items.index(i)
        return self.parent[p_i]

    def find_set(self, root):
        """返回parent为root的所有元素

        :param root:
        :return:
        """
        result = []
        size = len(self.parent)
        for index in range(size):
            if self.parent[index] == root:
                result.append(self.origin_items[index])
        return result
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        # print (root_i,root_j)
        if root_i == root_j:
            print ("----------%s 和 %s 已经是连通的----------" %(i, j))
            return True
        else:  # root_i != root_j:
            self.parent[root_i] = root_j
            self.partition_count -= 1

            for x in self.origin_items:
                # 如果父节点相同,压缩路径
                # print ("压缩路径前的list:    : %s" %(self.parent))
                # print ("当前检查点: %s" %(x))
                # input("enter to continue...")

                if self.parent[self.origin_items.index(x)] == root_i:
                    self.parent[self.origin_items.index(x)] = root_j

def main1():
    # 邻接表的数据结构
    N = 10 # 岛屿数量是10
    origin_list = [i for i in range(N)]
    ufs = UnionFindSet(origin_list, N)
    print ("初始化并查集parent list: %s" % (",").join(str(x) for x in ufs.parent))
    list = [
        (4,3),
        (3,8),
        (6,5),
        (9,4),
        (2,1),
        (8,9),
        (5,0),
        (7,2),
        (6,1),
        (1,0),
        (6,7)
    ]
    for k in list:
        p = k[0]
        q = k[1]
        ufs.union(p, q)
        print ("建立连接关系: %s和%s " %(p, q))
        print ("DEBUG: origin_list is: %s" %(ufs.origin_items))
        print ("DEBUG: self.parent is: %s" %(ufs.parent))

    print ("最终分类数量: %s" %(ufs.partition_count))

def main2():
    iland = ["A","B","C","D","E","F"]
    iland_n = len(iland)
    ufs = UnionFindSet(iland, iland_n)
    print ("初始化并查集parent list: %s" % (",").join(str(x) for x in ufs.parent))
    list = [
        ("A","E"),
        ("B","C"),
        ("C","F")
    ]
    for k in list:
        p = k[0]
        q = k[1]
        ufs.union(p, q)
        print ("建立连接关系: %s和%s " %(p, q))
        print ("DEBUG: origin_list is: %s" %(ufs.origin_items))
        print ("DEBUG: self.parent is: %s" %(ufs.parent))
    print ("最终分类数量: %s" %(ufs.partition_count))
    
    item = "A"
    cluster = ufs.find(item)
    print ("%s属于%s" %(item, cluster))

if __name__ == '__main__':

    #main1()
    main2()
    """
    强连通图:对于一个有向图，每个节点都存在到达其他任何节点的路径
    不是强连通图，可能问:求强连通分量
    判断是否为强连通图：
    随机找一个节点记为S，从S开始深度优先搜索
        如果从S可以遍历到所有节点，所有边反向，再从S遍历一遍
        如果从S不可以遍历到所有节点，那么肯定不是强连通图
    """

    
