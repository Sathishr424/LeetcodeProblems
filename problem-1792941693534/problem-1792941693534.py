# Last updated: 10/25/2026, 8:51:33 PM
1class Solution:
2    def countMagicalPairs(self, s: str) -> int:
3        n = len(s)
4        s = [ord(c) - ord('a') for c in s]
5
6        ans = 0
7        there = [[0] * 27 for _ in range(n)]
8        for i in range(n):
9            uniq = set()
10            for j in range(i, n):
11                uniq.add(s[j])
12                cnt = len(uniq)
13
14                if i > 0: ans += there[i-1][cnt]
15                there[j][cnt] += 1
16
17        return ans