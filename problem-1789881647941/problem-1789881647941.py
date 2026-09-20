# Last updated: 9/20/2026, 10:50:47 AM
1class Solution:
2    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
3        intervals.sort()
4
5        sl = SortedList()
6        ans = 0
7        for l, r in intervals:
8            left = sl.bisect_left(l)
9            ans += len(sl) - left
10            sl.add(r)
11
12        return ans