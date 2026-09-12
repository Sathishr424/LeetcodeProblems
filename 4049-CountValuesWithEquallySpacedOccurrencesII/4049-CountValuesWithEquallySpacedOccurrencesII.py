# Last updated: 9/12/2026, 11:01:24 PM
1INF = 10**20
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
12@cache
13def rec(rem):
14    if rem == 0: return 0
15    index = bisect_right(prefix, rem)
16    ans = rec(rem - prefix[index-1]) + index
17    return ans + 1
18
19class Solution:
20    def minDays(self, n: int) -> int:
21        index = bisect_right(prefix, n)
22
23        best = INF
24        for i in range(index):
25            best = min(best, rec(n - prefix[i]) + i + 1)
26
27        return int(best)
28