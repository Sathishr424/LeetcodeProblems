# Last updated: 30/9/2025, 7:50:27 pm
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        rows = [0] * m
        cols = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                else:
                    rows[i] -= 1
                    cols[j] -= 1

        for i in range(m):
            for j in range(n):
                grid[i][j] = rows[i] + cols[j]

        return grid
                    