# Last updated: 9/12/2026, 8:21:51 PM
1inf = 10**20
2prefix = []
3s = 1
4N = 10**5
5curr = 1
6
7while s <= N:
8    prefix.append(s)
9    curr += 1
10    s += curr
11
12class Solution:
13    def minDays(self, n: int) -> int:
14        @cache
15        def rec(rem):
16            if rem == 0: return 0
17            index = bisect_right(prefix, rem)
18            ans = rec(rem - prefix[index-1]) + index
19            return ans + 1
20
21        index = bisect_right(prefix, n)
22
23        best = inf
24        for i in range(index):
25            best = min(best, rec(n - prefix[i]) + i + 1)
26
27        return int(best)
28