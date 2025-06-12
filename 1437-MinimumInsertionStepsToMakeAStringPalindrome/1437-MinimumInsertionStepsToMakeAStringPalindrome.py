# Last updated: 12/6/2025, 5:42:22 am
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[1 for _ in range(n)] for _ in range(n)]
        for i in range(1,n):
            dp[1][i] = 1 + (s[i-1] == s[i])

        for i in range(2, n):
            for j in range(i, n):
                if s[j-i] == s[j]:
                    dp[i][j] = 2 + dp[i-2][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
        return n - dp[-1][-1]
