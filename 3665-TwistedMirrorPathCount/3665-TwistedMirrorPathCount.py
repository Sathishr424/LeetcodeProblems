# Last updated: 31/8/2025, 12:12:35 am
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        # N = 500
        # grid = [[random.randrange(2) for _ in range(N)] for _ in range(N)]
        # grid[0][0] = 0
        # grid[-1][-1] = 0
        mod = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        dp = [[[-1, -1] for _ in range(n)] for _ in range(m)]
        dp[-1][-1][0] = 1
        dp[-1][-1][1] = 1
        def rec(i, j, is_down):
            if i == m or j == n: return 0
            if dp[i][j][is_down] != -1: return dp[i][j][is_down]
            if i == m-1 and j == n-1: return 1

            if grid[i][j] == 1:
                if is_down:
                    return rec(i, j + 1, False)
                else:
                    return rec(i + 1, j, True)

            ans = 0
            if i+1 < m:
                ans += rec(i + 1, j, True)
            if j+1 < n:
                ans += rec(i, j + 1, False)
            dp[i][j][is_down] = ans % mod
            return dp[i][j][is_down]

        return rec(0, 0, False)
                    