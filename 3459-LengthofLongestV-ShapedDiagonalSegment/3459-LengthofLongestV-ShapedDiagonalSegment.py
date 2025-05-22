# Last updated: 23/5/2025, 12:47:26 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[[0] * 8 for _ in range(n)] for _ in range(m)]

        DIR_hash = [3, 0, 1, 2]
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
                ans = cmax(ans, dfs(i2, j2, d * 2 + t) + 1)
            if t == 0:
                i2, j2 = DIR[DIR_hash[d]]
                i2 += i
                j2 += j
                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == next_:
                    ans = cmax(ans, dfs(i2, j2, DIR_hash[d] * 2 + 1) + 1)
            
            visited[i][j][z] = ans
            return ans
        
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1: continue
                ret = cmax(ret, 1)
                for d, (i2, j2) in enumerate(DIR):
                    i2 += i
                    j2 += j

                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 2:
                        ret = cmax(ret, dfs(i2, j2, d * 2) + 1)

        return ret