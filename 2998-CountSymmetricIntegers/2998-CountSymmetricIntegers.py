# Last updated: 12/6/2025, 5:36:28 am
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ret = 0
        for num in range(low, high+1):
            n = len(str(num))
            if n % 2 != 0: continue
            
            prefix = []
            tot = 0

            while num:
                tot += num % 10
                num //= 10

                prefix.append(tot)
            
            half = prefix[n // 2 - 1]
            if tot - half == half: ret += 1
        
        return ret

