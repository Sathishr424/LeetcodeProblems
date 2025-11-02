# Last updated: 2/11/2025, 7:39:15 am
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        grid = [[0] * n for _ in range(m)]

        for i, j in guards:
            grid[i][j] = 1
        for i, j in walls:
            grid[i][j] = 2

        def rec(i, j, i2, j2):
            grid[i][j] = -1
            i3 = i2 + i
            j3 = j2 + j

            if 0 <= i3 < m and 0 <= j3 < n and grid[i3][j3] <= 0:
                rec(i3, j3, i2, j2)
        
        for i, j in guards:
            for i2, j2 in DIR:
                i3 = i2 + i
                j3 = j2 + j
                if 0 <= i3 < m and 0 <= j3 < n and grid[i3][j3] <= 0:
                    rec(i3, j3, i2, j2)
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1 or grid[i][j] > 0:
                    cnt += 1
        
        return m * n - cnt