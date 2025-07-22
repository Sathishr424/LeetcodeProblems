# Last updated: 23/7/2025, 12:44:30 am
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
                    ans = min(ans, left + right)
            
            ans = min(ans, rec(l, r) + 1)
            return ans
        
        ret = rec(0, n-1)
        rec.cache_clear()
        return ret