# Last updated: 12/6/2025, 5:54:07 am
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        for i in range(1, m+1):
            tmp = dp[0]
            for j in range(1, n+1):
                curr = dp[j]
                dp[j] = min(dp[j], dp[j-1]) + grid[i-1][j-1]
                tmp = curr
    
        return dp[-1]