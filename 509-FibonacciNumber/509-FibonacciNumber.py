# Last updated: 28/9/2025, 9:14:58 pm
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n]