# Last updated: 7/7/2026, 2:46:43 PM
1class Solution:
2    def sumAndMultiply(self, n: int) -> int:
3        sum = 0
4        x = 0
5        power = 0
6        num = n
7
8        while num:
9            d = num % 10
10            if d > 0:
11                x = d * (10 ** power) + x
12                power += 1
13                sum += d
14            num //= 10
15
16        return x * sum