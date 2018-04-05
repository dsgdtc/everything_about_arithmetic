#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: erfenchazhao.py 有序数组的二分查找
Author: dsgdtc@163.com
Date: 2017/10/26 21:38
"""

def erfen_find(l, size, value):

    _from = 0
    _to = size - 1
    find_flag = False
    while _from < _to:
        mid = (_from + _to) // 2
        if l[mid] == value:
            find_flag = True
            break
        elif l[mid] < value:
            _from = mid + 1
        elif l[mid] > value:
            _to = mid - 1

    return find_flag



if __name__ == '__main__':

    l = [3,5,1,2,2,9,3,7,14,8]
    l.sort()
    size = len(l)
    value = 9
    print ("Origin list: %s, find value: %s" %(l, value))

    result = erfen_find(l, size, value)
    print ("是否找到值:%s %s" %(value, result))