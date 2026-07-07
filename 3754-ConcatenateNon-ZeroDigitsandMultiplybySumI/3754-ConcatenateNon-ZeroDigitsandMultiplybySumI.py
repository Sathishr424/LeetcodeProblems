# Last updated: 7/7/2026, 2:46:58 PM
1class Solution:
2    def sumAndMultiply(self, num: int) -> int:
3        sum = 0
4        x = 0
5        power = 0
6
7        while num:
8            d = num % 10
9            if d > 0:
10                x = d * (10 ** power) + x
11                power += 1
12                sum += d
13            num //= 10
14
15        return x * sum