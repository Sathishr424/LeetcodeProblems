# Last updated: 6/7/2026, 2:58:47 PM
1from typing import List
2
3class Solution:
4    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
5        need = ceil(brightness / 3)
6
7        intervals.sort()
8
9        curr = intervals[0]
10        ans = 0
11
12        for l, r in intervals[1:]:
13            if l <= curr[1]:
14                curr[1] = max(r, curr[1])
15            else:
16                ans += (curr[1] - curr[0] + 1) * need
17                curr = [l, r]
18
19        ans += (curr[1] - curr[0] + 1) * need
20        return ans
21