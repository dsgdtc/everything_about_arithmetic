# -*- coding: utf-8 -*-
"""
本福特定律，也叫第一数字定律
100!里，首数字是1的概率
没装桌面环境，在jupyter上画图
100！：[30, 18, 13, 7, 7, 7, 3, 10, 4]
1000！：[293, 176, 124, 101, 69, 87, 51, 51, 47]
"""

__author__ = 'guyu'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def first_digital(x):

    while x>= 10:
        x //= 10
    return x

if __name__ == "__main__":

    n = 1
    frequency = [0] * 9
    for i in range(1, 100):
        n *= i
        m = first_digital(n) - 1
        frequency[m] += 1
    print (frequency)
    plt.plot(frequency, 'r-', linewidth=2)
    plt.plot(frequency, 'go', markersize=8)
    plt.grid(True)
    plt.show()

