#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: lcs.py
Author: dsgdtc@163.com
Date: 2017/10/5 23:41
http://blog.chinaunix.net/uid-26548237-id-3374211.html
http://blog.csdn.net/littlethunder/article/details/25637173
最长公共子序列
算法：
    若X[m] == Y[n] (最后一个字符相同)，则X[m]与Y[m]的最长
    公共子序列Z[k]的最后一个字符必定为X[m](=Y[n])
    LCS(X,Y) = LCS(X[:m-1], Y[:n-1]) + X[m]
    若X[m] != Y[n]
        要么 LCS(X,Y) = LCS(X[:m-1], Y[:n])
        要么 LCS(X,Y) = LCS(X[:m], Y[:n-1])
        LCS(X[m],Y[n]) = max{ LCS(X[:m-1], Y[:n]), LCS(X[:m], Y[:n-1]) }

    用c[i][j]记录X[i]和Y[j]的最长公共子序列的长度

    c[i][j] = 0                           当i = 0, j = 0 时
            = c[i-1][j-1] + 1             当i>0,j>0,xi == yi
            = max{ c[i-1][j], c[i][j-1] }  当i>0,j>0,xi != yi

"""



import numpy as np
import sys
import pprint
sys.setrecursionlimit(204800)

def lcs(x, y):

    c = np.zeros((len(x)+1, len(y)+1))
    # flag = np.zeros((len(x)+1, len(y)+1))
    flag = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    print ("x: %s \ny: %s" %(x,y))
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            if x[i] == y[j]:
                c[i+1][j+1] = c[i][j] + 1
                flag[i+1][j+1] = 'ok'

            elif c[i+1][j] > c[i][j+1]:
                c[i+1][j+1] = c[i+1][j]
                flag[i+1][j+1] = 'left'
            else:
                c[i+1][j+1] = c[i][j+1]
                flag[i+1][j+1] = 'up'

                # c[i+1][j+1] = max(c[i+1][j], c[i][j+1])
    print (c)
    pprint.pprint(flag)
    # print (c[1][4])
    return c, flag

lcs_text = []
def lcsprint(flag, x, i, j):
    if i == 0 or j == 0:
        return
    elif flag[i][j] == 'ok':
        lcs_text.append(x[i-1])
        lcsprint(flag, x, i-1, j-1)
    elif flag[i][j] == 'left':
        lcsprint(flag, x, i, j-1)
    elif flag[i][j] == 'up':
        lcsprint(flag, x, i-1, j)

if __name__ == '__main__':

    """
    求解最长公共子序列，动态规划的方法
    注意区别最长公共子串
    算法思想:
    if x[m] == y[n]:
        lcs(x, y) = lcs(x[m-1], y[n-1]) + 1
    else:
        lcs(x, y) = max(lcs(x[m-1], y[n]), lcs(x[m], y[n-1]))
    算法中的数据结构:
        二维数组c[m,n]
        c = np.zeros([m,n])
        c[i,j]记录序列x[i], y[j]的最长公共子序列的长度，当i=0或j=0时,空序列是x,y的最长公共子序列,故c[i,j] = 0
    """
    x = 'abcbdab'
    y = 'bdcaba'
    list_x = list(x)
    list_y = list(y)
    lcs_map, lcs_flag = lcs(list_x, list_y)
    print ("lcs长度: %s" %(lcs_map[len(x)][len(y)]))
    lcsprint(lcs_flag, x, len(x), len(y))
    lcs_text.reverse()
    print ("最长子序列为: %s" %(lcs_text))