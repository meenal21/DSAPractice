from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFSUtil(self,u):
        visited = set()
        visited.add(u)
        
        queue = []
        queue.append(u)

        while queue:
            v = queue.pop()
            print(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(2,0)
g.addEdge(1,2)
g.addEdge(3,3)

g.BFSUtil(2)
        
            
