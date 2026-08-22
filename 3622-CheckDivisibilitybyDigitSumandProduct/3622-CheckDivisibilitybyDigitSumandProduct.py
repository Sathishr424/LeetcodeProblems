# Last updated: 8/22/2026, 12:39:45 PM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        orig = n
4        x = 0
5        y = 1
6        while n:
7            rem = n % 10
8            x += rem
9            y *= rem
10            n //= 10
11
12        return orig % (x + y) == 0