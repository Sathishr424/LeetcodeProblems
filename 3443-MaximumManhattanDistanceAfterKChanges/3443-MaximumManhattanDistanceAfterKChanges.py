# Last updated: 20/6/2025, 8:36:25 am
cmax = lambda x, y: x if x > y else y
inf = 200
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dis = [[inf] * n for _ in range(n)]
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j))
        d = 0
        ret = -1
        while stack:
            d += 1
            new_stack = []
            for i, j in stack:
                for i2, j2 in DIR:
                    i2 += i
                    j2 += j
                    if 0 <= i2 < n and 0 <= j2 < n and grid[i2][j2] == 0 and d < dis[i2][j2]:
                        ret = cmax(ret, d)
                        dis[i2][j2] = d
                        new_stack.append((i2, j2))
            stack = new_stack

        return -1 if ret == inf else ret