# -*- coding: utf-8 -*-
"""
输入3个字符串S1，S2和S3，判断第三个字符串S3是否由前两个字符串
S1和s2交错而成，即不改变s1和s2中各个字符原有的相对顺序
eg:当s1="aabcc", s2="dbbca"，s3="aadbbcbcac时"输出true
但如果s3="accabdbbca",则输出false
换个表述：
    s1和s2是s3的子序列，且 s1 并 s2 = s3

算法:
    动态规划解决：
    为了方便，从1开始数
    令dp[i][j]表示s3[1..i+j]是否由s1[1..i]和s2[1..j]的字符组成
    即dp[i][j]取值范围为true/false
    先判定最后一个元素
    如果s3的最后一个元素来自s1:
        s1[i] == s3[i+j]且dp[i-1][j]为真，则dp[i][j]为真
    或者s3的最后一个元素来自s2:
        s1[j] == s3[i+j]且dp[i][j-1]为真，则dp[i][j]为真
    其他情况，dp[i][j]为假

    可以用滚动数组降低空间复杂度
"""
__author__ = 'guyu'

def is_interlace(str1, str2, str):

    M = len(str1)
    N = len(str2)
    S = len(str)
    if (M+N) != S:
        return False
    p = [[False for j in range(N+1)] for i in range(M+1)]
    p[0][0] = True

    for i in range(1, M+1):
        p[i][0] = (p[i-1][0]) & (str1[i-1] == str[i-1])

    for j in range(1, N + 1):
        p[0][j] = (p[0][j-1]) & (str2[j - 1] == str[j - 1])

    for i in range(1, M+1):
        for j in range(1, N+1):
            p[i][j] = (p[i-1][j] & (str[i+j-1] == str[i-1]))
            | (p[i][j-1] & (str[i+j-1] == str[j-1]))

    return p[M][N]

if __name__ == "__main__":
    str1 = list("aabcc")
    str2 = list("dbbca")
    str = list("aadbbcbcac")
    result = is_interlace(str1, str2, str)