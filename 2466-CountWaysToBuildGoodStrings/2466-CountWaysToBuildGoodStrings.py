# Last updated: 27/9/2025, 7:31:26 pm
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        @cache
        def rec(rem):
            if rem < min(one, zero): 
                return 1
            ans = 1
            if rem >= one:
                ans += rec(rem - one)
            if rem >= zero:
                ans += rec(rem - zero)
            return ans % mod

        right = rec(high)
        left = rec(low - 1)
        rec.cache_clear()
        return (right - left) % mod