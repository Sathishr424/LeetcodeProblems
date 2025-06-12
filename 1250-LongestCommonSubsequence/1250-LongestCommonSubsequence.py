# Last updated: 12/6/2025, 5:43:24 am
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        dp = [0] * (n+1)

        for i in range(1, m+1):
            prev = dp[0]
            for j in range(1, n+1):
                tmp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = tmp
        
        return dp[-1]
