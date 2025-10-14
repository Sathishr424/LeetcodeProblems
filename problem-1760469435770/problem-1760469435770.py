# Last updated: 15/10/2025, 12:47:15 am
class Solution:
    def distinctIntegers(self, n: int) -> int:
        cache = {}
        def rec(n):
            if n in cache: return 0
            cache[n] = 1
            ans = 1
            for i in range(1, n):
                if n % i == 1:
                    ans += rec(i)

            return ans

        return rec(n)