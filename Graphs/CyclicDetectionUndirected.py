

class Graph:
    def __init__(self,vertices):
        rows,cols = (vertices,vertices)
        self.V = vertices
        self.graph = [[0 for i in range(cols)] for j in range(rows)]

    def addEdge(self,u,v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1


    def showGraph(self):
        for row in self.graph:
            print(row)

    def isCyclic(self,v,visited,parent):
        visited[v] = True

        for i in range(self.V):
            if self.graph[v][i] == True:    
                if i == parent:
                    continue
                elif visited[i] == True:
                    return True
                elif self.isCyclic(i,visited,v) == True:
                    return True

        return False
            


    def detectCycle(self):
        visited = [False]*(self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclic(node,visited,-1) == True:
                    return True
        return False

g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(3,2)
g.addEdge(4,3)

g.showGraph()

if g.detectCycle() == True:
    print("There is a cycle")
else:
    print("No cycle present")