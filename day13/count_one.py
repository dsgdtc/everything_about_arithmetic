#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: count_one.py
Author: dsgdtc@163.com
Date: 2018/2/8 20:25
给定一个32位无符号整数N，求整数N的二进制中1的个数
思路：
    不断的将整数N右移，判断当前的数字的最低位是否为1，直到整数N为0为止
"""


def func(N):

    count = 0
    bin_num = []
    while N != 0:
        s = N % 2
        bin_num.append(s)
        if s == 1:
            count += 1
        N = N // 2
    bin_num.reverse()
    return bin_num

if __name__ == "__main__":
    N = 33
    res = func(N)
    print (res)