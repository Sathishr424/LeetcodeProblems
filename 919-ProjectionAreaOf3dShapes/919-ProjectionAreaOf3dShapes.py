# Last updated: 12/6/2025, 5:45:40 am
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ret = 0
        m = len(grid)
        n = len(grid[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                cols[j] = max(cols[j], grid[i][j])
                rows[i] = max(rows[i], grid[i][j])
                ret += grid[i][j] > 0
        
        return sum(rows) + sum(cols) + ret
                