# Last updated: 8/8/2025, 6:38:19 pm
class Solution:
    def soupServings(self, n: int) -> float:
        n = ceil(n / 25)
        if n > 200: return 1
        @cache
        def rec(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0

            i = rec(a-4, b)
            j = rec(a-3, b-1)
            k = rec(a-2, b-2)
            l = rec(a-1, b-3)
            ans = 0.25 * (i + j + k + l)
            return ans
        
        return rec(n, n)