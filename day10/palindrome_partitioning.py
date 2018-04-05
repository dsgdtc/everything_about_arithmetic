#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: palindrome_partitioning.py
Author: dsgdtc@163.com
Date: 2018/2/7 18:00
palindrome:回文
给定一个字符串str,将str划分成若干子串，使得每一个子串都是回文串。
在所有可能的划分中，子串数目最少是多少？
II：计算所有的可能的划分？ 没听懂

小算法：用O(1)的时间复杂度判断一个字符串是否是回文的p[i][j] is True?
先算一遍，存到O(n)的一个空间里，再判断是就可以用了。
"""

if __name__ == "__main__":

    str  = "abacdccdaa"