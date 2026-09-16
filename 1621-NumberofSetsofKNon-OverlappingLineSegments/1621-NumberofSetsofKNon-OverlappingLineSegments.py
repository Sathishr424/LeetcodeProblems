# Last updated: 9/16/2026, 4:22:09 PM
1class Solution:
2    def numberOfSets(self, n: int, k: int) -> int:
3        mod = 10**9 + 7
4
5        @cache
6        def rec(index, rem, start):
7            if rem == 0 and not start:
8                return 1
9            if index == n: return 0
10
11            ans = rec(index + 1, rem, start)
12            if start:
13                ans += rec(index + 1, rem, False)
14                if rem:
15                    ans += rec(index + 1, rem - 1, True)
16            elif not start and rem:
17                ans += rec(index + 1, rem - 1, True)
18            return ans % mod
19
20        ret = rec(0, k, False)
21        rec.cache_clear()
22        return ret