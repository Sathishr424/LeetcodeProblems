# Last updated: 1/12/2025, 3:04:05 pm
1class Solution:
2    def maxRunTime(self, n: int, batteries: List[int]) -> int:
3        def isGood(mid):
4            s = 0
5            for bat in batteries:
6                s += min(bat, mid)
7            
8            return s // mid >= n
9
10        l = 1
11        r = sum(batteries)
12
13        while l <= r:
14            mid = (l + r) // 2
15
16            if isGood(mid):
17                l = mid + 1
18            else:
19                r = mid - 1
20
21        return r