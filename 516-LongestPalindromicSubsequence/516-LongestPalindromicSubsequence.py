# Last updated: 31/5/2025, 11:30:44 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+2)
        ret = 1

        for i in range(1, n+1):
            prev = dp[n+1]
            for j in range(n, i-1, -1):
                curr = dp[j]
                if s[i-1] == s[j-1]:
                    dp[j] = prev + (1 if i == j else 2)
                    ret = cmax(ret, dp[j])
                else:
                    dp[j] = cmax(dp[j+1], dp[j])
                prev = curr
                
        return ret