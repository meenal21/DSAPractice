class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numstr = str(num)
        leng = len(numstr)
        i = 0
        j = i+k
        count = 0
        while j <= leng:
            if int(numstr[i:j])!=0 and num % int(numstr[i:j]) == 0:
                count += 1
            
            i += 1
            j = i+k
        
        return count
               
              