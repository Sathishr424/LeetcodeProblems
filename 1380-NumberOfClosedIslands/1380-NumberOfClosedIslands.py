# Last updated: 12/6/2025, 5:42:42 am
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        def dfs(i, j):
            if grid[i][j] == 1: return True
            elif i == 0 or j == 0 or i == m-1 or j == n-1: return False
            grid[i][j] = 1
            ans = dfs(i+1, j)
            ans &= dfs(i-1, j)
            ans &= dfs(i, j+1)
            ans &= dfs(i, j-1)
            return ans

        for i in range(1, m-1):
            for j in range(1, n-1):
                cnt += grid[i][j] == 0 and dfs(i, j)
        return cnt