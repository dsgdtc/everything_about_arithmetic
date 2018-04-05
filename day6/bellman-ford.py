# -*- coding: utf-8 -*-
# __author__ = 'guyu'





"""
bellman-ford算法，解决带负权值的最短路径问题
本质：动态规划
适用：单源节点到其他所有节点的最短路径
若u-->v是有向边源点记为o，则d[v] <= d[u] + dis(u,v)
这个操作被称为松弛操作
优点：对边权无要求，可以发现负环
SPFA，对bellman-ford的改进
"""


