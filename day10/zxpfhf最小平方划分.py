#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: zxpfhf最小平方划分.py
Author: dsgdtc@163.com
Date: 2018/2/6 20:16
一个正整数可以由若干个正整数的平方和
求整数201314最小的平方划分数目
eg: 10 = 1*1 + 3*3                  返回值是2
    10 = 1*1 + 1*1 + 2*2 + 2*2      返回值是4
    应该返回2

算法：
    如果已经求出了1...n-1的所有数的最小划分
    a是一个比n小的某个数，它的最小划分数是已经算好的，那么如果我们能够找到一个数字k，使得
    a + k*k = n,  则a的最小划分数+1就是n的一个候选值，把a从1...n都取一遍，看看k是否存在

    或者反着算：
        令k=1...sqrt(n)
        计算n-k*k，得到x，split[x] + 1就是n需要的划分数
        遍历完k后，找到最小值就可以了

    记split[n]是1...n-1的最小划分数目，令n的最小划分数目为x，初始化为n
    记k：遍历1...sqrt(n)
        若split[k] + 1 < x，则将x更新为split[k] + 1
    x即为n的最小划分数目
        赋值split[n] = x，为计算更大的n做准备

"""

import math

# def _print(N, pre):
#     while (N!=0):
#

def function(N):
    min_split = [0] * (N+1)
    pre = [0] * (N+1)
    for n in range(1, N+1):
        K = math.sqrt(n)
        K = math.floor(K) # n的平方根向下取整
        if K*K == n:
            min_split[n] = 1
            pre[n] = 0
            continue
        min_split[n] = n # 默认分成n份
        pre[n] = n-1    # n份，则前驱是n-1
        for k in range(1, K+1):
            t = n - k*k
            if min_split[n] > min_split[t] + 1:
                min_split[n] = min_split[t] + 1
                pre[n] = t
    print(N, pre)
    print (min_split)
    return pre

if __name__ == "__main__":

    N = 10
    res = function(N)