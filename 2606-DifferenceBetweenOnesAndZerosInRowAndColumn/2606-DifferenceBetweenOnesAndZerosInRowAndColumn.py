# Last updated: 12/6/2025, 5:37:32 am
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = rows[i] + cols[j] - (n-rows[i]) - (m-cols[j])
        return grid