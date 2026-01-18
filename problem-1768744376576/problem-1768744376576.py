# Last updated: 1/18/2026, 7:22:56 PM
1class Solution:
2    def vowelConsonantScore(self, s: str) -> int:
3        v = 0
4        c = 0
5        for char in s:
6            if char in 'aeiou':
7                v += 1
8            elif ord(char) >= ord('a') and ord(char) <= ord('z'):
9                c += 1
10
11        if c == 0: return 0
12        return v // c