# Last updated: 11/6/2026, 2:43:02 PM
1class Solution:
2    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
3        window = defaultdict(lambda: set())
4        for s, t in logs:
5            window[t].add(s)
6
7        queries_map = {}
8        for i, t in enumerate(queries):
9            queries_map[t] = i
10        ans = []
11        times = sorted(set(list(window.keys()) + queries))
12
13        freq = [0] * (n + 1)
14        sub = [defaultdict(int) for _ in range(len(times) + 1)]
15        cnt = 0
16        for i, t in enumerate(times):
17            for s in window[t]:
18                freq[s] += 1
19                if freq[s] == 1: cnt += 1
20
21            for s in sub[i]:
22                freq[s] -= sub[i][s]
23                if freq[s] == 0: cnt -= 1
24
25            next = bisect_left(times, t + x + 1)
26            for s in window[t]:
27                sub[next][s] += 1
28
29            if t in queries_map:
30                ans.append((queries_map[t], n - cnt))
31        ans.sort()
32        return [c for _, c in ans]