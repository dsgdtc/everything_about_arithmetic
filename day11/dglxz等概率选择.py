# -*- coding: utf-8 -*-
"""
从N个元素中等概率的选取k个元素
开辟缓冲区a[0...k-1]
将N的前k个元素放入缓冲区a
对于第i(i>k)个元素:
    选取随机数r属于(0,i-1)
    若r < k，则替换到a[r] = a[i]
"""
__author__ = 'guyu'
