#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: lingzishuzu.py
求对于长度为N的数组A，求连续子数组的和最接近0的值
sum(a[i...j]) = sum(a[0...j]) - sum(a[0...i])
对前N项和排序，找到最接近
Author: dsgdtc@163.com
Date: 2017/10/29 18:10
需要求子数组本身？
"""

def func(a, size):
    sum_a = [0] * (size + 1)
    sum_b = []
    for i in range(0, size):
        sum_a[i+1] = sum_a[i] + a[i]
    print ("前N项和:%s" % sum_a)
    for i in range(len(sum_a)):
        sum_b.append((i, sum_a[i]))

    print ("带序号的前N项和:%s" % sum_b)
    sum_a = sorted(sum_a)
    print (sum_a)

    diff = abs(sum_a[1]-sum_a[0])
    result = diff
    for i in range(1, size):
        diff = abs(sum_a[i+1] - sum_a[i])
        result = min(diff, result)
    return result


if __name__ == '__main__':

    l = [1,-2,3,10,-4,7,2,-5]
    size = len(l)
    print ("Origin list: %s, size is:%s" %(l,size))
    res = func(l, size)
    print (res)