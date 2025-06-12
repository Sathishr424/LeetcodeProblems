# Last updated: 12/6/2025, 5:44:35 am
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = []
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rottens.append([i,j])
        minutes = 0
        while rottens:
            new_rottens = []
            for i, j in rottens:
                if i+1 < n and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    new_rottens.append([i+1, j])
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    new_rottens.append([i-1, j])
                if j+1 < m and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    new_rottens.append([i, j+1])
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    new_rottens.append([i, j-1])
            rottens = new_rottens
            if rottens: minutes += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: return -1
        return minutes
            
