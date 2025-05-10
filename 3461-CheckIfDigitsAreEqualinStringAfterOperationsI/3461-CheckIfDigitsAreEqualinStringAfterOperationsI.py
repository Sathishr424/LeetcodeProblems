# Last updated: 10/5/2025, 1:41:20 pm
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        dp = [int(i) for i in s]

        for i in range(1, n-1):
            for j in range(n-1, i-1, -1):
                dp[j] = (dp[j] + dp[j-1]) % 10
        
        return dp[-1] == dp[-2]
