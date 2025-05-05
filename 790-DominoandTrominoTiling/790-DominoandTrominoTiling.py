# Last updated: 5/5/2025, 12:06:16 pm
mod = 10**9 + 7
# [2, 1, 3, 3, 4, 4], (6, 8, 10, 12, 14, 18, ....) (vertival and horizontal)
# (5, 7, 9, 11, ....) (vertival and horizontal)

class Solution:
    def numTilings(self, N: int) -> int:
        @cache
        def rec(n):
            if n <= 1: return 1
            elif n == 2: return 2
            
            ret = rec(n-1)
            ret = (ret + rec(n-2)) % mod
            
            for num in range(3, n+1):
                ret = (ret + (rec(n-num) * 2 % mod)) % mod

            return ret
        
        return rec(N)