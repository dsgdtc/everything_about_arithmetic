#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: quanpailie.py
Author: dsgdtc@163.com
Date: 2017/10/13 21:00
"""
import sys
import pprint
sys.setrecursionlimit(204800)


def reverse_string(x, _from, _to):
    """
    因为string是不可变的数据类型,所以实际操作时,将string转换为list执行
    """
    while (_from < _to):
        temp_letter = x[_from]
        x[_from] = x[_to]
        _from = _from + 1
        x[_to]= temp_letter
        _to = _to - 1

    # print (x)
    return x

def permutation(x, index):
    if index == 3:
        print (x)
    for i in range(index, len(x)):
        x[i], x[index] = x[index], x[i]
        permutation(x, index+1)
        x[i], x[index] = x[index], x[i]


def permutation2(x):
    """
    非递归的方式：
    步骤：后找，小大，交换，反转
    后找：从后向前找，找到第一个可以升序的地方，eg 21543,15是第一个升序的地方,1就是要找的字符

    小大：从S[i+1...N-1]中比S[i]大的最小值S[j]
    交换：交换S[i]和S[j]
    反转：对S[i+1...N-1]排序，实际就是反转
    :return:
    """
    i = len(x)
    # 后找
    while i > 0:
        i = i - 1
        if x[i] > x[i-1]:
            last_up = x[i]
            last_up_index = i
            # print ("从后向前找,字符串中最后的一个升序的位置:%s, 值为: %s" %(i, last_up))
            break
    # if (p < 0):
    #     return false

    # 小大
    waiting_switch = x[i-1]
    # print (p)
    for index in range(last_up_index, len(x)):
        if (x[index] >= x[i-1]):
            j = index
    # print ("找到待交换字符后中比waiting_switch大的最小值:%s, 索引位置: %s" %(x[j],j))

    # 交换
    x[i-1], x[j] = x[j], x[i-1]
    # print ("交换后的列表为:%s" %(x))

    # 翻转
    # print ("翻转后的列表为:")
    print (reverse_string(x, i ,len(x)-1))
    return x

if __name__ == '__main__':

    """
    给你个字符串，返回字符串可行的全排列  n!个
    全排列 permutation

    隐式图的深度优先搜索DFS
    """

    x = '21543'
    list_x = list(x)
    # list_x.sort()
    positive_squence_list_x = sorted(list_x)
    list_x.sort(reverse = True)
    reverse_list_x = list_x
    print ("原始字符串:%s" %(list(x)))
    print ("最小字符串:%s" %(positive_squence_list_x))
    print ("最大字符串:%s" %(reverse_list_x))
    print ("全排列如下:")
    print (positive_squence_list_x)
    # permutation(list_x, 0)
    while True:
        new_x = permutation2(positive_squence_list_x)
        if new_x == reverse_list_x:
            break

