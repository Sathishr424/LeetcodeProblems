# Last updated: 28/10/2025, 4:50:28 pm
class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        if grid[0][0] == 0 or grid[-1][-1] == 0: return true
        m = len(grid)
        n = len(grid[0])

        dp = [[[-1,-1] for _ in range(n)] for _ in range(m)]
        
        def dfs(i, j, d):
            if i == m-1 and j == n-1:
                dp[i][j][d] = 1
                return 1
            if dp[i][j][d] != -1: return dp[i][j][d]
            # print(i, j, d)
            can = 0
            if i + 1 < m and grid[i + 1][j] == 1:
                can = dfs(i + 1, j, 0) or can
            if j + 1 < n and grid[i][j + 1] == 1:
                can = dfs(i, j + 1, 1) or can 

            dp[i][j][d] = can
            return can

        dfs(0, 0, 0)
        if not dp[0][0][0]: return True
        if m == 1 and n <= 2: return False
        if n == 1 and m <= 2: return False

        if n > 1 and dp[0][1][1] != 1: return True
        if m > 1 and dp[1][0][0] != 1: return True
        # [print(row) for row in dp]
        for i in range(1, m-1):
            cnt = 0
            for j in range(n):
                if dp[i][j][0] == 1 and dp[i + 1][j][0] == 1:
                    cnt += 1

            if cnt <= 1: return True

        if dp[-1][-1][0] == -1 or dp[-1][-1][1] == -1: return True

        return False

        