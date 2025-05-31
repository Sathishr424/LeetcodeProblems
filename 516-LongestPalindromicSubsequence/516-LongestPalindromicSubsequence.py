# Last updated: 31/5/2025, 11:32:03 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        ret = 1

        for i in range(n):
            prev = 0
            for j in range(n-1, i-1, -1):
                curr = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + (1 if i == j else 2)
                    ret = cmax(ret, dp[j])
                else:
                    dp[j] = cmax(dp[j+1], dp[j])
                prev = curr
                
        return ret