# -*- coding: utf-8 -*-
# __author__ = 'guyu'
"""
File: hundred百数问题.py
Author: dsgdtc@163.com
Date: 2017/11/13 20:23
暴力求解
1,2,3,4,5,6,7,8,9 在中间插入+-null，最后得100
8个空，每个空3中方法，一共3**8可能性

"""
from functools import reduce
operator = {
    0: "",
    1: "+",
    2: "-",
}

def ishandred(l, size, num):

    # 将num转换为3进制数,得到运算符数组
    ternary_list = []
    slot = size - 1
    org_num = num
    # print ("换算 %s 变成一个8位的3进制数" %(num))
    for index in range(slot, 0, -1):
        # 把num换算成一个8位的3进制数
        index = index - 1
        value = num // 3**index
        ternary_list.append(value)
        # print ("第%s位是%s" %(index, value))
        num = num - (value * 3**index)
    # print("%s的换算结果为:%s" %(org_num, ternary_list))
    # 换成符号
    ternary_list = map(lambda x: operator[x], ternary_list)
    ternary_list = list(ternary_list)
    # print (list(ternary_list))
    # print (l, type(l))
    connect_l_and_ternary_list = zip(l, list(ternary_list))
    connect_l_and_ternary_list = list(connect_l_and_ternary_list)
    # print ("把l和ternary_list拼接起来:%s" %(connect_l_and_ternary_list))
    express = reduce(lambda x,y:x+y, connect_l_and_ternary_list)
    express = list(express)
    express.append(l[-1])
    express = "".join(express)

    result = eval(express)
    return result, express

def calculate(l, size):

    # opration = [(0, 0)] * (size - 1)
    total = 3 ** (size - 1)

    for num in range(total):
        result, express = ishandred(l, size, num)
        if result == 100:
            print (express)


if __name__ == '__main__':

    l = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    size = len(l)
    print("一共%s个数,%s个空" % (size, size-1))
    calculate(l, size)