#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: aco蚁群算法.py
Author: dsgdtc@163.com
Date: 2018/2/12 11:03
核心：路径中的信息素以一定的比例挥发减少，而某蚂蚁经过的路径，信息素以一定的比例释放
算法：m只蚂蚁，最大迭代次数K
    信息素的初始化
    路径构建
    信息素更新
    2,3步骤迭代K次或最短路径不再变化

"""