# Last updated: 17/9/2025, 9:01:00 pm
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        DIR = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        dp = [[-1] * n for _ in range(m)]
        
        def rec(i, j):
            if dp[i][j] != -1: return dp[i][j]
            ans = 1
            for i2, j2 in DIR:
                i2 += i
                j2 += j

                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] > grid[i][j]:
                    ans += rec(i2, j2)
            
            dp[i][j] = ans % mod
            return dp[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (rec(i, j) + ans) % mod
        
        return ans