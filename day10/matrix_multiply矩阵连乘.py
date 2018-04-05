#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: matrix_multiply矩阵连乘.py
Author: dsgdtc@163.com
Date: 2018/1/11 19:57
矩阵连乘，如果矩阵A1 * A2 * A3 * A4可乘，那么如何加括号

两个实数矩阵相乘（M*N）*（N*P）,需要乘法次数是M*N*P次

卡特兰数 Catalanr
n个矩阵连乘，可以分解成i个矩阵连乘和n-i个矩阵连乘，再将这两个矩阵相乘。如果我们要算n个矩阵连乘，公有多少种乘法次数
那么我们把i从1到n-1遍历，就能得到P(n) = P(1)*P(n-1) + P(2)*P(n-2) + P(3)*P(n-3) +... +P(n-1)*P(n-(n-1))
H(n) = C(2n,n)


算法：
    将矩阵连城积A(i)A(i+1)...A(i+j)记为A[i:j]
    ( A(i)A(i+1)...A(k) ) ( A(k+1)A(k+2)...A(j) )
    计算量为 A[i:k]的计算量 加上A[k+1:j]的计算量，再加上
    A[i:k]和A[k+1:j]相乘的计算量

    设计算A[i:j]所需要的最少数乘次数为m[i,j],则原问题的最优值为m[1,n];
    记A(i)的维度为p(i-1)*pi
        当i==j时，A[i:j]即A(i)本身,m[i,j]=0
        当i<j时, m[i,j] = m[i,k] + m[k+1,j] + p(i-1)p(k)p(j)
"""

def matrix_mutiply(p, n, m, s):
    """

    :param p: p[0...n]存储了n+1个数，其中,(p[i-1],p[i])是矩阵i的阶
    :param n: n个矩阵
    :param m: m[i][j]记录数乘最小值
    :param s: s[i][j]记录A[i...j]从什么位置断开
    :return:
    """
    for i in range(1, n):
        m[i][i] = 0

    for r in range(2, n):
        for i in range(1, n-r+1):
            j = i+r-1
            m[i][j] = m[i+1][j] + p[i-1]*p[i]*p[j]
            s[i][l] = i
            for k in range(i+1, j):
                t = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if (t < m[i][j]):
                    m[i][j] = t
                    s[i][j] = k



if __name__ == "__main__":


    root = 2
#    result = find_set(root)
#    print (result)
    with open("clustering_result.txt", 'w') as f:
        f.write("123")