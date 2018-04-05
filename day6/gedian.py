# -*- coding: utf-8 -*-
__author__ = 'guyu'
from collections import defaultdict

#This class represents an undirected graph
#using adjacency list representation
class Graph:

    # 用邻接表表示的图,不是矩阵，邹博代码里好像是用的矩阵
    def __init__(self, vertices):
        self.V = vertices #No. of vertices
        """
        self.graph2 = {
          0: [],
          1: []
        }
        """
        self.graph2 = { i: [] for i in range(vertices) }
        # self.graph = defaultdict(list) # default dictionary to store graph
        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph2[u].append(v)
        self.graph2[v].append(u)

    '''A recursive function that find articulation points
    using DFS traversal
    u --> The vertex to be visited next
    visited[] --> keeps tract of visited vertices
    disc[] --> Stores discovery times of visited vertices
    parent[] --> Stores parent vertices in DFS tree
    ap[] --> Store articulation points'''
    def APUtil(self, u, visited, ap, parent, low, disc):

        #Count of children in current node
        children =0
        # Mark the current node as visited and print it
        visited[u]= True
        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        #Recur for all the vertices adjacent to this vertex
        for v in self.graph2[u]:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[v] == False :
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[v])
                print ("low:  %s" %(low))
                print ("disc: %s" %(disc))
                input("enter to continue...")

                # u is an articulation point in following cases
                # (1) u is root of DFS tree and has two or more chilren.
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                #(2) If u is not root and low value of one of its child is more
                # than discovery value of u.
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

                # Update low value of u for parent function calls
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    #The function to do DFS traversal. It uses recursive APUtil()
    def AP(self):

        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V) #To store articulation points


        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if visited[i] == False:
                self.APUtil(i, visited, ap, parent, low, disc)

        for index, value in enumerate(ap):
            if value:
                print (index, value)

if __name__ == '__main__':
    # Create a graph given in the above diagram
    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)

    # print ("\nArticulation points in first graph ")
    # g1.AP()

    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    # print ("\nArticulation points in second graph ")
    # g2.AP()


    g3 = Graph (7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    # print ("\nArticulation points in third graph ")
    # g3.AP()

    #This code is contributed by Neelam Yadav

    g4 = Graph(13)
    g4.addEdge(0, 1)
    g4.addEdge(0, 2)
    g4.addEdge(0, 5)
    g4.addEdge(0, 11)

    g4.addEdge(1, 0)
    g4.addEdge(1, 2)
    g4.addEdge(1, 3)
    g4.addEdge(1, 4)
    g4.addEdge(1, 6)
    g4.addEdge(1, 7)
    g4.addEdge(1, 12)

    g4.addEdge(2, 0)
    g4.addEdge(2, 1)

    g4.addEdge(3, 1)
    g4.addEdge(3, 4)

    g4.addEdge(4, 1)
    g4.addEdge(4, 3)

    g4.addEdge(5, 0)

    g4.addEdge(6, 1)
    g4.addEdge(6, 8)
    g4.addEdge(6, 10)
    g4.addEdge(7, 1)
    g4.addEdge(7, 10)
    g4.addEdge(8, 6)
    g4.addEdge(9, 11)
    g4.addEdge(9, 12)
    g4.addEdge(10, 6)
    g4.addEdge(10, 7)
    g4.addEdge(11, 0)
    g4.addEdge(11, 9)
    g4.addEdge(11, 12)
    g4.addEdge(12, 1)
    g4.addEdge(12, 9)
    g4.addEdge(12, 11)
    print("\nArticulation points in g4 graph ")
    g4.AP()



