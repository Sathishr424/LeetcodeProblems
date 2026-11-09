# Last updated: 11/9/2026, 11:04:53 PM
1class Solution:
2    def countValidSubstrings(self, s: str) -> int:
3        n = len(s)
4
5        total = 0
6        window = 0
7        for i in range(n):
8            if i >= 2 and s[i-2:i + 1] == 'abc':
9                window = 2
10            else:
11                window += 1
12            total += window
13
14        return total