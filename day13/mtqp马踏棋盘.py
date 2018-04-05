#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: mtqp马踏棋盘.py
Author: dsgdtc@163.com
Date: 2018/2/8 20:41

按照DFS做，因为提前知道能够遍历所有点，所以选择[0][0]作为起点即可
i_horse = [-2, -2, -1, +1, +2, +2, +1, -1]
j_horse = [-1, +1, +2, +2, +1, -1, -2, -2]
棋盘较大时，速度很慢（7的时候我就很慢了）
启发式策略：
    最多情况下，每个棋位有8个后继，由于棋盘边界和已经遍历的原因，往往是小于8个的。
    记当前棋位可跳转的后继棋位数量为X个，这X个棋位的后继棋位数目记为h1h2h3...hx，优先选择最小的hi
"""
import pprint
import sys
sys.setrecursionlimit(150000)

class Chess(object):

    def __init__(self, M, N):
        self.M = M
        self.N = N
        self.i_horse = [-2, -2, -1, +1, +2, +2, +1, -1]
        self.j_horse = [-1, +1, +2, +2, +1, -1, -2, -2]
        self.chess = [[0 for j in range(N)] for i in range(M)]

    def can_jump(self, i, j):
        # 越界了
        if i < 0 or i >= self.M or j < 0 or j >= self.N:
            return False
        # 之前已经有人访问过,不能再访问
        elif self.chess[i][j] != 0:
            return False
        # chess[i][j] == 0表示没人访问,可以踩这个点
        else:
            return True

    def jump(self, i, j, step):

        if step == self.M * self.N:
            # print (self.chess)
            return True

        for k in range(8):
            i_current = i + self.i_horse[k]
            j_current = j + self.j_horse[k]
            if self.can_jump(i_current, j_current):
                # 如果当前点的这个邻域可以被访问，就跳过来
                # print ("当前的棋盘是:")
                # pprint.pprint (self.chess)
                # input("etc...")
                self.chess[i_current][j_current] = step + 1
                if self.jump(i_current, j_current, step+1):
                    return True
                # 如果调过来后的这个点的八邻域都被访问过，那么这个点就没法跳了，回溯
                self.chess[i_current][j_current] = 0
        return False


if __name__ == "__main__":

    M = 7
    N = 7
    chess = Chess(M, N)
    # 从(0,0)点开始跳,当前步数是1
    chess.chess[0][0] = 1
    res = chess.jump(0, 0, 1)
    print (chess.chess)
