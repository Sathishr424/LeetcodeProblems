# Last updated: 26/7/2025, 2:18:01 am
mod = 10**9 + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                for d in range(k):
                    new_d = (d + val) % k
                    if i + 1 < m:
                        dp[i + 1][j][new_d] += dp[i][j][d]
                        dp[i + 1][j][new_d] %= mod
                    if j + 1 < n:
                        dp[i][j + 1][new_d] += dp[i][j][d]
                        dp[i][j + 1][new_d] %= mod
        
        ret = 0
        lastVal = grid[m-1][n-1]
        lastBlock = dp[m-1][n-1]
        for d in range(k):
            if (d + lastVal) % k == 0:
                ret += lastBlock[d]
                ret %= mod
            
        return ret