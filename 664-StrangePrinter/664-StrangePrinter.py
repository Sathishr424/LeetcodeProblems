# Last updated: 23/7/2025, 12:42:49 am
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)

        @cache
        def rec(l, r):
            if l > r: return 0
            if l == r: return 1

            ans = inf
            for i in range(l + 1, r + 1):
                if s[i] == s[l]:
                    left = rec(l + 1, i - 1)
                    right = rec(i, r)
                    ans = min(ans, left + right)
            
            ans = min(ans, rec(l + 1, r) + 1)
            return ans
        
        return rec(0, n-1)