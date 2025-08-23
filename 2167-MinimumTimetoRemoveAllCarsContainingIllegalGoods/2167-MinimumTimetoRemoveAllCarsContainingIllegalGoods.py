# Last updated: 24/8/2025, 1:56:47 am
class Solution:
    def minimumTime(self, s: str) -> int:
        n = len(s)

        right = [0] * n
        r = 0
        add = 0
        for i in range(n-1, -1, -1):
            add += 1
            if s[i] == '1':
                r += add
                add = 0
            right[i] = r

        @cache
        def rec(index):
            if index == n: return 0

            if s[index] == '1':
                return min(right[index], 2 + rec(index + 1))
            else:
                return rec(index + 1)
        
        l = 0
        add = 0
        ans = inf
        for i in range(n):
            ans = min(ans, l + rec(i))
            add += 1
            if s[i] == '1':
                l += add
                add = 0
        
        rec.cache_clear()
        return ans