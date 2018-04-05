#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
#

"""
给定若干个单词组成的词典words,
找到词典中的所有单词对(i,j),使得words[i] + words[j]是回文串

算法:
    str1比str2短:
        str1和str2的后半段能组成回文串，并且str2是回文的
    str1比str2长:
        反之

    还是用trie树，所有词逆序存在trie树种

算法2：
    一个str总能分成<left-right>,若left是回文的，将right翻转得到T，且T在字典中，那么[T, left, right]是回文的
                                若right是回文的，将left翻转得到T，且T在字典中，那么[left, right, T]是回文的

    若str是回文串，且str的翻转串T也在字典中，则[T, str]构成回文串

"""



