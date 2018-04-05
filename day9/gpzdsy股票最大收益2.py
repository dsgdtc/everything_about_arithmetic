# -*- coding: utf-8 -*-
"""
给定数组A，其中A[i]表示某股票第i天的价格。
如果允许最多进行K次交易(K是已经给定的定值)，
请计算何时买卖达到最大收益，返回最大收益值。
规定 不能嵌套买卖  Z只能是买卖-买卖-买卖......
eg
[7,1,5,3,6,4]最大收益值为5-1=4,6-3=3，4+3 = 7

算法：
dp[k][i] 表示最多k次交易在第i天的最大收益
在第i天，有两种选择，要么卖出股票，要么不卖出股票，从而得到最大收益
dp[k][i] = max { dp[k][i-1] 不卖出 }
              { dp[k-1][j] + prices[i] - prices[j] , j属于[0,i-1] }
"""
__author__ = 'guyu'

def max_profit(A, size, K):

    # dp[k][i] 表示最多K次交易在第i天的最大收益
    # +1是为了好数数
    dp = [[0 for col in range(size+1)] for row in range(K+1)]
    profit = 0
    price = A
    price.insert(0, None) #首位占个空位置,为了方便天从第1天开始数
    for k in range(1, K+1):
        for i in range(1, size+1):

            dp[k][i] = dp[k][i - 1] # 第i天不卖出时的价格
            for j in range(1, i+1):
                # print (dp[k][i-1])
                # print (dp[k-1][j]+(price[i] - price[j]))

                dp[k][i] = max(dp[k][i], dp[k-1][j]+(price[i] - price[j]) )
                # print ("dp[%s][%s]设置为%s" %(k,i, dp[k][i]))
                # print ("What is dp:%s" %(dp))
                # input("etc...")


    # print (dp)
    # print (dp[K])
    return dp[K][size-1]

    return profit

if __name__ == "__main__":
    A= [7,1,5,3,6,4]
    size = len(A)
    K = 3
    result = max_profit(A, size, K)
    print (result)