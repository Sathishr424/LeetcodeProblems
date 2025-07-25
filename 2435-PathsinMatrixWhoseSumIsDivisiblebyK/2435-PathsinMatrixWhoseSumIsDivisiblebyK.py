# Last updated: 26/7/2025, 2:23:21 am
mod = 10**9 + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                for d in range(k):
                    new_d = (d + val) % k
                    dp[i + 1][j][new_d] = (dp[i + 1][j][new_d] + dp[i][j][d]) % mod
                    dp[i][j + 1][new_d] = (dp[i][j + 1][new_d] + dp[i][j][d]) % mod
        
        return dp[m][n-1][0]