# -*- coding: utf-8 -*-
"""
根据5的余数把数字们分成5份
X=5N    整除的肯定能用5克砝码凑出来,X=5
X=5N+1  余数是1的，需要把若干个5克砝码换成7g砝码，并且7a-5b=1
            穷举的a=3,b=4,所以之前至少要有4个5g砝码，X=21
X=5N+2  余数是2的，需要把若干个5克砝码换成7克砝码，并且7a-5b=2
            穷举得a=1,b=1,所以至少有1个5克砝码，X=7
X=5N+3  同理7a-5b=3得 a=4,b=5，X=28
X=5N+4  7a-5b=4得  a=2,b=2,X=14
把可行的数字列在数轴上，最大的不可行数字是23

"""
__author__ = 'guyu'
