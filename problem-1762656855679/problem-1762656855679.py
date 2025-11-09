# Last updated: 9/11/2025, 8:24:15 am
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # k = 1000
        # grid = [[random.randint(0, 3) for _ in range(200)] for _ in range(200)]
        
        m = len(grid)
        n = len(grid[0])

        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        def getCostCell(cell):
            return 1 if cell > 0 else 0
        
        def getCost(i, j):
            return getCostCell(grid[i][j])
        
        def rec(i, j, rem):
            if dp[i][j][rem] != -1: return dp[i][j][rem]
            if i == m-1 and j == n-1:
                return 0
            
            ans = -inf
            if i+1 < m and rem >= getCost(i + 1, j):
                cell = grid[i+1][j]
                ans = max(ans, rec(i + 1, j, rem - getCostCell(cell)) + cell)
            if j+1 < n and rem >= getCost(i, j + 1):
                cell = grid[i][j+1]
                ans = max(ans, rec(i, j + 1, rem - getCostCell(cell)) + cell)

            dp[i][j][rem] = ans
            return ans

        ans = rec(0, 0, k)
        return -1 if ans == -inf else ans