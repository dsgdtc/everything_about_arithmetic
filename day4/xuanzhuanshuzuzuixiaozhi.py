 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: xuanzhuanshuzuzuixiaozhi.py旋转数组最小值
假定一个排序数组以某个未知元素为支点做了旋转
如：原数组0124567旋转后4567012，请找出旋转后数组的最小值
假定数组没有重复数字
Author: dsgdtc@163.com
Date: 2017/10/27 21:08
二分
"""

def func(a, size):
    low = 0
    high = size - 1
    while (low < high):
        mid = (low + high) // 2
        # print (mid)
        if a[mid] < a[high]:
            high = mid
        elif a[mid] > a[high]:
            # 说明从mid到high里有旋转数组,left到mid是正常升序数组,仍带left到mid部分
            low = mid + 1
    return a[low]


if __name__ == '__main__':

    l = [0,1,2,4,5,6,7]
    l = [4,5,6,7,0,1,2]
    size = len(l)
    print ("Origin list: %s" %(l))
    res = func(l, size)
    print (res)