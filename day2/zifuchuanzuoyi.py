#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: zifuchuanzuoyi.py
Author: dsgdtc@163.com
Date: 2017/10/5 23:13
"""

# 时间复杂度O(n), 空间复杂度O(k)
def zuoyi(x, index):
    # print (x)
    list_x = x
    # print (list_x)
    left_x = list_x[:index]
    right_x = list_x[index:]
    print (left_x,right_x)
    new_x = right_x + left_x
    print (new_x)
    new_x = "".join(new_x)
    return new_x

# 时间复杂度O(k), 空间复杂度O(1)
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
def zuoyi2(x, index):
    """该问题会在完美洗牌算法中再次遇到。
    时间复杂度是O(n),空间复杂度为O(1)
    问题：python字符串切片的空间复杂度是多少
    (X'Y')' = YX用向量转秩
    eg:
    i love c++  -->> c++ love i
    X = ab  X' = ba
    Y = cdef Y' = fedc
    (X'Y')' = (bafedc)' = cdefab
    :param x:
    :param index:
    :return:
    """
    index_end = len(x) - 1
    index = index
    new_x = reverse_string(x, 0, index)
    new_x = reverse_string(new_x, index+1, index_end)
    new_x = reverse_string(new_x, 0, index_end)
    new_x = "".join(new_x)
    return new_x



if __name__ == '__main__':
    x = input("请输入字符串:")
    list_x = list(x)
    # print ("原始字符串为:%s" %(x))
    index = 2
    index = index - 1
    new_x = zuoyi2(list_x, index)
    print ("左移%s位后的字符串为:%s" %(index+1, new_x))
