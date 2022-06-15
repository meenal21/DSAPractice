from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self,u,visited):
        visited.add(u)
        print(u)

        for neighbor in self.graph[u]:
            if neighbor not in visited:
                self.DFSUtil(neighbor,visited)

    def DFS(self, u):
        visited = set()

        self.DFSUtil(u,visited)


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(2,0)
g.addEdge(1,2)
g.addEdge(3,3)

g.DFS(2)