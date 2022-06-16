class ChessBoard:

    def __init__(self,N,finali,finalj):
        self.graph = [[0 for i in range(N)] for j in range(N)]
        self.V = N
        self.steps = []
        self.finali = finali
        self.finalj = finalj
    
    def stepsCounter(self,ini,inj,count):
        if ini==self.finali and inj==self.finalj:
            self.steps.append(count)
            print(count)
            return
        
        if ini > self.V - 1 or inj > self.V-1 or ini < 0 or inj < 0:
            #print(ini,inj)
            return
        
        if self.graph[ini][inj] == False:
            self.graph[ini][inj] = True
            #print(ini,inj)
            
            self.stepsCounter(ini+2,inj+1,count+1)
            self.stepsCounter(ini-2,inj+1,count+1)
            self.stepsCounter(ini-2,inj-1,count+1)
            self.stepsCounter(ini+2,inj-1,count+1)
            self.stepsCounter(ini+1,inj+2,count+1)
            self.stepsCounter(ini-1,inj+2,count+1)
            self.stepsCounter(ini-1,inj-2,count+1)
            self.stepsCounter(ini+1,inj-2,count+1)
            self.graph[ini][inj] = False

    def KnightSteps(self,ini,inj):
        count = 0
        self.stepsCounter(ini,inj,count)
        return self.steps

N = 6
ini = 4
inj = 5
finali = 1
finalj = 1
c = ChessBoard(N,finali-1,finalj-1)
total = c.KnightSteps(ini-1,inj-1)
print(total)
if total:
    print(min(total))
else:
    print(0)

