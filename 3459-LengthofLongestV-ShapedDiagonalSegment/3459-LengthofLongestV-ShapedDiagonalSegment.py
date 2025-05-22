# Last updated: 22/5/2025, 11:28:41 pm
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # visited = [[[[-1] * 2 for _ in range(4)] for _ in range(n)] for _ in range(m)]

        DIR_hash = {
            (1, 1): 3, # top-left to bottom-right
            (1, -1): 2, # top-left to bottom-left
            (-1, -1): 1, # bottom-right to top-left
            (-1, 1): 0 # bottom-left to top-right
        }

        DIR = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

        @cache
        def dfs(i, j, d, t):
            # if visited[i][j][d][t] != -1: return visited[i][j][d][t]
            ans = 1

            i2, j2 = DIR[d]
            i2 += i
            j2 += j

            if 0 <= i2 < m and 0 <= j2 < n and (grid[i2][j2] != grid[i][j] and grid[i2][j2] != 1):
                ans = max(ans, dfs(i2, j2, d, t) + 1)
            if t == 0:
                i2, j2 = DIR[DIR_hash[DIR[d]]]
                i2 += i
                j2 += j
                if 0 <= i2 < m and 0 <= j2 < n and (grid[i2][j2] != grid[i][j] and grid[i2][j2] != 1):
                    ans = max(ans, dfs(i2, j2, DIR_hash[DIR[d]], t+1) + 1)
            
            # visited[i][j][d][t] = ans
            return ans
        
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                ret = max(ret, 1)
                for d, (i2, j2) in enumerate(DIR):
                    i2 += i
                    j2 += j

                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 2:
                        ret = max(ret, dfs(i2, j2, d, 0) + 1)

        return ret