class Graph:

    def __init__(self,graph,sr,sc,cols,rows):
        self.graph = graph
        self.visited = [[0 for i in range(cols)] for j in range(rows)]
        self.initcolor = graph[sr][sc]
        
    def showGraph(self):
        for row in self.graph:
            print(row)

    def floodfill(self,i,j,color,rows,cols):
        if (i > rows-1) or (j > cols-1) or (i < 0) or (j < 0):
            return 
        if self.visited[i][j] == False:
            if self.graph[i][j] == self.initcolor:
                self.graph[i][j] = color
                self.floodfill(i+1,j,color,rows,cols)
                self.floodfill(i,j+1,color,rows,cols)
                self.floodfill(i-1,j,color,rows,cols)
                self.floodfill(i,j-1,color,rows,cols)
        else:
            return
            
        self.visited[sr][sc] = True

g = [[1,1,1],[1,1,0],[1,0,1]]
#g = [[]]
sr = 1
sc = 1
color = 2


rows = len(g)
if rows:
    cols = len(g[0])
gr = Graph(g,sr,sc,cols,rows)
gr.showGraph()
gr.floodfill(sr,sc,color,rows,cols)
gr.showGraph()

#print(rows,cols) 