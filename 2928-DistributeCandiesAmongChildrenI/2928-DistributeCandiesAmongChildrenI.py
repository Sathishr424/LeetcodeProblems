# Last updated: 22/6/2025, 7:48:13 am
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # *****
        limit += 1
        @cache
        def rec(k, rem):
            if k == 0:
                if rem == 0: return 1
                return 0
            ans = 0
            for c in range(limit):
                ans += rec(k-1, rem-c)
            return ans

        return rec(3, n)
