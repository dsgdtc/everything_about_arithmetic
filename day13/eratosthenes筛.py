#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: eratosthenes筛.py
Author: dsgdtc@163.com
Date: 2018/2/8 20:33
给定正整数N，求小于等于N的全部素数
算法：
    将2到N写成一排
    记派头元素为X，则X是素数；除X以外，将X的倍数全部划去
    重复以上操作，直到没有元素被划去

    一直晒到sqrt(N)即可
    eg: 删完2,3,5的时候，在删7时，直接从7*7之后开始删就可以了。
"""
import math

def eratosthenes(N):
    a = [True for i in range(N+1)]
    a[0] = False
    a[1] = False # a[0]不用
    p = 2
    j = p * p
    while j <= N:
        while j <= N:
            a[j] = False # 从p*p之后开始删除
            j += p
        p += 1
        while (a[p] is False):
            p += 1
        j = p*p

    res = []
    for index, item in enumerate(a):
        if item:
            res.append(index)
    print (res)
if __name__ == "__main__":
    N = 100
    res = eratosthenes(N)
