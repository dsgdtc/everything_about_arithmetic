#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: nixushu逆序数.py
Author: dsgdtc@163.com
Date: 2018/1/4 17:07
设A[1..n]是一个包含n个不同数的数组。
如果在i<j的情况下，有A[i]>A[j]，则(i, j)就称为A中的一个逆序对（inversion）
一个列表中逆序对的数量叫逆序数。
算法：
算法实现类似于合并排序，但需要额外处理逆序数的计数。
因此，逆序数的计算相当于合并排序的副产品。
在下面的代码中将global num num = num + 1 去掉就是基本的归并排序。
T(n) = 2T(n/2)+n,因此算法时间复杂度为O(nlog(n)).
"""

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            global num
            # right[j]和left[i]后边的元素组逆序对
            num += len(left) - i
            result.append(right[j])
            j += 1
    # print ('result is:%s' %(result))
    result += left[i:]
    result += right[j:]
    # print ('after result is:%s' %(result))
    return result


def merge_sort(lists):

    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)

# def  merge(lst1, lst2):
#     """to Merge two list together"""
#     list = []
#     while(len(lst1)>0 and len(lst2)>0):
#         data1 = lst1[0]
#         data2 = lst2[0]
#         if (data1<=data2):
#             list.append(lst1.pop(0))
#         else:
#             global num
#             num = num + 1
#             list.append(lst2.pop(0))
#
#     if(len(lst1)>0):
#         list.extend(lst1)
#     else:
#         list.extend(lst2)
#     return list

num = 0
arr = [2, 1, 4, 3]
# arr = [3, 56, 2, 7]
print(merge_sort(arr))
print(num)