# Last updated: 10/11/2026, 8:09:41 AM
1class Solution:
2    def threeFibonacciSum(self, n: int) -> bool:
3        if n == 1: return False
4        def rec(first, second):
5            third = first + second
6            tot = first + second + third
7            if tot > n: return False
8            if tot == n: return True
9            return rec(second, third)
10
11        return rec(0, 1)