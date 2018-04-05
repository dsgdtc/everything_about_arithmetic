#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#

"""
File: surround regional周围的区域.py
Author: dsgdtc@163.com
Date: 2017/12/26 20:54
围湖造田
给定M*N的二维平面，格点处要么是X，要么是O。将完全由X围成的区域中的O替换成X
数据是4向联通
算法：
找出那些O是应该保留的:边界的O保留，能和边界O联通的O保留

1：对于每一个边界O为起点，做若干次广度优先搜索，对于搜索到的O，标记为Y
2：再遍历一次整个图，把Y恢复成O，把O替换成X

X X X X         X X X X
X O O X   -->   X X X X
X X O X         X X X X
X O X X         X O X X
"""

import random
import pprint

class Solution(object):

    def __init__(self, graph, M, N):
        self.graph = graph
        self.M = M
        self.N = N
        self.q = []
    def solve(self):


        def fill_lake(x, y):
            # print ("坐标是(%s,%s)" %(x,y))
            if x<0 or x>self.M-1 or y<0 or y>self.N-1:
                pass
                # print("出界了")
            else:
                # print(self.graph[x][y])
                if self.graph[x][y] != "O":
                    return
                self.q.append((x, y))
                self.graph[x][y] = "Y"

        def bfs(x, y):

            i_direct = [-1, 1, 0, 0]
            j_direct = [0, 0, -1, 1]

            if self.graph[x][y] == "O":

                self.q.append((x,y))
                fill_lake(x, y)

            while len(self.q) != 0:
                coordinate = self.q.pop()
                i = coordinate[0]
                j = coordinate[1]
                for step in range(4):
                    fill_lake(i+i_direct[step], j+j_direct[step])


        if len(self.graph) == 0:
            return self.graph

        # 遍历边界,进行bfs搜索，把需要保留的O改写成Y
        for i in range(M):
            # 遍历第一列和最后一列
            bfs(i, 0)
            bfs(i, self.N-1)
        for j in range(N):
            bfs(0, j)
            bfs(self.M-1, j)

        for i in range(M):
            for j in range(N):
                if self.graph[i][j] == "O":
                    self.graph[i][j] = "X"
                if self.graph[i][j] == "Y":
                    self.graph[i][j] = "O"
        return self.graph

if __name__ == "__main__":

    # 生产随机图
    # M*N M行N列
    M = 10
    N = 10
    graph = [["X" for j in range(N)] for i in range(M)]
    random.seed(1)
    for i in range(M):
        for j in range(N):
            if random.randint(1,10) % 3 == 1:
                graph[i][j] = "O"
    print ("Origin graph is:")
    pprint.pprint (graph)
    s = Solution(graph, M, N)
    graph_solved = s.solve()
    print("变换后:")
    pprint.pprint(graph_solved)





