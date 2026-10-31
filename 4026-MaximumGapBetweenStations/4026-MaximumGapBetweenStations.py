# Last updated: 11/1/2026, 1:58:55 AM
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
26        prev = n
27        for i in range(m-1, -1, -1):
28            c = skill[i]
29            while indexes[c][-1] >= prev:
30                indexes[c].pop()
31            curr = indexes[c].pop()
32            if i > 0: best = max(best, curr - earliest[i-1])
33            prev = curr
34
35        return best