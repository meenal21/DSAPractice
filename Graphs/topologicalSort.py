from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topSortUtil(self,u,visited,stack):
        visited.add(u)

        for i in self.graph[u]:
            if i not in visited:
                self.topSortUtil(i,visited,stack)

        stack.append(u)


    def topologicalSort(self):
        visited = set()
        stack = []

        for i in range(self.V):
            if i not in visited:
                self.topSortUtil(i,visited,stack)
        
        print(stack[ ::-1]) # returns the list in reverse order


g = Graph(6)
"""
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
"""

g.addEdge(0,5)
g.addEdge(0,4)
g.addEdge(4,1)
g.addEdge(3,1)
g.addEdge(2,3)
g.addEdge(2,5)
g.topologicalSort()