# Last updated: 31/5/2025, 11:20:21 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n+2) for _ in range(n+2)]
        ret = 1

        for i in range(1, n+1):
            for j in range(n, i-1, -1):
                if s[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j+1] + (1 if i == j else 2)
                    ret = cmax(ret, dp[i][j])
                else:
                    dp[i][j] = cmax(dp[i-1][j], dp[i][j+1])
                
        return ret