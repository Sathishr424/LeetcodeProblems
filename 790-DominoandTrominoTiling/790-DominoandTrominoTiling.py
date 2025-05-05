# Last updated: 5/5/2025, 12:01:28 pm
mod = 10**9 + 7
ways = [1, 2, 3, 3, 4, 4]

# [2, 1, 3, 3, 4, 4], (6, 8, 10, 12, 14, 18, ....) (vertival and horizontal)
# (5, 7, 9, 11, ....) (vertival and horizontal)

class Solution:
    def numTilings(self, N: int) -> int:
        
        @cache
        def rec(n):
            if n <= 1: return 1
            elif n == 2: return 2
            
            ret = 0
            for num in ways:
                if num > n: break
                ret = (ret + rec(n-num)) % mod
            
            for num in range(5, n+1, 2):
                ret = (ret + (rec(n-num) * 2 % mod)) % mod
            
            for num in range(6, n+1, 2):
                ret = (ret + (rec(n-num) * 2 % mod)) % mod

            return ret
        
        return rec(N)