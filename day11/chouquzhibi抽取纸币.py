# -*- coding: utf-8 -*-
"""
现在又一叠纸币，5元面值的6张，10元的5张，20元的4张，从中任意取出4张纸币
则每种面值至少取一张的概率是多少？
"""
__author__ = 'guyu'
from scipy.special import comb, perm
if __name__ == "__main__":

    总事件：C(15,4)
    至少一张: C(6,2) * c(5,1) * c(4,1) +
                C(6, 1) * c(5, 2) * c(4, 1) +
                C(6, 1) * c(5, 1) * c(4, 2) +
