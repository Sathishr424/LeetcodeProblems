# Last updated: 8/9/2026, 7:11:18 PM
1class Solution:
2    def maximumValue(self, n: int, s: int, m: int) -> int:
3        if n == 1: return s
4        half = n // 2 + 1
5        left = m * half + (s - m)
6        return left - (n - half) + (n % 2)