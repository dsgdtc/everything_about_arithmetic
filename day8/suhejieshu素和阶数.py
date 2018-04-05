# -*- coding: utf-8 -*-
__author__ = 'guyu'
"""
一个正整数可以被拆分成两个素数和的数目为"素和阶数"。计算100万以内哪个数的素和阶数最大
思路：
先把100万以内的素数都找出来存入p
从1-100万遍历i：
    查找p中大于等于i的最小值，
"""

def eratosthenes(n):

    x = [True for i in range(0, n)]  # initiates the array of flags
    x[0] = False  # 0 is not a prime number
    x[1] = False  # 1 is not a prime number too
    p = []
    for i in range(2, n):
        if (x[i]):
            y = i * 2
    # For every y multiples of i, y is not a prime number
            while y < n:
                x[y] = False
                y += i

            p.append(i)
    return p
def two_sum(a, size, Sum):
    i= 0
    j = size -1
    count = 0
    while i < j:
        if a[i] + a[j] < Sum:
            i += 1
        elif a[i] + a[j] > Sum:
            j -= 1
        else:
            i += 1
            j -= 1
            count += 1
            # print ("%s + %s = %s" %(a[i], a[j], Sum))

    return count


def cal_suhejieshu(prime_number, END):

    index = 0
    for s in range(END):
        for p in prime_number:
            # 遍历100万，在素数集合中找到大于i的最小的那个质数值的位置
            if p > s:
                index = prime_number.index(p)
                break
        # 在prime_num[0: index]中，两头扫，找到和为s的各种质数的组合
        using_prime_number = prime_number[0:index]
        size = len(using_prime_number)
        count = two_sum(using_prime_number, size, s)
        print ("%s的素和阶数为%s" %(s, count))
        input("etc...")


if __name__ == '__main__':
    END = 100 * 100000
    prime_number = eratosthenes(END)
    cal_suhejieshu(prime_number, END)