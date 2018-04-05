#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: hannuota.py
Author: dsgdtc@163.com
Date: 2017/10/24 20:30
hanoi塔（越南首都河内）
"""

# 汉诺塔的状态
def



def MoveOne(_from, _to):
    print (_from, "-->", _to)

def Move(_from, _to, _aux, n):
    if (n == 1):
        MoveOne(_from, _to)
        return

    else:
        Move(_from, _aux, _to, n-1)
        MoveOne(_from, _to)
        Move(_aux, _to, _from, n-1)

if __name__ == '__main__':

    n = 3 
    Move('A', 'C', 'B', n)