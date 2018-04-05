# -*- coding: utf-8 -*-

"""
给定非负整数组，初始时在起始位置放置一个机器人，
数组的每个元素表示在当前位置机器人最大能够跳跃的数目。
它的目的是用最少的步数到达末端。
例如给定数组A=[2,3,1,1,2]，最少跳步数是2，对应跳法是
2-->3-->2
算法：
    初始步数step赋值为0
    记当前步的控制范围是[i,j]，则用k遍历i到j
        计算A[k] + k的最大值，记做j2
    step ++，继续遍历[j+1,j2]

"""
__author__ = 'guyu'

def jump(A, size):
    step = 0
    i = 0
    j = 0 # [i,j]表示当前能覆盖的区间
    if size == 1:
        return 0

    while (j < size):
        step +=1:
        j2 = j
        for k in range(i, j):
            j2 = max(j2, A[k] + k)
            if (j2 >= n-1):
                # 跳到末尾
                return step
        i = j+1
        j = j2
        if (j<i):
            # 无法跳到末尾
            return -1
    return step

if __name__ == "__main__":
    A = [2,3,1,1,2,4,1,1,6,1,7]
    size = len(A)
    res = jump(A, size)
