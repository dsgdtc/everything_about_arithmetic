#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: helanguoqi.py
现有红白蓝三个不同颜色的小球，乱序排列在一起，请重新排列这些小球，使得红白蓝三色的同色的球在一起
Author: dsgdtc@163.com
Date: 2017/10/29 18:54
问题转换，给定数组A[0...N-1]，元素只能取0,1,2三个值，设计算法
使得数组排序成“000011112222”的形式
"""

def func1():
    """
    while current <= end
    当a[current] == 2时 a[current]和a[end]交换,end --
    当a[current] == 1时 current++,begin,end不变
    当a[current] == 0时:
        如果begin == current: begin++,current++
        else： a[current]和a[begin交换] begin++,current不变(优化current++)
    :return:
    """



if __name__ == '__main__':

    l = [1,-2,3,10,-4,7,2,-5]
    size = len(l)
    print ("Origin list: %s, size is:%s" %(l,size))
    res = func(l, size)
    print (res)
