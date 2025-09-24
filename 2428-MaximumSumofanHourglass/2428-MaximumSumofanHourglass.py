# Last updated: 24/9/2025, 11:20:27 pm
dirs = [(0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        best = 0
        for i in range(m-2):
            for j in range(n-2):
                curr = grid[i][j]
                for i2, j2 in dirs:
                    curr += grid[i + i2][j + j2]
                best = max(best, curr)

        return best