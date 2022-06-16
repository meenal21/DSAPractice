from collections import defaultdict
import sys

class Graph:

    def __init__(self,vertices):
        self.V = vertices + 1
        self.graph = defaultdict(list)
        self.indegree = dict()
        self.time = [sys.maxsize] * (self.V)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def calcInDegree(self):
        indegree = [0] * (self.V )
        for i in range(self.V):
            for j in self.graph[i]:
                indegree[j] += 1
        return indegree

    def minUtil(self,u,v):
        if self.time[u] > self.time[v]:
            self.time[u] = self.time[v] + 1
        
        for i in self.graph[u]:
            self.minUtil(i,u)


    def minTimeJob(self):
        indegree = self.calcInDegree()
        for i in range(self.V):
            if indegree[i] == 0:
                self.time[i] = 0
                self.minUtil(i,i)
        print(self.time)
        
            





g = Graph(10)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(1,5)
g.addEdge(2,3)
g.addEdge(2,9)
g.addEdge(4,8)
g.addEdge(3,6)
g.addEdge(6,7)
g.addEdge(4,8)
g.addEdge(8,10)
g.addEdge(7,8)
g.addEdge(2,8)

g.minTimeJob()