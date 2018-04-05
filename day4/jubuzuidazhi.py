#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: jubuzuidazhi.py局部最大
Author: dsgdtc@163.com
Date: 2017/10/27 19:56
给定一个无重复元素的数组A[0...N-1]，求找到一个该数组的局部最大值  nlogN时间复杂度
高原数组
循环不变式：一个问题，最开始是对的，每次推导式对的，则结论是对的
"""
def jubuzuida(l, size):
    _from = 0
    _to = size
    while _from != _to:
        mid = (_from + _to) // 2
        if l[mid] < l[mid+1]:
            _from = mid + 1
        else: #l[mid] >= l[mid+1]
            _to = mid
    return [_from, l[_from]]

if __name__ == '__main__':

    l = [3,1,1,1,1,2,3,5,1,1]
    size = len(l)
    print ("Origin list: %s" %(l))
    result = jubuzuida(l, size)
    print ("局部最大值为: %r" %(result))
