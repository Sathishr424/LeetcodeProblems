# Last updated: 1/4/2026, 3:18:56 PM
1class Solution:
2    def largestEven(self, s: str) -> str:
3        while len(s) > 0 and s[-1] == '1':
4            s = s[:-1]
5
6        return s