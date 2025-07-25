# Last updated: 26/7/2025, 2:05:11 am
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7

        dp = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def dfs(i, j, s):
            if dp[i][j][s] != -1: return dp[i][j][s]
            if i == m-1 and j == n-1:
                if (s + grid[i][j]) % k == 0: return 1
                return 0
            
            ans = 0
            if i+1 < m:
                ans += dfs(i + 1, j, (s + grid[i][j]) % k)
            if j+1 < n:
                ans += dfs(i, j + 1, (s + grid[i][j]) % k)
            dp[i][j][s] = ans % mod
            return dp[i][j][s]
        
        ans = dfs(0, 0, 0)
        return ans