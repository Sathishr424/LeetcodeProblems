# Last updated: 12/6/2025, 5:54:08 am
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return 0
        m = len(grid)
        n = len(grid[0])
        
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if grid[i-1][j-1] == 0:
                    dp[j] = dp[j] + dp[j-1]
                else:
                    dp[j] = 0
        return dp[-1]
        
        