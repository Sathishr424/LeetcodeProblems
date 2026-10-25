# Last updated: 10/25/2026, 11:26:53 PM
1class Solution:
2    def calculateScore(self, a: int, b: int) -> int:
3        s1 = 0
4        s2 = 0
5
6        while a:
7            s1 += a & 1
8            a >>= 1
9
10        while b:
11            s2 += b & 1
12            b >>= 1
13
14        if s1 >= s2: return s1 * s2
15        return s2 // s1