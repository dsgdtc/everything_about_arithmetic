#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: young_tableau.py
Author: dsgdtc@163.com
Date: 2018/1/4 17:27
杨氏矩阵
在一个二维数组中，每行都是有序的，每列都是有序的。
特殊：从左到右递增排序，从上到下递增排序
请完成一个函数，输入这样的一个数组和一个数，判断数组中是否包含这个数。
主要看查找。
"""
# from numpy import *
import numpy as np

def young_insert(m, value, i, j):
    m[i][j] = value
    largesti = i
    largestj = j

    if i-1>=0 and (np.isnan(m[i-1][j]) or m[i-1][j] > m[i][j]):
        largesti = i-1
        largestj = j
    if j-1>=0 and (np.isnan(m[i][j-1]) or m[i][j-1] > m[largesti][largestj]):
        largesti = i
        largestj = j - 1
    if i!=largesti or j!=largestj:
        temp = m[i][j]
        m[i][j] = m[largesti][largestj]
        m[largesti][largestj] = m[i][j]
        young_insert(m,value,largesti,largestj)

def young_delete(m, i, j):
    m[i][j] = np.NAN
    mini = i
    minj = j
    if i+1<m.shape[0]:
        mini = i+1
        minj = j
    if j+1<m.shape[1] and (np.isnan(m[mini][minj]) or m[i][j+1] < m[mini][minj]):
        mini = i
        minj = j+1

    if mini!=i or minj!=j:
        temp = m[i][j]
        m[i][j] = m[mini][minj]
        m[mini][minj] = temp
        young_delete(m, mini, minj)

def young_find(m, value):

    # 从右上角开始找
    i = 0
    j = m.shape[1] - 1
    while i<m.shape[0] and j >=0:

        if m[i][j] == value:
            return True
        elif np.isnan(m[i][j]) or m[i][j] > value:
            # 如果value比矩阵位置上的值小，那么向左走
            j = j -1
        elif np.isnan(value) or m[i][j] < value:
            # 如果比矩阵位置上的值大，那么向下走
            i = i+ 1
    return False

def young_modify(m, i, j, value):
    m[i][j] = value
    nexti = i
    nextj = j
    if i-1>=0 and m[i-1][j] > m[i][j]:
        nexti = i-1
        nextj = j
    if j-1>=0 and m[i][j-1] > m[nexti][nextj]:
        nexti = i
        nextj = j-1

    if i+1<m.shape[0] and m[i][j] > m[i+1][j]:
        nexti = i+1
        nextj = j
    if j+1<m.shape[1] and( np.isnan(m[nexti][nextj]) or m[i][j+1] < m[nexti][nextj]):
        nexti = i
        nextj = j+1

    if nexti!=i or nextj!=j:
        temp = m[i][j]
        m[i][j] = m[nexti][nextj]
        m[nexti][nextj] = temp
        young_modify(m, nexti, nextj, value)

if __name__ == '__main__':
    m = np.array([[2,4,6,np.NAN],
               [3,7,10,np.NAN],
               [5,12,np.NAN,np.NAN],
               [8,np.NAN,np.NAN,np.NAN]])
    hight, width = m.shape
    print ('matrix is:')
    print (m)
    print ('-'* 24)
    print ('after insert 7')
    young_insert(m, 7, hight-1, width-1)
    print (m)
    print ('-'*24)
    print ('after delete m[0][0]')
    young_delete(m,0,0)
    print (m)
    print ('-'*24)
    print ('if 12 in the matrix')
    print (young_find(m,12))
    print ('-'*24)
    print ('after update m[1][1] to 1')
    young_modify(m, 1, 1,1)
    print (m)
