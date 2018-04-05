#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: largest_bst_subtree.py
Author: dsgdtc@163.com
Date: 2017/11/6 19:53
给定某二叉树，找出最大二叉搜索子树，并返回其根节点

"""

class Node():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None



if __name__ == '__main__':

    l = [1,-2,3,10,-4,7,2,-5]
    size = len(l)
    print ("Origin list: %s, size is:%s" %(l,size))
    bst = BST(l)
    bst.inOrderTraverse(bst.root)  #中序遍历
    bst.preOrderTraverse(bst.root)  #前序遍历

    bst.largest_sub_tree
