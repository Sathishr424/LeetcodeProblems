# Last updated: 12/8/2025, 10:33:40 am
powers = [[0] * 301 for _ in range(6)]
for i in range(1, 6):
    y = 1
    while y ** i <= 300:
        powers[i][y] = y ** i
        y += 1

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod = 10**9 + 7
        y = 0
        while y <= 300 and powers[x][y] <= n:
            y += 1
        
        @cache
        def rec(index, rem):
            if rem == 0:
                return 1
            
            if index == y: return 0

            ans = 0
            if rem >= powers[x][index]:
                ans += rec(index + 1, rem)
                ans += rec(index + 1, rem - (powers[x][index]))
            
            return ans % mod
            
        return rec(1, n)