# Last updated: 22/8/2025, 1:13:34 pm
cmin = lambda x, y: x if x < y else y
cmax = lambda x, y: x if x > y else y

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        pos = [m, 0, 0, n]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pos[0] = cmin(pos[0], i)
                    pos[1] = cmax(pos[1], j)
                    pos[2] = cmax(pos[2], i)
                    pos[3] = cmin(pos[3], j)

        width = pos[1] - pos[3] + 1
        height = pos[2] - pos[0] + 1

        return height * width