# Last updated: 12/6/2025, 5:49:09 am
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def check(i, j):
            return grid[i][j]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += i+1 < m and check(i+1, j)
                    ans += i-1 >= 0 and check(i-1, j)
                    ans += j+1 < n and check(i, j+1)
                    ans += j-1 >= 0 and check(i, j-1)
        
        for i in range(m):
            ans += grid[i][0]
        
        for i in range(n):
            ans += grid[0][i]
        
        for i in range(m):
            ans += grid[i][n-1]
        
        for i in range(n):
            ans += grid[m-1][i]
                
        return ans
            