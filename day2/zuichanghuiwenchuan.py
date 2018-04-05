#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: zuichanghuiwenchuan.py
Author: dsgdtc@163.com
Date: 2017/10/16 20:51
O(n2)：枚举回文串的中点

最长回文子串。用O(n)时间复杂度做
Longest Palindromic Substring
LPS
回文分奇数和偶数，分开讨论
马拉车算法 manacher算法
http://blog.csdn.net/dyx404514/article/details/42061017
"""

def palindromic(x):

    length = len(x)
    if length == 1:
        return 1

    lps_left = 0
    lps_right = 0
    max = 0
    for i in range(0, length-1):
        # 奇数的情况
        middle = i
        left = i - 1
        right = i + 1
        # print (x[i])
        while left >= 0 and right < length:
            # input()
            # print(left, right, "最长回文长度为:",max)
            # print ("左元素为:%s, 中间元素为:%s, 右元素为:%s" %(x[left], x[middle], x[right]))
            if x[left] == x[right]:
                # print ("是回文")
                if right - left + 1 > max:
                    max = right - left + 1
                    lps_left = left
                    lps_right = right
                left = left - 1
                right = right + 1
            else:
                # print ("不是回文,继续找")
                break

        # 偶数的情况
        left = i
        right = i + 1

        while left >= 0 and right < length:
            # print(left, right, "最长回文长度为:",max)
            if x[left] == x[right]:
                if right - left + 1 > max:
                    lps_left = left
                    lps_right = right
                    max = right - left + 1
                left = left - 1
                right = right + 1
            else:
                break
    return (lps_left, lps_right, x[lps_left:lps_right+1])




if __name__ == '__main__':
    x = '1221234'
    list_x = list(x)
    print ("原始字符串:%s" %(list_x))
    left,right,lps = palindromic(list_x)
    print (left,right,lps)