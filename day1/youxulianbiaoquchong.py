#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""有序链表去重
File: youxulianbiaoquchong.py
Author: dsgdtc@163.com
Date: 2017/9/5 20:34
"""

import random

def unique(li):

    unique_li = []
    for i in range(len(li)):
        if i+1 == len(li):
        # if i+1 == len(li) or i==0: # 如果发现重复则全部删掉
            unique_li.append(li[i])
        else:
            if li[i] == li[i+1]:
            # if li[i] == li[i+1] or li[i-1] == li[i]:
                print ("Do not need %s" %(li[i]))
            else:
                unique_li.append(li[i])

    return  unique_li

if __name__ == '__main__':
    li = [2,3,5,5,5,7,8,8,8,9]
    print ("Origin li: %s" % (li))
    unique_li = unique(li)
    print ("Unique li: %s" % (unique_li))


