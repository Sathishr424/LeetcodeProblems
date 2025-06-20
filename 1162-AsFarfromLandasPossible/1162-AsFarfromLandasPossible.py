# Last updated: 20/6/2025, 8:46:47 am
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j))
        d = 1
        ret = -1
        while stack:
            new_stack = []
            for i, j in stack:
                for i2, j2 in DIR:
                    i2 += i
                    j2 += j
                    if 0 <= i2 < n and 0 <= j2 < n and grid[i2][j2] == 0:
                        grid[i2][j2] = 1
                        ret = d
                        new_stack.append((i2, j2))
            stack = new_stack
            d += 1

        return ret