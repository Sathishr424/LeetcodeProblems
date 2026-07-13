# Last updated: 7/13/2026, 11:57:18 AM
1class Solution:
2    def sequentialDigits(self, low: int, high: int) -> List[int]:
3        ret = []
4        def rec(curr, prev):
5            if curr > high: return
6            if curr >= low:
7                ret.append(curr)
8
9            if prev < 9:
10                rec(curr * 10 + (prev + 1), prev + 1)
11
12        for i in range(1, 10):
13            rec(i, i)
14        return sorted(ret)