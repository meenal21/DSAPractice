class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create a dictionary of the tasks - and then n
        
        dic = dict()
        for i in tasks:
            dic[i] =  dic[i] + 1 if i in dic else 1
        
        sortedlist = sorted(dic.items(), key = lambda i: i[1], reverse = True)
        # max space - the one which value is highest - 
        if n == 0:
            return len(tasks)
        else:      
            val = (sortedlist[0][1]-1)*(n+1) + 1
            maxval = sortedlist[0][-1]
            for i in range(1,len(sortedlist)):
                if maxval == sortedlist[i][1]:
                    val += 1
                else:
                    break
            return max(len(tasks), val)