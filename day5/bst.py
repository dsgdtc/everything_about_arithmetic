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
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST(object):
    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for data in node_list[1:]:
            # self.insert(data)
            self.insert2(self.root, data)

    # 搜索
    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    # 插入
    def insert(self, data):
        flag, n, p = self.search(self.root, self.root, data)
        if not flag:
            new_node = Node(data)
            if data > p.data:
                p.rchild = new_node
            else:
                p.lchild = new_node

    # 更容易理解的插入方法
    def insert2(self, root, data):

        if root is None:
            root = Node(data)
        else:
            if data < root.data:
                # print ("data < root.data,往左节点插入数据")
                root.lchild = self.insert2(root.lchild, data)
            else:
                # print("data > root.data,往右节点插入数据")
                root.rchild = self.insert2(root.rchild, data)
        return root


    # 删除
    def delete(self, root, data):
        """
        若删除的元素刚好是叶子节点，就直接删除元素，然后把该结点用None来代替。
        若删除的元素只有一个孩子节点，那么就把这个节点删除再将其孩子节点变成现在的节点。
        若删除的元素有两个孩子，那么需要判断的情况就稍微复杂一点，需要从该元素的右孩子树中找到一个合适的元素（称为后继）来代替该元素，
        原来的右子树变为当前更新元素的右子树。
        :param root:
        :param data:
        :return:
        """
        flag, n, p = self.search(root, root, data)
        if flag is False:
            print ("无该关键字，删除失败")
        else:
            print (flag, n.data, p.data)
            input("running here")
            if n.lchild is None:
                if n == p.lchild:
                    print(n, p.lchild)
                    print(n.data, p.lchild.data)
                    input("here")
                    p.lchild = n.rchild
                else:
                    print(n, p.rchild)
                    print(n.data, p.rchild.data)
                    p.rchild = n.rchild
                    print ("self.root: ",self.root, self.root.data)
                    print (p, p.data, p.lchild.data, p.rchild.data)
                    input("here")
                # 这句话有什么用？为什么不del n
                # del p
                del n
                print("self.root: ", self.root, self.root.data)
                print("n: ", n, n.data)

                # print(p, p.data)
                # input("here")

            elif n.rchild is None:
                if n == p.lchild:
                    p.lchild = n.lchild
                else:
                    print(n, p.rchild)
                    print(n.data, p.rchild.data)
                    input("here")
                    p.rchild = n.lchild
                del n
            else:  # 左右子树均不为空
                """
                方法一：
                将p的直接后继的值拷贝到p处
                删除p的直接后继
                下面不是这个方法,和老师讲的方法不同，但写起来简单
                """
                pre = n.rchild
                if pre.lchild is None:
                    n.data = pre.data
                    n.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.data = next.data
                    pre.lchild = next.rchild
                    del n


    # 先序遍历
    def preOrderTraverse(self, node):
        if node is not None:
            print (node.data)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    # 中序遍历
    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print (node.data)
            self.inOrderTraverse(node.rchild)

    # 后序遍历
    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print (node.data)

a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
b = [15,3,5,12,10,6,7,13,16,20,18,23]
bst = BST(b)  # 创建二叉查找树
print ("中序遍历:")
bst.inOrderTraverse(bst.root)  # 中序遍历

x=16
print ("删除%s" %(x))
bst.delete(bst.root, x)
print (bst.inOrderTraverse(bst.root))
