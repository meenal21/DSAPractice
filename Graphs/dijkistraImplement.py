import sys

class Graph:

    def __init__(self,vertices,graph):
        self.V = vertices
        self.graph = graph

    def minimumDist(self,dist,visited):
        min = sys.maxsize
        for i in range(self.V):
            if dist[i] < min and i not in visited :
                min = dist[i]
                min_ele = i
        return min_ele

    def printDistFromSource(self,dist):
        print("node   distance from source")
        for i in range(self.V):
            print("\t" + str(i) + "\t \t" + str(dist[i]))

    def dijkistra(self,source):
        dist = [sys.maxsize] * self.V
        visited = set()

        dist[source] = 0

        for i in range(self.V):
            x = self.minimumDist(dist,visited)
            visited.add(x)
            
            for y in range(self.V):
                if self.graph[x][y] > 0 and y not in visited and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printDistFromSource(dist)

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
g = Graph(9,graph)
g.dijkistra(0)
    
    