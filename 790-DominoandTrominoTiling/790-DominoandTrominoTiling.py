# Last updated: 5/5/2025, 12:15:38 pm
mod = 10**9 + 7
# [2, 1, 3, 3, 4, 4], (6, 8, 10, 12, 14, 18, ....) (vertival and horizontal)
# (5, 7, 9, 11, ....) (vertival and horizontal)

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1]
            dp[i] = (dp[i] + dp[i-2]) % mod
            
            for num in range(3, i+1):
                dp[i] = (dp[i] + (dp[i-num] * 2 % mod)) % mod

        return dp[n]