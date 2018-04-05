#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: zhongshu.py 绝对众数的计算：
给定N个数，称出现次数最多的数为众数，若某众数出现次数大于N/2，称该众数为绝对众数
Author: dsgdtc@163.com
Date: 2017/10/27 19:45
"""
def jueduizhongshu(l, size):
    count = 0
    m = l[0]
    for i in range(size):
        if count == 0:
            count = 1
            m = l[i]
        elif m != l[i]:
            count -= 1
        else: # m == l[i]
            m = l[i]
            count += 1
    return m



if __name__ == '__main__':

    l = [3,1,1,1,1,2,3,5,1,1]
    size = len(l)
    print ("Origin list: %s" %(l))
    result = jueduizhongshu(l, size)
    print ("绝对重数为: %s" %(result))