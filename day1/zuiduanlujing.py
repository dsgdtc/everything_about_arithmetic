#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: zuiduanlujing.py
Author: dsgdtc@163.com
Date: 2017/9/11 21:00
"""


import numpy as np
from queue import Queue

q = Queue(999)

def init_memset():
    g = np.zeros([16,16])
    g[0][1] = g[0][4] = 1
    g[1][5] = g[1][0] = g[1][2] = 1
    g[2][1] = g[2][6] = g[2][3] = 1
    g[3][2] = g[3][7] = 1
    g[4][0] = g[4][5] = 1
    g[5][1] = g[5][4] = g[5][6] = g[5][9] = 1
    g[6][2] = g[6][5] = g[6][7] = g[6][10] = 1
    g[7][3] = g[7][6] = 1
    g[8][9] = g[8][12] = 1
    g[9][8] = g[9][13] = g[9][10] = 1
    g[10][9] = g[10][14] = g[10][11] = 1
    g[11][10] = g[11][15] = 1
    g[12][8] = g[12][13] = 1
    g[13][9] = g[13][12] = g[13][14] = 1
    g[14][10] = g[14][13] = g[14][15] = 1
    g[15][11] = g[15][14] = 1
    return g


if __name__ == '__main__':
    g = init_memset()
    """
    给定节点步数step[0...N-1]，初始化为0，如果step[i]是0，表示之前没有人来过这个点
    路径树木path_number[0...N-1],表示从起点0到节点i的最短路径的条数是几条，迪杰斯特拉算法的想法
    path_number[0]:从起点0到起点0的条数：1条

    若从当前节点i扩展到邻近节点j时：
    若step[j] == 0那么说明没有人来过j，此时
        step[j] = step[i] + 1, path_number[j] = path_number[i]
    若step[j]!=0时，则step[j] 一定== step[i] + 1,说明之前有人到达过这个节点，最短路径是任何到达j节点的i节点的最短路径加上j节点的最短路径，是个不断累加的过程
        path_number[j] += path_number[i]
    到达N时终止
    """
    print (g)
    N = 16
    # print (g[1][4])
    step = [0] * N
    step[0] = 0
    path_number = [1] * N
    path_number[0] = 1
    q.put(0)
    # while not (q.empty()):
    for _from in range(N):
        # _from = q.get()
        print ("x" * 50)
        print ("从起点%s开始检查" % (_from))
        # print ("队列中还有:%s" % (q.queue))
        s = step[_from] + 1
        # input()
        for _to in range(N):
            # 表示节点连通, == 0是不联通的,比如g[0][1] == 1
            print ("循环到%s终点" %(_to))
            if g[_from][_to] == 1:
                print ("发现可连接到该节点")
                print ("step[_to]: %s" % (step[_to]))
                print ("from %s to %s" % (_from, _to))
                # print ("当前节点的最短路径条数: %s" % (%path_number[_to]))
                # step[_to] == 0表示没有人来过这个节点,step[_to] > s本题中不可能，因为路径长度均为1
                # print ("before handle: step[_to]: %s, path_number[_from]: %s" % (step[_to], path_number[_from]))
                # if (step[_to] == 0 or step[_to] > s):
                if (step[_to] == 0):
                    # 之前s 已经等于step[_from] + 1
                    step[_to] = s
                    path_number[_to] = path_number[_from]
                    q.put(_to)
                    # input("节点为首次访问,将节点压入队列,之后再检查: %s" %(_to))
                    input("节点为首次访问: %s" %(_to))
                elif step[_to] == s:
                    path_number[_to] = path_number[_to] + path_number[_from]
                    print ("之前有人访问过此节点:%s" %(_to))
                    print (path_number[_to] , path_number[_from])
                if _to > _from:
                    print ("path_number[_from]:%s" %(path_number[_from]))
                    print ("从0出发,到达%s后，再从%s出发到达%s的最短路径长度是: %s  (0 means never coming)" % (_from, _from, _to, step[_to]))
                # print ("当前节点%s的最短路径条数: %s" % (_to, path_number[_to]))

    print (path_number[N-1])
    print (path_number)
