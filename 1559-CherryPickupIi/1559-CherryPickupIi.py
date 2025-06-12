# Last updated: 12/6/2025, 5:41:35 am
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-1] * n for _ in range(n)] for _ in range(m)]
        
        def dfs(index, j1, j2):
            if index == m or j1 == n or j1 == -1 or j2 == n or j2 == -1: return 0
            if dp[index][j1][j2] != -1: return dp[index][j1][j2]
            tmp = grid[index][j1]
            if j1 != j2:
                tmp += grid[index][j2]
            if index+1 < m:
                ans = 0
                for i in range(-1, 2, 1):
                    for j in range(-1, 2, 1):
                        ans = max(ans, dfs(index+1, j1+i, j2+j))
                tmp += ans
            dp[index][j1][j2] = tmp
            return tmp
        
        return dfs(0, 0, n-1)
        