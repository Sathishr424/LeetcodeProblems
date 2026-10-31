# Last updated: 11/1/2026, 2:04:29 AM
1class Solution:
2    def maximumGap(self, skill_: str, station_: str) -> int:
3        m = len(skill_)
4        n = len(station_)
5
6        skill = [ord(c) - ord('a') for c in skill_]
7        station = [ord(c) - ord('a') for c in station_]
8        best = 0
9
10        indexes = [[] for _ in range(26)]
11        for i, c in enumerate(station):
12            indexes[c].append(i)
13
14        earliest = []
15        prev = -1
16        index = [0] * 26
17        for i, c in enumerate(skill):
18            j = index[c]
19            while indexes[c][j] <= prev:
20                j += 1
21            earliest.append(indexes[c][j])
22            prev = earliest[i]
23            index[c] = j + 1
24
25        prev = n
26        for i in range(m-1, -1, -1):
27            c = skill[i]
28            while indexes[c][-1] > prev:
29                indexes[c].pop()
30            curr = indexes[c].pop()
31            if i > 0: best = max(best, curr - earliest[i-1])
32            prev = curr
33
34        return best