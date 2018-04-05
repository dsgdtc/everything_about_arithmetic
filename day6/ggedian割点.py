#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: gedian.py
Author: dsgdtc@163.com
Date: 2017/11/13 20:23
割点，隔边问题，深度优先搜索（和第一课的拓扑排序一样）
无向图G，删除点X以及与X邻接的所有边，图G变成非连通图，则X称为割点
算出图的所有割点
"""
from pprint import pprint

class Graph:

    # 用邻接表表示的图,不是矩阵，邹博代码里好像是用的矩阵
    # 算法思想：
    # 我们判断一个节点start_node是否是割点，就是判读他的子节点end_nodes中是否存在节点x不经过这个节点start_node就无法回到始祖节点，
    # 如果有这样的x，那么节点start_node就是割点。在递归过程的判断中，不是和始祖节点比较是和start_node的访问顺序比较
    def __init__(self, n):
        self.N = n #No. of vertices
        """
        self.graph = {
          0: [],
          1: []
        }
        """
        self.graph = { i: [] for i in range(n) }
        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, i, j):
        self.graph[i].append(j)
        # 写两个的话，输入图时输入一次连接关系就可以了
        # self.graph[j].append(i)

    def find_articulation_point(self):
        # 节点是否已经被访问的标志
        is_visit = dict( ( node, False ) for node in self.graph )
        is_ap = dict( ( node, False ) for node in self.graph )

        # 在dfs过程中，访问到此节点是第几次(和access_order_list差不多)
        access_order = dict( ( node, 0 ) for node in self.graph )
        # 在不经过父节点时,可以最早访问到当前节点的是第几次
        # 节点在不经过父节点时，最早能回溯到的访问次序，和上面一句等价
        # 如果这个子节点的low值
        lowest_access_order = dict( ( node, 0 ) for node in self.graph )

        parent = dict( ( node, 0 ) for node in self.graph )
        access_order_list = []

        def dfs(graph, start_node):
            access_order_list.append(start_node)
            access_order[start_node] = self.Time
            lowest_access_order[start_node] = self.Time

            # print ("access_order: %s" %(access_order))
            # input("enter to continue...")
            for end_node in graph[start_node]:
                print ("从%s的边开始找,访问到了%s"%(start_node, end_node))
                if is_visit[end_node] == False:
                    is_visit[end_node] = True
                    parent[end_node] = start_node
                    print ("is_visit: %s" %(is_visit))
                    print ("%s的父节点是%s" %(end_node, start_node))
                    input("enter to continue...\n")
                    self.Time += 1
                    dfs(graph, end_node)
                    print ("在递归过程中,%s的dfs完成了,也就是说和%s相连的子节点都已经被访问过了,start_node is:%s" %
                           (end_node, end_node, start_node))
                    print ("is_visit: %s" %(is_visit))
                    print("lowest_access_order:%s" % (lowest_access_order))
                    print("access_order:       %s" % (access_order))
                    lowest_access_order[start_node] = min(lowest_access_order[end_node], lowest_access_order[start_node])
                    print ("lowest_access_order:%s" % (lowest_access_order))
                    print ("access_order:       %s" % (access_order))

                    input("enter to continue...\n")
                    if parent[start_node] == 0 and len(graph[start_node]) > 1:
                        print ("根节点的分支多于2条,所以肯定是割点 %s" %(start_node))
                        input("!!!!!!!!enter to continue...")
                        is_ap[start_node] = True
                    if parent[start_node] != 0 and lowest_access_order[end_node] >= access_order[start_node]:
                        print("非根节点的时候,子节点%s不经过父节点能够回溯到的最早次序是%s, "
                              "父节点%s的访问次序是%s,所以父节点%s肯定是割点" %
                              (end_node, lowest_access_order[end_node], start_node, access_order[start_node], start_node))
                        input("!!!!!!!!enter to continue...")
                        is_ap[start_node] = True

                elif end_node != parent[start_node]:
                    # 就是说从start_node找到了不是父节点的其他节点了
                    # print("看不懂这个逻辑")
                    print ("end_node:%s, start_node:%s, parent[start_node]:%s"%(end_node, start_node, parent[start_node]))
                    print("lowest_access_order:%s" % (lowest_access_order))
                    print("access_order:       %s" % (access_order))
                    # 访问到自己的次序和不经过父节点时能够回溯到的其他亲戚的最早次序,如果其他的这个亲戚能比父节点还小，那么说明可以
                    # 通过这个其他亲戚回溯到祖先节点，如果这个亲戚的访问顺序比父节点大，那么说明不经过父节点还是不成
                    lowest_access_order[start_node] = min(lowest_access_order[end_node], lowest_access_order[start_node])
                    print("lowest_access_order:%s" % (lowest_access_order))
                    print("access_order:       %s" % (access_order))
                    print("已经访问过%s了,不用进递归" %(end_node))
                else:
                    print("已经访问过%s了,不用进递归" % (end_node))


        for start_node in self.graph:
            print ("Start node is:%s" %(start_node))
            print ("is_visit结果:%s" %(is_visit))
            # input("enter to continue...")
            if is_visit[start_node] == False:
                is_visit[start_node] = True
                # access_order_list.append(start_node)
                dfs(self.graph, start_node)
        print ("--"*50)
        print (self.graph)
        letter_node = ["A,0","B,1","C,2","D,3","E,4","F,5","G,6","H,7","I,8","J,9","K,10","L,11","M,12"]
        print(letter_node)
        print ("节点们:                %s"%(list(self.graph.keys())))
        print ("节点的父节点们:%s" %(parent))

        # access_order是存的节点名,list顺序是访问次序
        print ("深度优先https://www.bilibili.com/bangumi/play/ep116163搜索的访问次序:%s" %(access_order_list))
        print ("DFS过程中,每个节点是第几次被访问到的:  %s" %(access_order))
        print ("DFS过程中,每个节点最早可以第几次被访问:%s" %(lowest_access_order))
        print ("is_ap: %s" %(is_ap))

if __name__ == '__main__':

    # 邻接表的数据结构
    g4 = Graph(13)
    g4.addEdge(0, 1)
    g4.addEdge(0, 2)
    g4.addEdge(0, 5)
    g4.addEdge(0, 11)

    g4.addEdge(1, 0)
    g4.addEdge(1, 2)
    g4.addEdge(1, 3)
    g4.addEdge(1, 4)
    g4.addEdge(1, 6)
    g4.addEdge(1, 7)
    g4.addEdge(1, 12)

    g4.addEdge(2, 0)
    g4.addEdge(2, 1)

    g4.addEdge(3, 1)
    g4.addEdge(3, 4)

    g4.addEdge(4, 1)
    g4.addEdge(4, 3)

    g4.addEdge(5, 0)

    g4.addEdge(6, 1)
    g4.addEdge(6, 8)
    g4.addEdge(6, 7)
    g4.addEdge(6, 10)
    g4.addEdge(7, 1)
    g4.addEdge(7, 10)
    g4.addEdge(8, 6)
    g4.addEdge(9, 11)
    g4.addEdge(9, 12)
    g4.addEdge(10, 6)
    g4.addEdge(10, 7)
    g4.addEdge(11, 0)
    g4.addEdge(11, 9)
    g4.addEdge(11, 12)
    g4.addEdge(12, 1)
    g4.addEdge(12, 9)
    g4.addEdge(12, 11)
    print ("图g4是:\n%s"% (g4.graph))
    print("\nArticulation points in g4 graph ")
    g4.find_articulation_point()