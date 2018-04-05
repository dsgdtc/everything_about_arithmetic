#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: shudu.py
Author: dsgdtc@163.com
Date: 2018/1/4 15:20
"""
import random
import pprint

class Solution(object):

    def __init__(self, shudu):
        self.chess_shudu = shudu
        self.solve_count = 0

    def isvalid(self, i, j, k):

        # 判断行是否冲突
        row = self.chess_shudu[i][:]
        if k in row:
            # print ("第%s行为:%s"%(i, row))
            # print ("在(%s,%s)处填%s在行上冲突了"%(i,j,k))
            return False
        # 判断列是否冲突
        col = [x[j] for x in self.chess_shudu]
        if k in col:
            # print ("第%s列为:%s"%(j, col))
            # print ("在(%s,%s)处填%s在列上冲突了"%(i,j,k))
            return False
        # 判断大格子是否冲突
        i_grid_start = (i//3) * 3
        j_grid_start = (j//3) * 3
        for ii in range(i_grid_start, i_grid_start+3):
            for jj in range(j_grid_start, j_grid_start+3):
                if self.chess_shudu[ii][jj] == k:
                    # print ("在(%s,%s)处填%s在大格子上冲突了"%(i,j,k))
                    return False
        return True

    def solve(self):

        for i in range(9):
            for j in range(9):
                # 如果是0,就把1-9填一遍并校验
                if self.chess_shudu[i][j] == 0:
                    for k in range(1, 10):
                        flag1 = self.isvalid(i, j, k)
                        # 如果可以放这个数字,那就放上，然后递归继续
                        if flag1:
                            self.chess_shudu[i][j] = k
                            # print ("在(%s,%s)处放上%s,此时的数独为:"%(i,j,k))
                            # pprint.pprint(self.chess_shudu)
                            # input("etc...")
                            flag2 = self.solve()
                            if flag2 is False:
                                # print ("从(%s,%s)处拿起%s"%(i,j,k))
                                self.chess_shudu[i][j] = 0
                            else:
                                # 在这里好像可以拿到所有解,都是多重复的...
                                # self.solve_count += 1
                                # print ("一个可行的解为:")
                                # pprint.pprint(self.chess_shudu)
                                return True
                    # 如果在i,j处9个数字都放不了,那么说明填错了,显然第一次进solve是不可能的,如果第一次就没法放任何数字,说明数独天生无解
                    return False
        return True

if __name__ == "__main__":

    shudu = [[8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,8,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]]

    print ("输入的数独游戏是:")
    pprint.pprint(shudu)
    s = Solution(shudu)
    result = s.solve()
    print (result)
    print ("一个可行解为:")
    pprint.pprint(s.chess_shudu)
