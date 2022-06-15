## check sum - if all are changed - then true or only one is true

class Graph:
    def __init__(self,wordlist,end):
        self.listwords = []
        self.end = end
        self.wordlist = wordlist
        self.path = []

    def wordHelper(self,beg,count,wordli):
        if beg == self.end:
            self.listwords.append(count)
            self.path.append(wordli)
            return


        for i in range(self.wordlist.__len__()):
            ele = self.wordlist.pop(i)
            # perform check here
            sum = 0
            for k in range(beg.__len__()):
                sum += (ele[k] == beg[k])
            
            if sum == beg.__len__() - 1:
                self.wordHelper(ele,count+1,wordli+ele)
            self.wordlist.insert(i,ele)

    def wordladder(self,beg):
        count = 0
        self.wordHelper(beg,count,"")
        return self.listwords,self.path

wordl = ["hot","dot","dog","lot","log","cog"]
beg = "hit"
end = "cog"

g = Graph(wordl,end)
countlist, words = g.wordladder(beg)
print(min(countlist))