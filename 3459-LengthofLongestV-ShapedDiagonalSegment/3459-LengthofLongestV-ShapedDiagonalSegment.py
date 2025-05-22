# Last updated: 23/5/2025, 12:00:26 am
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[[0] * 8 for _ in range(n)] for _ in range(m)]

        DIR_hash = {
            (1, 1): 3, # top-left to bottom-right
            (1, -1): 2, # top-left to bottom-left
            (-1, -1): 1, # bottom-right to top-left
            (-1, 1): 0 # bottom-left to top-right
        }

        DIR = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

        def dfs(i, j, z):
            if visited[i][j][z]: return visited[i][j][z]
            d = z // 2
            t = z % 2

            ans = 1

            i2, j2 = DIR[d]
            i2 += i
            j2 += j

            next_ = 0 if grid[i][j] == 2 else 2

            if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == next_:
                ans = max(ans, dfs(i2, j2, d * 2 + t) + 1)
            if t == 0:
                i2, j2 = DIR[DIR_hash[DIR[d]]]
                i2 += i
                j2 += j
                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == next_:
                    new_d = DIR_hash[DIR[d]]
                    ans = max(ans, dfs(i2, j2, new_d * 2 + 1) + 1)
            
            visited[i][j][z] = ans
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
                        ret = max(ret, dfs(i2, j2, d * 2) + 1)

        return ret