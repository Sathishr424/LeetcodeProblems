# Last updated: 31/5/2025, 11:18:18 pm
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+2) for _ in range(n+2)]
        ret = 1

        for i in range(1, n+1):
            for j in range(n, i-1, -1):
                if s[i-1] == s[j-1]:
                    # print(i, j, (i-1, j-1), dp[i-1])
                    dp[i][j] = dp[i-1][j+1] + (1 if i == j else 2)
                    ret = max(ret, dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j+1])
                
        return ret