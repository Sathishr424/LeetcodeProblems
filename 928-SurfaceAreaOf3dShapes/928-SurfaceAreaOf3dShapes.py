# Last updated: 12/6/2025, 5:45:33 am
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = 0

        def check(i, j, curr):
            if i == -1 or j == -1 or i == m or j == n: return 0
            if memo[i][j]: return curr
            return grid[i][j]
        
        area = 0
        memo = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                area += curr > 0
                memo[i][j] = 1
                ans += abs(curr - check(i+1, j, curr))
                ans += abs(curr - check(i-1, j, curr))
                ans += abs(curr - check(i, j+1, curr))
                ans += abs(curr - check(i, j-1, curr))
        
        return ans + (area * 2)

                