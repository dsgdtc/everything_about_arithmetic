#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: k个不同字符的最长子串.py
Author: dsgdtc@163.com
Date: 2017/11/6 20:17
如:给定字符串eceba和k=3，则包含3个不同字符的最长子串为eceb
算法描述:
使用双索引i,j,初始值为0，考察字符串string[i,j]
记'子串str[i,j]中包含的不同字符数目小于等于K'这个命题为A
若子串str[i,j]满足A，则j++
若子串str[i,j]不满足A，则i++
继续考察str[i,j]是否满足A
"""
def func(l, size, k):
    if k<= 0:
        return 0

    left = 0
    right = 0
    mx = 0

    # for i in range(size):
    while right <= size:
        input("\nenter...")
        print ("截取的字符串为:%s, right为:%s" %(l[left:right], right))
        checking_str = set(l[left:right])

        if len(checking_str) <= k:
            right = right + 1
            print (right, left, list(checking_str))
        else:
            left = left + 1
            print (right, left, list(checking_str))

        mx = max(len(checking_str), mx)
        print ("max is:%s" %(mx))
    return mx




if __name__ == '__main__':

    string = 'eceba'
    l = list(string)
    size = len(l)
    k = 3
    print ("Origin string list: %s" %(l))
    count = func(l, size, k)
    print ("结果是 %s" %(count))