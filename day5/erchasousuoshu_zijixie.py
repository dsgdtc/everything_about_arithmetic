#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: bst.py
Author: dsgdtc@163.com
Date: 2017/10/30 21:05
左子树上的所有节点值均小于根节点值，
右子树上的所有节点值均不小于根节点值，
左右子树也满足上述两个条件
凸包算法是什么
"""

# encoding: utf-8
class TreeNode(object):
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BST(object):

    def __init__(self, node_list):
        self.root = TreeNode(node_list[0])
        for data in node_list[1:]:
            self.insert(data)

    def insert(self, root, data):
        if root is None:
            root = TreeNode(data)
        else:
            if data < root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root

    def search(self, root, data):
        if root is None:
            return None
        if root.data == data:
            return 1
        if root.data <= data:
            return self.search(root.right, data)
        else:
            return self.search(root.left, data)



if __name__ == "__main__":

    # 二叉搜索树数据,a[0]为根
    a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
    bst = BST(a)  # 创建二叉查找树


