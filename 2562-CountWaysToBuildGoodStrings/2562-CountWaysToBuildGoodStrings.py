# Last updated: 12/6/2025, 5:37:40 am
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = (10**9) + 7
        dp = [0] * (high+1)
        dp[0] = 1
        for i in range(high+1):
            if i >= zero:
                dp[i] += dp[i-zero]
            if i >= one:
                dp[i] += dp[i-one]
            dp[i] %= mod
            
        return sum(dp[low:]) % mod