# Last updated: 12/6/2025, 5:36:59 am
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[0 for _ in range(n)] for _ in range(m)]

        def is_valid(x, y):
            if x == -1 or x == m or y == -1 or y == n or grid[x][y] == 0 or vis[x][y] != 0: return False
            return True
        
        ret = 0
        def dfs(x, y):
            nonlocal ret
            if not is_valid(x, y): return 0

            vis[x][y] = 1
            ans = grid[x][y]
            ans += dfs(x+1, y) + dfs(x-1, y) + dfs(x, y-1) + dfs(x, y+1)
            ret = max(ret, ans)
            return ans
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    dfs(i, j)
        
        return ret