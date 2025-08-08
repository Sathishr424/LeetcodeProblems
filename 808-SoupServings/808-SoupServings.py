# Last updated: 8/8/2025, 6:36:47 pm
class Solution:
    def soupServings(self, n: int) -> float:
        n = ceil(n / 25)
        if n > 200: return 1
        @cache
        def rec(a, b):
            if a == 0 and b == 0:
                return 0.5
            if a == 0:
                return 1
            if b == 0:
                return 0

            i = rec(max(0, a-4), b)
            j = rec(max(0, a-3), max(0, b-1))
            k = rec(max(0, a-2), max(0, b-2))
            l = rec(max(0, a-1), max(0, b-3))
            ans = 0.25 * (i + j + k + l)
            return ans
        
        return rec(n, n)