#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: diyigequeshidezhengshu.py第一个缺失的整数
Author: dsgdtc@163.com
Date: 2017/10/27 20:11
加一个缓冲区可以是 时间O(N)，空间O（N）复杂度来找到

用时间O(N) 空间O(1)最优
从前到后遍历，然后归为
将找到的元素放到正确的位置上，如果最终发现某个一直没有找到则该元素即为所求
循环不变式:如果命题初始为真，且每次更改后仍然保持该命题为真，则若干次更改后该命题仍然为真
"""


def func(a, size):
    # while
    i = 0
    while i < size:
        print ("检查位置:%s,当前列表:%s" %(i, a))
        if a[i]-1 == i:
            i = i + 1
        elif a[i] < i or a[i] > size or a[i] == a[a[i]-1]:
            # a[i] = -999
            a[i] = a[-1]
            del a[-1]
            # i = i + 1
            size = size - 1
        else:
            print ("交换位置%s和位置%s" %(i, a[i]-1))
            print (a[i], a[a[i]-1])
            tmp = a[a[i]-1]
            a[a[i]-1] = a[i]
            a[i] = tmp

if __name__ == '__main__':

    l = [3,5,1,2,-3,7,14,8]
    size = len(l)
    print ("Origin list: %s" %(l))
    func(l, size)