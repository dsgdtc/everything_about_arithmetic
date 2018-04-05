#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: distinct_subsequences子序列数目.py
Author: dsgdtc@163.com
Date: 2018/1/11 20:49
给定文本串TEXT和模式串Pattern,计算问恩串Text的子序列中包含模式串Pattern的个数
eg:
rabbit在rabbbit中出现过3次
借用day2的lcs思想

算法：
    记pattern[0...j]在text[0...i]中出现的次数为dp[i][j]
    从最后一个字母看
    若pattern[j] != text[i]
        则text[0...i]和text[0...i-1]对于pattern[0...j]的表达能力是相同的

    若pattern[j] == text[i]
        text[0...i-1]表达完pattern[0...j-1]后，最后缀上text[i]
        或者text[0...i-1]直接表达pattern[0...j]
        即：dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    dp[i,0] = 1空串在任何串中都出现了一次

"""
import pprint
def distinct_subsequences(text, pattern):


    size_pattern = len(pattern)
    size_text = len(text)
    dp = [[0 for j in range(size_pattern)] for i in range(size_text)]
    for i in range(size_text):
        dp[i][0] = 1
    for i in range(size_text):
        for j in range(size_pattern-1, 0, -1):
            if pattern[j] == text[i]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    pprint.pprint (dp)
    return dp[size_text-1][size_pattern-1]


if __name__ == "__main__":
    text = "rabbbit"
    pattern = "rabbit"
    res = distinct_subsequences(text, pattern)
    print(res)
