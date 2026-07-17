# Last updated: 7/17/2026, 6:58:59 PM
1class Solution:
2    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
3        mod = 10**9 + 7
4        LCM = lcm(a, b)
5
6        def getCnt(x, y, cnt):
7            val = x * cnt
8
9            y_cnt = val // y
10            lcm_cnt = val // LCM
11
12            return cnt + (y_cnt - lcm_cnt)
13
14        def getIndex(x, y):
15            l = 1
16            r = n
17            while l < r:
18                mid = (l + r) // 2
19                tot = getCnt(x, y, mid)
20    
21    
22                if tot >= n:
23                    r = mid
24                else:
25                    l = mid + 1
26            return l
27
28        index = getIndex(a, b)
29        if getCnt(a, b, index) == n: return index * a % mod
30        return getIndex(b, a) * b % mod