# -*- coding: utf-8 -*-

"""
__author__ = 'guyu'
一只老鼠在迷宫的0,0处，在5,5位置有块奶酪，1表示连通，0表示墙，寻找一条路径，让老鼠吃到奶酪
[['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
 ['1', '1', '0', '1', '1', '1', '0', '1', '1', '1'],
 ['1', '1', '0', '0', '0', '0', '1', '0', '1', '1'],
 ['1', '0', '1', '1', '1', '1', '1', '1', '0', '1'],
 ['1', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
 ['0', '1', '1', '1', '1', '9', '1', '1', '1', '1'],
 ['1', '1', '0', '1', '1', '1', '1', '1', '0', '1'],
 ['0', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
 ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1'],
 ['1', '1', '0', '1', '1', '1', '1', '1', '1', '0']]
迷宫四连通
"""
import random
import pprint


class Solution(object):

    def __init__(self, graph, M, N):
        self.graph = graph
        self.M = M
        self.N = N
        # self.q = []
        self.graph_visited = [[False for j in range(self.N)] for i in range(self.M)]
        self.path = []
    def find_mouse_path(self):

        def dfs(x, y):
            if self.graph[x][y] == 9:
                print(self.path)
                return True
            i_direct = [-1, 1, 0, 0]
            j_direct = [0, 0, -1, 1]

            for step in range(4):
                # print (x, y)

                x_current = x + i_direct[step]
                y_current = y + j_direct[step]
                print(x, y, "-->", x_current, y_current)
                print(self.path)
                if x_current < 0 or x_current > self.M-1 or y_current < 0 or y_current> self.N-1:
                    print("出界了")
                    input("etc...")
                    continue
                if (self.graph_visited[x_current][y_current] is False) and (self.graph[x_current][y_current] !=0):
                    # 如果此点没有被访问过，并且等于1，可以连通
                    print ("没出界并且此节点为1,没被访问过")
                    input("etc...")
                    self.graph_visited[x_current][y_current] = True
                    self.path.append((x_current, y_current))

                    if (dfs(x_current, y_current)):
                        # 如果找一条，return True,如果找多条，把path放到all_path中
                        return True

                    self.path.pop()
                    self.graph_visited[x_current][y_current] = False
                else:
                    print("此节点被访问过或者值为0:%s %s" %(self.graph_visited[x_current][y_current],
                                                 self.graph[x_current][y_current]))
                    input("etc...")
            return False

        if len(self.graph) == 0:
            return False

        if self.graph[0][0] == 0:
            return False

        self.path.append((0,0))
        self.graph_visited[0][0] = True
        dfs(0, 0)

if __name__ == "__main__":
    M = 5
    N = 5
    graph = [[1 for j in range(N)] for i in range(M)]
    random.seed(1)
    for i in range(M):
        for j in range(N):
            if random.randint(1, 10) % 5 == 1:
                graph[i][j] = 0
    print ("Origin graph is:")
    graph[2][2] = 9
    pprint.pprint (graph)
    s = Solution(graph, M, N)
    graph_solved = s.find_mouse_path()
    print (s.path)
