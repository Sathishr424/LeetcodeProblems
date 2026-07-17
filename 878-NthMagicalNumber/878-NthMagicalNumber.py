# Last updated: 7/17/2026, 7:07:24 PM
1class Solution:
2    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
3        mod = 10**9 + 7
4        LCM = lcm(a, b)
5
6        def getCnt(val):
7            x_cnt = val // a
8            y_cnt = val // b
9            lcm_cnt = val // LCM
10
11            return x_cnt + (y_cnt - lcm_cnt)
12
13        l = 1
14        r = min(a, b) * n
15
16        while l < r:
17            mid = (l + r) // 2
18
19            cnt = getCnt(mid)
20
21            if cnt >= n:
22                r = mid
23            else:
24                l = mid + 1
25        
26        return l % mod