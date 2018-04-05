# -*- coding: utf-8 -*-

"""
如果想判断一个元素是不是在一个集合里，
一般想到的是将所有元素保存起来，然后通过比对来
判定是否在集合内：链表、树等数据结构都是这种思路
但是随着集合中元素数目的增加，我们需要的存储空间越来越大
检索的速度也越来越慢(O(n),0(logn))
可以利用bitmap:只要检查相应点是不是1就知道可以集合中有没有某个数

bloom filter算法介绍
有这个第三方库，python3没法用,python2可以用，爬虫里常用，判断url是否在集合里
"""
__author__ = 'guyu'
