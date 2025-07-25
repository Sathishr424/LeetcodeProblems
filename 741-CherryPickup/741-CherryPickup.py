# Last updated: 26/7/2025, 5:17:17 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid)
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

            # if i == n-1 and j == n-1:
            #     check.append((i, j, i2 + 1, j2))
            #     check.append((i, j, i2, j2 + 1))
            
            # if i2 == n-1 and j2 == n-1:
            #     check.append((i + 1, j, i2, j2))
            #     check.append((i, j + 1, i2, j2))
            
            add = grid[i][j]
            if i != i2 and j != j2: add += grid[i2][j2]
        
            for ni, nj, ni2, nj2 in check:
                if ni < m and nj < m and ni2 < m and nj2 < m and grid[ni][nj] != -1 and grid[ni2][nj2] != -1:
                    ans = max(ans, dfs(ni, nj, ni2, nj2) + add)
            
            return ans
        
        return max(0, dfs(0, 0, 0, 0))