# Last updated: 5/8/2025, 12:17:50 am
class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def rec(l, r):
            if l >= r: return 1

            ans = 0
            for i in range(l, r):
                ans += rec(l, i) * rec(i + 1, r)
            return ans
        
        return rec(1, n + 1)

