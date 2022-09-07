class Solution:
    def isHappy(self, n: int) -> bool:
        
        setnew = set()
        while n not in setnew and n != 1:
            sq = 0
            setnew.add(n)
            while n > 0:
                dig = n%10
                n = n//10
                sq += pow(dig,2)
            n = sq
            
        return True if n == 1 else False