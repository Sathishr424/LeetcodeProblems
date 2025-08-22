# Last updated: 22/8/2025, 1:11:21 pm
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        pos = [0, 0, 0, 0]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pos = [i, j, i, j]
                    break
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    pos[0] = min(pos[0], i)
                    pos[1] = max(pos[1], j)
                    pos[2] = max(pos[2], i)
                    pos[3] = min(pos[3], j)
        
        # start = pos[0], pos[3]
        # end = pos[2], pos[1]

        width = pos[1] - pos[3] + 1
        height = pos[2] - pos[0] + 1
        # print(pos, width, height)

        return height * width