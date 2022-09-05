class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # move ahead 
        # starting from any tree
        dic = dict()
        minval = 0
        i = 0
        j = 0
        inc = 0
        while j < len(fruits):
            
            if len(dic) == 2 and fruits[j] not in dic:
                itert = sorted(dic.items(), key = lambda item: item[1])[0]
                
                if minval < inc:
                    minval = inc
                inc -= itert[1] - i + 1
                i = itert[1] + 1
                del dic[itert[0]]
            
            dic[fruits[j]] = j
                
            inc += 1
            j += 1
        
        if minval < inc:
            return inc
                
        return minval
            
                