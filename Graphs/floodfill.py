class Graph:

    def __init__(self,graph,vertices):
        self.graph = graph
        self.V = vertices
        


g = [[1,1,1],[1,1,0],[1,0,1]]
g = [[]]
sr = 1
sc = 1
color = 2


rows = len(g)
if rows:
    cols = len(g[0])


print(rows,cols) 