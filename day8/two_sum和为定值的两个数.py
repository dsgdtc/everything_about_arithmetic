#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: sum_constant和为定值的两个数.py
Author: dsgdtc@163.com
Date: 2018/1/4 17:37
1、暴力求解O(n2)
2、先排序，再两头扫，O(nlogn+n) = O(nlogn)
3、Hash, O(1)
用两头扫就足够，Hash理解原理即可
"""

def two_sum(a, size, Sum):
    i= 0
    j = size -1
    while i < j:
        if a[i] + a[j] < Sum:
            i += 1
        elif a[i] + a[j] > Sum:
            j -= 1
        else:
            i += 1
            j -= 1
            print ("%s + %s = %s" %(a[i], a[j], Sum))

if __name__ == "__main__":

    a = [0,3,7,9,11,14,16,17]
    size = len(a)
    Sum = 20
    two_sum(a, size, Sum)


