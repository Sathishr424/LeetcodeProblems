# Last updated: 10/25/2026, 10:00:05 PM
1class Solution:
2    def countMagicalPairs(self, s: str) -> int:
3        n = len(s)
4
5        ans = 0
6        there = [[0] * 27 for _ in range(n + 1)]
7        for i in range(n):
8            uniq = set()
9            for j in range(i, n):
10                uniq.add(s[j])
11                cnt = len(uniq)
12
13                ans += there[i-1][cnt]
14                there[j][cnt] += 1
15
16        return ans