class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        sp, eff, heap = 0,0,[]
        for e,s in sorted(zip(efficiency,speed), reverse = True):
            if len(heap) == k:
                sp -= heappop(heap)
            sp += s
            eff = max(eff, sp*e)
            heappush(heap,s)
        
        return eff % (10  ** 9 + 7)
            
            # either you take or you dont take, us according tree banega - cou
            