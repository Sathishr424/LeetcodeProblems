# Last updated: 11/1/2026, 1:57:13 AM
1class Solution:
2    def maximumGap(self, skill_: str, station_: str) -> int:
3        m = len(skill_)
4        n = len(station_)
5
6        skill = [ord(c) - ord('a') for c in skill_]
7        station = [ord(c) - ord('a') for c in station_]
8        best = 0
9
10        indexes = [deque() for _ in range(26)]
11        for i, c in enumerate(station):
12            indexes[c].append(i)
13
14        earliest = []
15        prev = -1
16        for i, c in enumerate(skill):
17            while indexes[c][0] <= prev:
18                indexes[c].popleft()
19            earliest.append(indexes[c].popleft())
20            prev = earliest[i]
21
22        indexes = [[] for _ in range(26)]
23        for i, c in enumerate(station):
24            indexes[c].append(i)
25
26        latest = [0] * m
27        prev = n
28        for i in range(m-1, -1, -1):
29            c = skill[i]
30            while indexes[c][-1] > prev:
31                indexes[c].pop()
32            latest[i] = indexes[c].pop()
33            prev = latest[i]
34            if i > 0: best = max(best, latest[i] - earliest[i-1])
35        # print(earliest)
36        # print(latest)
37        return best