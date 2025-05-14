# Last updated: 15/5/2025, 2:07:20 am
N = 10**5
dp = [[[-1] * 2 for _ in range(3)] for _ in range(N+1)]

class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7

        def dfs(x, l, a):
            if dp[x][l][a] != -1: return dp[x][l][a]
            if x == 0: return 1
            ans = 0
            if l < 2: ans = (ans + dfs(x-1, l+1, a)) % mod
            if a == 0: ans = (ans + dfs(x-1, 0, a+1)) % mod

            ans = (ans + dfs(x-1, 0, a)) % mod
            dp[x][l][a] = ans
            return ans
        
        return dfs(n, 0, 0)