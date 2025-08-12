# Last updated: 12/8/2025, 10:26:10 am
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        y = 0
        while y ** x <= n:
            y += 1
        
        @cache
        def rec(index, rem):
            if rem == 0:
                return 1
            
            if index == y+1: return 0

            ans = rec(index + 1, rem)
            if rem >= index ** x:
                ans += rec(index + 1, rem - (index ** x))
            return ans % mod
            
        return rec(1, n)