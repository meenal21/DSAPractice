class Graph:

    def __init__(self,graph):
        self.graph = graph
        self.i = graph.__len__()
        self.j = graph[0].__len__()
        self.iin = [-1,-1,1,1,-1,0,0,1]
        self.jin = [-1,1,-1,1,0,1,-1,0]

    def islandUtil(self,i,j,visited):
        if self.graph[i][j] == 0 or visited[i][j] == True:
            return

        queue = []
        queue.append([i,j])

        while queue:
            ele = queue.pop()
            for i in range(self.iin.__len__()):
                ii = ele[0]+self.iin[i]
                jj = ele[1]+self.jin[i]
                if ii < 0 or jj < 0 or ii > self.i - 1 or jj > self.j - 1  :
                    pass
                else:
                    if visited[ii][jj] == True:
                        pass
                    elif self.graph[ii][jj] == 1:
                        queue.append([ii,jj])
                        visited[ii][jj] = 1
        


    def findIslands(self):
        visited = [[0 for i in range(self.j)] for j in range(self.i)]
        count = 0
        for i in range(self.i):
            for j in range(self.j):
                #print(visited[i][j])
                #print(i,j)
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.islandUtil(i,j,visited)
                    count += 1
        print(count)
        

g = Graph([[0,1],[1,0],[1,1],[1,0]])
g = Graph([[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]])
g.findIslands()
                
        
