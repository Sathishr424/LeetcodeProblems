# Last updated: 11/18/2026, 2:09:38 PM
1class Solution:
2    def minChanges(self, s: str) -> int:
3        n = len(s)
4
5        @cache
6        def rec(index, one, odd):
7            if index == n: return 0
8            add = s[index] != '1' if one else s[index] != '0'
9            ans = rec(index + 1, one, odd ^ 1)
10
11            if not odd:
12                ans = min(ans, rec(index + 1, True, 1), rec(index + 1, False, 1))
13
14            return ans + add
15
16        ans = min(rec(0, True, 1), rec(0, False, 1))
17        rec.cache_clear()
18        return ans