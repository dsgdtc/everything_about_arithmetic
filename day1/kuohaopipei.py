#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: kuohaopipei.py
Author: dsgdtc@163.com
Date: 2017/9/11 20:10
"""
from queue import Queue

text_q = Queue(999)

def ismatch(left):
    if left == '(':
        return ')'

def match_parentheses(text):
    for i in text:
        if i == '(':
            text_q.put(i)
        else:
            if i == ')':
                if text_q.empty():
                    flag = 0
                    return flag
                expect_right = ismatch(text_q.get())
                if expect_right == i:
                    flag = 1
                else:
                    flag = 0
    if not text_q.empty():
        flag = 0
    return flag


if __name__ == '__main__':

    text = input("输入字符串,判断()是否匹配: ")
    status = match_parentheses(text)
    print (status)