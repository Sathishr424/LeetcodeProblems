# Last updated: 12/6/2025, 5:43:27 am
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [1 for _ in range(n+1)]
        dp[0] = 0
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
        