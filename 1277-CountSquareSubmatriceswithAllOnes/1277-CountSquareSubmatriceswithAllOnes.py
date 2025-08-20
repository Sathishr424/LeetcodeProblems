# Last updated: 20/8/2025, 11:00:33 am
"""
[0,1,1,1,1,1],
[1,1,1,1,1,1],
[0,1,1,1,1,1],
[0,1,1,1,1,1],
[0,1,1,1,1,1]
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        grid = [[0] * n for _ in range(m)]

        tot = 0
        DIR = [(0, 1), (1, 1), (1, 0)]

        def dfs(i, j):
            if grid[i][j] != 0: return grid[i][j]
            matrix[i][j] = 0
            max_cnt = inf
            cnt = 0
            for i2, j2 in DIR:
                i2 += i
                j2 += j

                if 0 <= i2 < m and 0 <= j2 < n and (matrix[i2][j2] == 1 or grid[i2][j2] != 0):
                    ans = dfs(i2, j2)
                    max_cnt = min(ans, max_cnt)
                    cnt += 1
            if cnt == 3:
                grid[i][j] = max_cnt + 1
                return max_cnt + 1
            else:
                grid[i][j] = 1
                return 1
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                tot += grid[i][j]
        
        return tot