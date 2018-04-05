#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: callatz猜想.py
Author: dsgdtc@163.com
Date: 2018/2/8 20:23
又称3n+1猜想,角谷猜想
给定某正整数N，若为偶数，则N被更新为N/2，否则N被更新为3*N + 1，问：
（1）经过多少步N变成1,
（2）是否存在某整数X无法变成1


"""

def func(num):
    t = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            t += 1
        else:
            num = num * 3 + 1
            t += 1
    print ("用的次数:%s" %(t))


if __name__ == "__main__":
    N = 100
    res = func(N)