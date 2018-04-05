#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""给定一个链表和一个值X，将链表划分成两个部分，小于X的节点在前，大于X后的节点在后，这两部分中要保持原链表中的出现顺序.快排
File: lianbiaohuafen.py
Author: dsgdtc@163.com
Date: 2017/9/5 20:34
"""

import random

def divice(li):

    # divice_li = []
    length = len(li)
    device_top_half = []
    device_back_half = []
    # for i in range(length):
    #     print (li)
    #     print (i,li[i])
    #     input()
    #     if li[i] <= x:
    #         device_top_half.append(li[i])
    #     else:
    #         device_back_half.append(li[i])

    device_top_half = [i for i in li if i <= x]
    device_back_half = [i for i in li if i > x]
    device_top_half.extend(device_back_half)

    return device_top_half

    return  unique_li

if __name__ == '__main__':
    li = [2,3,6,3,8,3,7,9,4,3]
    x = 6
    print ("Origin li: %s" % (li))
    print ("划分用的x值为: %s" % (x))
    unique_li = divice(li)
    print ("divice li: %s" % (unique_li))


