# Last updated: 9/6/2026, 5:57:42 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m = len(s)
4        n = len(t)
5
6        if n > m: return 0
7
8        @cache
9        def rec(i, j):
10            if j == n: return 1
11            if i == m: return 0
12
13            ans = rec(i + 1, j)
14            if s[i] == t[j]:
15                ans += rec(i + 1, j + 1)
16
17            return ans
18
19        ans = rec(0, 0)
20        rec.cache_clear()
21        return ans