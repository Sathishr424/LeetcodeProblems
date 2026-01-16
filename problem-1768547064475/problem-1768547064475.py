# Last updated: 1/16/2026, 12:34:24 PM
1class Solution:
2    def residuePrefixes(self, s: str) -> int:
3        uniq = set()
4        ret = 0
5        for i, char in enumerate(s):
6            uniq.add(char)
7
8            ret += (i + 1) % 3 == len(uniq)
9
10        return ret