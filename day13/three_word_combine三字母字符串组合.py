#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: three_word_combine三字母字符串组合.py
Author: dsgdtc@163.com
Date: 2018/2/12 11:27
仅由三个字符A,B,C构成字符串，且字符串任意三个相邻元素不能完全相同。eg：ACCCAB不合法
求满足条件的长度为N的字符串个数
不考虑整数溢出
要求时间和空间复杂度不高于O(N)
计算n时，先考虑长度为n-1的合法字符串，在n-1长度的字符串末端增加一个字符，形成长度为n的字符串
将长度为n-1字符串分成"末尾两个字符不相等"和"末尾两个字符相等"
                       dp[n][0]             dp[n][1]

在纸上画
dp[n][0] = 2*dp[n-1][0] + 2*dp[n-1][1]
dp[n][1] = dp[n-1][0] + 0*dp[n-1][1]

初始条件
dp[1][0] = 3
dp[1][1] = 0
滚动数组做优化，把初始条件全部划掉

用矩阵计算，A[n] = A[0] * (2,1)的n-1次幂
                          (2,0)
"""

def func(size):

    dp = [[0 for j in range(2)] for i in range(size+1)]
    dp[1][0] = 3
    dp[1][1] = 0

    for n in range(2, size+1):
        dp[n][0] = 2*dp[n-1][0] + 2*dp[n-1][1]
        dp[n][1] = 1*dp[n-1][0] + 0*dp[n-1][1]

    print (dp)
    return dp[size][0] + dp[size][1]


if __name__ == "__main__":

    size = 6
    res = func(size)
    print ("长度为%s时，满足题目要求的字符串数量为:%s" %(size, res))