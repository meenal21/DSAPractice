class Graph:

    def __init__(self,vertices,graph):
        self.graph = graph
        self.V = vertices
        self.glist = []

    def showGraph(self):
        for row in self.graph:
            print(row)

    def checkPath(self,i,j,visited,path):
        #print(i,j)
        #print(path)
        if(i <  0 or j < 0 or i > self.V-1 or j > self.V-1 ):
            #print("Index out of bounds")
            return 
        if(visited[i][j] == True):
            #print("Already Visited")
            return 
        visited[i][j] = True


        if ((i == self.V-1) & (j == self.V-1)):
            self.glist.append(path)
        elif(self.graph[i][j] == True):
            self.checkPath(i-1,j,visited,path + 'U')
            self.checkPath(i+1,j,visited,path + 'D')
            self.checkPath(i,j-1,visited,path + 'L')
            self.checkPath(i,j+1,visited,path + 'R')
        
        visited[i][j] = False
            
    def findPath(self):
        visited = [[0 for i in range(self.V)] for j in range(self.V)]
        #print(vertices)

        if((self.graph[self.V-1][self.V-1] == False) | (self.graph[0][0] == False)):
            return -1
        self.checkPath(0,0,visited,'')
        print(self.glist)


m = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
g = Graph(4,m)
g.showGraph()
g.findPath()