#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: change_note找零钱.py
Author: dsgdtc@163.com
Date: 2018/2/6 20:57
给定某不超过100万的现金总额，兑换成数量不限的100,50,20,10,5,2,1元的纸币组合，公有多少种组合？

定义penny = { 2:2,5:5,10:10,20:20,50:50,100:100 }是可用的零钱
penny = [1,2,5,10,20,50,100]
定义dp[i][j]:使用面额小于等于penny[i]的钱币，凑成j元钱，共有多少种组合方法
dp[100][500] = dp[50][500]     +  dp[100][400]
               没用到100块钱      用到了100块钱，因为用到了，所以最少是用了1张，那么剩下的400块钱再用penny来凑

dp[i][j] = dp[i_small][j] + dp[i][j-penny[i]]   i_small是比i次小的面值

dp[i][j] = dp[i-1][j] + dp[i][j-penny[i]]        j >= penny[i]
         = dp[i-1][j]                            j <  penny[i]

初始条件
dp[0][j] = 1    i=0是表示最小面额的纸币,即1元
dp[i][0] = 1
利用滚动数组划掉第一维度得到：

dp[j] = last[j] + dp[j-penny[i]]   j >= penny[i]
      = dp[j]                      j <  penny[i]
"""

def solution(money, penny):

    size = len(penny)
    # dp[i][j] #用i面额以下组成j元
    dp = [[0 for j in range(money+1)] for i in range(size)]

    # dp[0][j] = 1 使用面额为penny[0]元(1元)以下的纸币组成j块钱的方法
    for j in range(money+1):
        dp[0][j] = 1

    # dp[i][0] = 1 使用任意面额纸币组成0块钱的方法
    for i in range(size):
        dp[i][0] = 1

    for i in range(1, size):  # penny[i]是纸币的面额
        for j in range(1, money+1):
            if j >= penny[i]:
                dp[i][j] = dp[i-1][j] + dp[i][j-penny[i]]
            else:
                dp[i][j] = dp[i-1][j]

    times = dp[size-1][money]
    return times


if __name__ == "__main__":
    money = 10
    # penny = { 1:1, 2:2,5:5,10:10,20:20,50:50,100:100 }
    penny = [1,2,5,10,20,50,100]
    res = solution(money, penny)
    print (res)