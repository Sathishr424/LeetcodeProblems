# Last updated: 26/7/2025, 5:18:29 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == -1: return 0

        @cache
        def dfs(i, j, i2, j2):
            if i == n-1 and j == n-1 and i2 == n-1 and j2 == n-1:
                return grid[i][j]
            
            ans = -inf
            check = [
                (i + 1, j, i2 + 1, j2),
                (i + 1, j, i2, j2 + 1),
                (i, j + 1, i2 + 1, j2),
                (i, j + 1, i2, j2 + 1),
            ]
            
            add = grid[i][j]
            if i != i2 and j != j2: add += grid[i2][j2]
        
            for ni, nj, ni2, nj2 in check:
                if ni < n and nj < n and ni2 < n and nj2 < n and grid[ni][nj] != -1 and grid[ni2][nj2] != -1:
                    ans = cmax(ans, dfs(ni, nj, ni2, nj2) + add)
            
            return ans
        
        return cmax(0, dfs(0, 0, 0, 0))