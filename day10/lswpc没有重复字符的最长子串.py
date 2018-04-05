#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: lswpc没有重复字符的最长子串.py
Author: dsgdtc@163.com
Date: 2018/1/11 20:59
无重复字符最长子串。好像就是字符串去重后剩下的字符串的长度, 子串，不是子序列
eg:
abcabcbb的最长无重复子串是abc

字符串只包含26个小写字母
时间复杂度O(n)，空间复杂度O(n)。
"""
def lengthOfLongestSubstring(s, size):
    res = 0
    if s is None or len(s) == 0:
        return res

    exist = {}
    max_length = 0
    start = 0 # 当前子串的起始位置

    for i in range(size):
        print (i, s[i])
        print (exist)
        print (start)
        input("etc...")
        # 循环整个字符串,如果字符串在exist中出现过 并且上一次出现该字符时的位置 >= 子串start位置
        # exist[s[i]]表示该字符上一次出现的位置
        if s[i] in exist and exist[s[i]] >= start:
            # start是新的子串的开始位置
            print ("字符%s在exist中出现过,位置是%s, 此时start是%s" %(s[i], exist[s[i]], start))
            start = exist[s[i]] + 1
            print ("更新start为%s" %(start))
        max_length = i - start + 1
        exist[s[i]] = i
        res = max(res, max_length)
        print (exist)
        print ("待比较子串起始位置为:%s" %(start))
        print ("最长子串长度为%s" %(res))
        print ("-" * 50)
        input("etc...")

    return res

if __name__ == "__main__":
    string = "abcdabcbb"
    string = list(string)
    size = len(string)
    result = lengthOfLongestSubstring(string, size)
    print ("最长子串长度是%s" %(result))