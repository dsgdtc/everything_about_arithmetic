#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: 进制推断.py
Author: dsgdtc@163.com
Date: 2017/12/17 20:09
如果84 * 148 = B6A8成立，则该公式采用的是 ？ 进制的
"""
按照定义做:
(8*x + 4) * (x^2 + 4*x + 8) = 11*x^3 + 6*x^2 + 10*x + 8

4*8 = 32, 32-8 = 24,