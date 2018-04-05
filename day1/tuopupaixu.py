#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright (c) 2017 Baidu.com, Inc. All Rights Reserved
# 

"""有向无环图的拓扑排序
DAG
File: tuopupaixu.py
Author: dsgdtc@163.com
Date: 2017/9/10 18:10
"""

def topological_sort( graph ):

    is_visit = dict( ( node, False ) for node in graph )
    li = []

    def dfs( graph, start_node ):

        input()
        print ("dfs function,checking: ", start_node)
        for end_node in graph[start_node]:
            print ("end_node: %s" % (end_node))
            if not is_visit[end_node]:
                is_visit[end_node] = True
                print ( graph, end_node)
                dfs( graph, end_node )
        li.append( start_node )

    for start_node in graph:
        print ("main loop")
        print (li)
        print ("Checking: ", start_node)
        print (is_visit)

        if not is_visit[start_node]:
            is_visit[start_node] = True
            dfs( graph, start_node )

    li.reverse()
    return li


if __name__ == '__main__':
    graph = {
        'v1': ['v5'],
        'v2': ['v1'],
        'v3': ['v1', 'v5'],
        'v4': ['v2', 'v5'],
        'v5': [],
    }
    li = topological_sort( graph )
    print (li)
