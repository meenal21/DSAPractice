from collections import defaultdict
import string
# topological order
class Graph:
    
    def __init__(self,K,input_alphabet):
        self.V = K
        self.graph = defaultdict(list)
        self.input_alphabet = input_alphabet
        self.alphdict = dict()
        for i in range(input_alphabet.__len__()):
            self.alphdict[input_alphabet[i]] = i

    def addEdge(self,u,v):
        
        self.graph[u].append(v)

    def createGraph(self,dict1):
        for i in range(dict1.__len__() - 1):
            min1 = min(dict1[i].__len__(),dict1[i+1].__len__())
            for j in range(min1):
                if dict1[i][j] != dict1[i+1][j]:
                    self.addEdge(self.alphdict[dict1[i][j]],self.alphdict[dict1[i+1][j]]) 
                    break
        for r in self.graph:
            print(r,self.graph[r])
    
    def topoUtil(self,u,visited,stack):
        visited.add(u)
        for i in self.graph[u]:
            if i not in visited:
                self.topoUtil(i,visited,stack)
        stack.append(u)        

    def topologicalSort(self):
        visited = set()
        stack = []

        for i in range(self.V):
            if i not in visited:
                self.topoUtil(i,visited,stack)

        list1 = []
        for i in reversed(stack):
            list1.append(self.input_alphabet[i])

        return list1

            

K = 4
alphabet = list(string.ascii_lowercase)
input_alphabet = alphabet[:K:1]
print(input_alphabet)
g = Graph(K,input_alphabet)
listhere = ["baa","abcd","abca","cab","cad"]
g.createGraph(listhere)
print(g.topologicalSort())