# Last updated: 30/11/2025, 8:06:04 am
1class Solution:
2    def maxDistinct(self, s: str) -> int:
3        n = len(s)
4        used = set()
5        split = 0
6        for i in range(n):
7            if s[i] not in used:
8                used.add(s[i])
9                split += 1
10
11        return split