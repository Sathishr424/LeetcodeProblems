# Last updated: 25/9/2025, 12:21:32 am
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        mod = 10**9 + 7

        dp = [[[-1] * k for _ in range(n)] for _ in range(m)]

        def rec(i, j, rem):
            rem = (rem + grid[i][j]) % k
            
            if i == m-1 and j == n-1:
                return 1 if rem == 0 else 0
            
            if dp[i][j][rem] != -1:
                return dp[i][j][rem]

            ans = 0
            if i + 1 < m:
                ans += rec(i + 1, j, rem)
            if j + 1 < n:
                ans += rec(i, j + 1, rem)

            ans %= mod
            dp[i][j][rem] = ans
            return ans

        return rec(0, 0, 0)