#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: spf.py
Author: dsgdtc@163.com
Date: 2017/11/13 20:35
最短路径SPF 最短路径是多少问题
dijkstra算法，时间复杂度是n2,实际用途中n2不好实现，用邻接矩阵做数据结构，dijkstra属于广度优先搜索
http://blog.csdn.net/u010558281/article/details/53905807
https://www.cnblogs.com/biyeymyhjob/archive/2012/07/31/2615833.html

2、启发式搜索 A*算法(107分钟附近)
"""
import copy
class Graph(object):

    def __init__(self, graph, node):
        self.size = len(graph)
        if self.size == 0:
            self.graph = None
        else:
            self.graph = graph
            self.node = node

    def dijkstra(self, start_node):
        if self.graph is None:
            return None,None

        # 集合source:初始时，集合source只包含原点。已求出最短路径的节点集合
        source = [start_node]
        # 其余未确定最短路径的节点集合
        other_nodes = copy.deepcopy(self.node)
        other_nodes.remove(start_node)
        # 源点start_node到各个节点的距离
        s_distance = {start_node:0}
        for i in other_nodes:
            s_distance[i] = self.graph[start_node-1][i-1]
        # print (start_node, others)
        print ("源点%s到各节点的距离:%s" %(start_node,s_distance))
        input()
        path = {start_node:{start_node:[]}}  #记录路径用的

        mininum_node = None
        pre = start_node
        while other_nodes:
            mininum_dist = 9999
            for mid_node in source:
                for end_node in other_nodes:
                    start_node_index = start_node - 1
                    end_node_index = end_node - 1
                    mid_node_index = mid_node - 1

                    # 当start_node是1时，这个是1--1距离+ 1--2距离
                    new_dist = self.graph[start_node_index][mid_node_index] + self.graph[mid_node_index][end_node_index]
                    print ("从节点%s到节点%s的距离为%s,通过中间节点%s" %(start_node, end_node, new_dist, mid_node))
                    if mininum_dist < new_dist:
                        mininum_dist = mininum_dist
                    else:
                        mininum_dist = new_dist
                        self.graph[start_node_index][end_node_index] = mininum_dist
                        pre = mid_node
                        mininum_node = end_node

            s_distance[mininum_node] = mininum_dist
            print (mininum_dist, mininum_node)
            print ("把%s加入到集合source中" % (mininum_node))
            source.append(mininum_node)
            other_nodes.remove(mininum_node)
            print(source)



            # distance = self.graph[start_node][end_node]



        return s_distance,None

if __name__ == '__main__':
    # 从1开始数，不要从0
    node_list = [1, 2, 3, 4, 5, 6, 7]
    graph_list = [
            [0, 20, 50, 30, 9999, 9999, 9999],
            [9999, 0, 25, 9999, 9999, 70, 9999],
            [9999, 9999, 0, 40, 20, 50, 9999],
            [9999, 9999, 9999, 0, 55, 9999, 9999],
            [9999, 9999, 9999, 9999, 0, 10, 70],
            [9999, 9999, 9999, 9999, 9999, 0, 50],
            [9999, 9999, 9999, 9999, 9999, 9999, 0]
    ]
    g = Graph(graph_list, node_list)
    start_node = 1
    distance, path = g.dijkstra(start_node)
    print ("从%s开始到各个节点的最短路径长度为:%s" %(start_node, distance))
    # print ("从v0开始到各个节点的最短路径次序为" %(path))

