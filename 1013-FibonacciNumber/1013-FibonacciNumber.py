# Last updated: 12/6/2025, 5:44:51 am
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        dp = [0, 1]
        for i in range(2, n+1):
            dp = [dp[1], dp[0]+dp[1]]
        return dp[-1]
        