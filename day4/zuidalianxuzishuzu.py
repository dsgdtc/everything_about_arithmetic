#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: 最大连续子数组.py
求对于长度为N的数组A，求连续子数组最大值
S[i+1] = Max(S[i]+A[i+1], A[i+1])
Author: dsgdtc@163.com
Date: 2017/10/29 18:29
"""


def func(a, size):
    _sum = a[0]
    result = _sum
    for i in range(0, size):
        if _sum > 0:
            _sum = _sum + a[i]
        else:
            _sum = a[i]
        result = max(_sum, result)

    return result


if __name__ == '__main__':

    l = [1,-2,3,10,-4,7,2,-5]
    size = len(l)
    print ("Origin list: %s, size is:%s" %(l,size))
    res = func(l, size)
    print (res)