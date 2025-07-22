# Last updated: 23/7/2025, 12:45:22 am
inf = 101
cmin = lambda x, y: x if x < y else y
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        @cache
        def rec(l, r):
            if l > r: return 0
            if l == r: return 1

            l += 1
            while l < r and s[l] == s[l - 1]:
                l += 1

            ans = inf
            for i in range(l, r + 1):
                if s[i] == s[l - 1]:
                    left = rec(l, i - 1)
                    right = rec(i, r)
                    ans = cmin(ans, left + right)
            
            ans = cmin(ans, rec(l, r) + 1)
            return ans
        
        ret = rec(0, n-1)
        rec.cache_clear()
        return ret