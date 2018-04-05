# -*- coding: utf-8 -*-
"""
__author__ = 'guyu'
计数排序的核心思想是用空间换时间，本质是建立了基于元素的Hash
计数排序的优势是突破了基于比较的排序的时间复杂度理论上的下限O(nlog(n))，复杂度是O(n+k)

"""


def sort(a):
    n = len(a)
    b = [None] * n
    for i in range(n):
        p = 0
        q = 0
        for j in range(n):
            if a[j] < a[i]:
                p += 1
            elif a[j] == a[i]:
                q += 1
        for k in range(p, p + q):
            b[k] = a[i]
    print (b)

