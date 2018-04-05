#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""
File: singlelinkedlist.py
Author: dsgdtc@163.com
Date: 2017/9/5 20:34
"""

import random

class Node(object):

    def __init__(self, val, p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key < 0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            return self.getitem(key)
    # def __repr__(self):
    #     '''
    #     用来定义Node的字符输出，
    #     print为输出data
    #     '''
    #     return str(self._item)



    def __setitem__(self, key, value):

        if self.is_empty():
            print ('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):

        self.head = Node(data[0])
        current_p = self.head
        # print (data[0])
        # print(self.head, self.head.data, current_p)
        # input()
        for i in data[1:]:
            node = Node(i)
            current_p.next = node
            current_p = current_p.next
            # print(node, node.data, current_p, current_p.next)
            # input()

    def getlength(self):
        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):
        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):
        self.head = 0


    def append(self,item):

        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getitem(self,index):

        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data
        else:
            print ('target is not exist!')

    def insert(self, index, item):

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p


    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next

    def index(self,value):

        if self.is_empty():
            print ('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


def reverse(linked_list, reverse_from, reverse_to):
    # linked_list.getitem(4)
    p_current = linked_list.head
    p_current = p_current.next
    for i in (range(reverse_from-1, reverse_to+1)):
        print (linked_list.getitem(i))

    print ('-'*50)

def touchafa_list():
    count = 50
    nums = []
    for i in range(count):
        nums.insert(5, i)
    print (nums)

def touchafa_reverse_list(lst, reverse_from, reverse_to):

    part_reverse_lst = []
    reverse_from = reverse_from - 1
    for i in range(len(lst)):
        if reverse_from < i <reverse_to:
            part_reverse_lst.insert(reverse_from, lst[i])
        else:
            part_reverse_lst.append(lst[i])
    print (part_reverse_lst)


def test_touchafa_list():
    test_list = [i+ random.randint(2, 100) for i in range(10)]
    print ("Origin linked_list: ", test_list)
    _from = 4
    _to = 8
    print ("reverse from %s to %s" %(_from, _to) )
    touchafa_reverse_list(test_list, 4, 8)

if __name__ == '__main__':
    l = LinkList()
    l.initlist([1,2,3,4,5,6,7])
    li = []
    for i in range(0, l.getlength()):
        li.append(l.getitem(i))

    # print ("Origin linked_list: ", li)
    # touchafa_list()
    # reverse(l, 2, 5)

    test_touchafa_list()




