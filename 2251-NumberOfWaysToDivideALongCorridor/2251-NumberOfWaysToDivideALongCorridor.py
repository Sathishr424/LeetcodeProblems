# Last updated: 12/6/2025, 5:38:41 am
class Solution:
    def numberOfWays(self, corr: str) -> int:
        n = len(corr)
        # PPSPS PP SPS P SPS P SS

        mod = (10**9) + 7
        ret = 1
        seats = 0
        plants = 0
        tmp = None
        prev = False

        for i in range(n):
            if corr[i] == 'S': 
                seats += 1
                if seats == 1 and tmp == None:
                    tmp = plants
                elif seats == 2:
                    if not prev: prev = True
                    else: ret *= tmp + 1

                    tmp = None
                    plants = 0
                    seats = 0
            else: plants += 1
        
        return ret % mod if prev and seats == 0 else 0
                    
