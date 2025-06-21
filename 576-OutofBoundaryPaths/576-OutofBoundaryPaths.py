# Last updated: 22/6/2025, 3:37:19 am
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, r: int, c: int) -> int:
        mod = 10**9 + 7
        DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        @cache
        def dfs(i, j, rem):
            if i == -1 or i == m or j == -1 or j == n: return 1
            if rem == 0: return 0
            ans = 0
            for i2, j2 in DIR:
                i2 += i
                j2 += j

                if -1 <= i2 <= m and -1 <= j2 <= n:
                    ans += dfs(i2, j2, rem-1)
                    ans %= mod
            return ans
                    
        
        return dfs(r, c, maxMove)
