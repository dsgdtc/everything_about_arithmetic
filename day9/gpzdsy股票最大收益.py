# -*- coding: utf-8 -*-
"""
给定数组A，其中A[i]表示某股票第i天的价格。如果允许最多进行一次交易(先买一次，再卖一次)，请计算何时买卖达到
最大收益，返回最大收益值
eg[7,1,5,3,6,4]最大收益值为6-1=5
一路下跌，最好的方法是不交易
算法：
profit = max(profit, A[i] - min(A[0...i-1]))
"""
__author__ = 'guyu'

def max_profit(A, size):

    profit = 0
    mn = A[0]  # 表示前边0--i-1的最小值
    for i in range(size):
        mn = min(mn, A[i-1])
        profit = max(profit, A[i] - mn)
    return profit

if __name__ == "__main__":
    A= [7,1,5,3,6,4]
    size = len(A)
    result = max_profit(A, size)
    print (result)