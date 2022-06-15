from collections import defaultdict
from operator import truediv

from numpy import True_

class Graph:

    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def IsCyclicUtil(self,node,visited,recStack):
        visited[node] = True
        recStack[node] = True
        for neighbor in self.graph[node]:
            if visited[neighbor] == False:
                if self.IsCyclicUtil(neighbor,visited,recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                    return True

        recStack[node] = False
        return False 

    def detectCycle(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)

        for node in range(self.V):
            if visited[node] == False:
                if self.IsCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.detectCycle() == 1:
    print("Graph has a cycle")
else:
    print ("Graph has no cycle")