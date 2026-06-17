# Last updated: 6/17/2026, 9:54:14 PM
1from typing import List
2
3class Solution:
4    def generateValidStrings(self, n: int, k: int) -> list[str]:
5        ans = []
6        def rec(index, st, cost):
7            if index == n:
8                ans.append(st)
9                return
10
11            if cost + index <= k and (len(st) == 0 or st[-1] != '1'):
12                rec(index + 1, st + "1", cost + index)
13            rec(index + 1, st + "0", cost)
14
15        rec(0, "", 0)
16        return ans
17