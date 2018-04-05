# -*- coding: utf-8 -*-
"""
给定m*n的矩阵，每个位置是一个非负整数，左上角有个机器人
每次只能向右向下走，直到右下角，求所有路径中，总和最小的那条路径
问最短长度是多少

做GIS有用

方法1：动态规划
算法:
    用dp[x][y] 表示从左上到当前点的最短路径的长度,那么
    dp[0][0] = chess[0][0] 自己到自己
    dp[x,0] = dp[0][0] + dp[1][0] + dp[2][0] + ... + dp[x][0] 当y==0时,也就是最左边的一列的最短路径
    dp[0,y] = dp[0][0] + dp[0][1] + dp[0][2] + ... + dp[0][y] 当x==0时,也就是最上边的一列的最短路径
    dp[x][y] = min(  dp[x-1][y] + chess[x][y],   dp[x][y-1] + chess[x][y])  到x,y的最短路径要么从上面过来，要么从左边过来
    即: dp[x][y] = min( dp[x-1][y],  dp[x][y-1]) + chess[x][y]

    如果不需要最短路径本身,每个x,y的状态之和其相邻的左面一个值和上面一个值的状态有关,而dp[x][y]却存储了所有的状态显然是浪费了
    滚动数组:
    dp[j] = dp[0][0] + dp[0][1] + dp[0][2] + ... + dp[0][y]  这个要先算好,当做缓冲区
    dp[j] = min(  dp[j](这个是缓冲区,表示i,j正上方那个值的大小), dp[j-1] + chess[i][j])


扩展:
重新定义dp[x][y]
若令dp[x][y]为当前位于(x,y)时有多少种可行的路径，那么dp[x][y] = 左边的条数dp[x-1][y] + 上边格子的条数dp[x][y-1]
不知道怎么的，就推出了下边的公式
dp(x+y, x, y) = dp(x+y-1, x-1, y) + dp(x+y-1, x, y-1)
看课件P49最后推出组合式公式
c(m,n) = m!/((m-n)! * n!)
C(m,n) = C(n-1, m-1) + C(n-1, m)    用纸写，把C(m,n)全都展开计算可得此结论


"""
__author__ = 'guyu'

import random
import pprint

def min_path(chess, M, N):

    path_length = [0] * N
    path_length[0] = chess[0][0]
    for j in range(1, N):
        path_length[j] = path_length[j-1] + chess[0][j]

    for i in range(1, M):
        path_length[0] = path_length[0] + chess[1][0]
        for j in range(1, N):
            if path_length[j-1] < path_length[j]:
                path_length[j] = path_length[j-1] + chess[i][j]
            else:
                path_length[j] += chess[i][j]


    return path_length[N-1]

if __name__ == "__main__":

    M = 10
    N = 8
    random.seed(1)
    chess = [[random.randint(1,100) for j in range(N)] for i in range(10)]
    print("原始棋盘是:")
    pprint.pprint (chess)
    result = min_path(chess, M, N)

    print ("从左上到右下的最短路径长度为:%s" %(result))
