# Last updated: 12/6/2025, 5:52:58 am
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1): 
            dp[i][n] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]


        