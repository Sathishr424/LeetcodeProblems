# Last updated: 12/25/2025, 7:09:31 PM
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        # k = 1000
        # grid = [[random.randint(0, 3) for _ in range(200)] for _ in range(200)]
        
        m = len(grid)
        n = len(grid[0])

        dp = [[defaultdict(lambda: -inf) for _ in range(n)] for _ in range(m)]
        dp[0][0][k] = 0
        
        def getCostCell(cell):
            return 1 if cell > 0 else 0
        
        def getCost(i, j):
            return getCostCell(grid[i][j])

        cost = 0
        for i in range(m):
            for j in range(n):
                for rem in dp[i][j]:
                    if i + 1 < m:
                        cell = grid[i+1][j]
                        cost = getCostCell(cell)
                        if rem >= cost:
                            cost = rem - cost
                            dp[i + 1][j][cost] = cmax(dp[i + 1][j][cost], dp[i][j][rem] + cell)
                    if j + 1 < n:
                        cell = grid[i][j+1]
                        cost = getCostCell(cell)
                        if rem >= cost:
                            cost = rem - cost
                            dp[i][j + 1][cost] = cmax(dp[i][j + 1][cost], dp[i][j][rem] + cell)

        ans = -inf
        for rem in dp[m-1][n-1]:
            ans = max(ans, dp[m-1][n-1][rem])
        return -1 if ans == -inf else ans