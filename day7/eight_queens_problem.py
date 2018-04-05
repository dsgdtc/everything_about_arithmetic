#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: eight_queens_problem.py
Author: dsgdtc@163.com
Date: 2018/1/3 16:55
算法：
显然任意一行有且仅有1个皇后，使用list queen[]表示第i行的皇后位于哪一类
eg:
queen[0] = 3 表示第0行第3列放皇后
queen[1] = 6 表示第1行第6列放皇后
........
queen[7] = 5 表示第7行第5列放皇后
八皇后问题就变成了一个0,1,2,3,4,5,6,7的全排列问题，再加入分支界限的条件判断是否相互攻击

深度优先搜索：
    将第i个皇后放置在第j列上，如果当前皇后与其他皇后互相攻击，则剪枝掉该节点
    分析对角线：
        主对角线：主对角线上(i-j)为定值，取值范围是-(size-1) <= (i-j) <= size-1,从而：0 <= (i-j + size - 1) <= 2*size - 2
        次对角线：(i+j)为定值 取值范围 0 <= (i+j) <= 2*size -2
"""
import random
import pprint

class Solution(object):

    def __init__(self, queen, size):
        # self.queen:一个可行解
        self.queen = queen

        self.size = size

        # self.occupy_col = [False] * size
        # self.occupy_main_diagonal = [False] * (2*size -1)
        # self.occupy_minor_diagonal = [False] * (2*size-1)

    def conflict(self, x, y):

        # print ("判断列,主对角线,次对角线是否被占据:")
        # print (self.occupy_col[y])
        # print (self.occupy_main_diagonal[self.size - 1 + x - y])
        # print (self.occupy_minor_diagonal[x + y])
        if not self.occupy_col[y] and not self.occupy_main_diagonal[self.size - 1 + x - y] and not self.occupy_minor_diagonal[x + y]:
            return True
        else:
            return False

    def is_answer(self, queen):
        # print("一个待检查的解为:%s" %(self.queen))
        # 每检查完一个解后要清空占据的标记
        occupy_col = [False] * self.size
        occupy_main_diagonal = [False] * (2 * self.size - 1)
        occupy_minor_diagonal = [False] * (2 * self.size - 1)
        # if self.queen == [2,0,3,1]:
        for x in range(0, self.size):
            y = self.queen[x]
            # print ("第%s行的皇后坐标(%s,%s)" %(x, x, y))
            if not self.conflict(x,y):
                # print ("冲突了,不能放,直接剪枝,这个解不可行")
                # input("etc...")
                return False
            else:
                # print("没冲突，可以放")
                # input("etc...")
                occupy_col[y] = True
                occupy_main_diagonal[self.size - 1 + x - y] = True
                occupy_minor_diagonal[x + y] = True
                # print ("皇后占据的列:      %s" %(occupy_col))
                # print ("皇后占据的主对角线:%s" %(occupy_main_diagonal))
                # print ("皇后占据的次对角线:%s" %(occupy_minor_diagonal))

        return True
    def solve(self, row):
        """
        graph, M, N, size
        :return:
        """
        if row == self.size - 1:
            # 输出一种全排列的方法
            # 一共size!种排列方法，每种方法去做个校验
            if self.is_answer(self.queen):
                print ("一个可行的结果:%s" %(self.queen))
                pass
        for i in range(row, self.size):
            # print ("col is:%s\nrow is: %s\n" %(i, row))
            # input("etc...")
            self.queen[i], self.queen[row] = self.queen[row], self.queen[i]
            self.solve(row+1)
            self.queen[i], self.queen[row] = self.queen[row], self.queen[i]



if __name__ == '__main__':


    size = 8
    graph = [["O" for j in range(size)] for i in range(size)]
    random.seed(1)
    # for i in range(M):
    #     for j in range(N):
    #         if random.randint(1, 10) % 5 == 1:
    #             graph[i][j] = "O"
    print ("Origin graph is:")
    # graph[5][5] = 9
    pprint.pprint (graph)
    # queen = [0,1,2,3,4,5,6,7]
    queen = [i for i in range(size)]
    s = Solution(queen, size)
    graph_solved = s.solve(0)
    # print ("找到路径:%s" %(s.path))