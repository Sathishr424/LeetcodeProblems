# Last updated: 11/6/2026, 2:45:29 PM
1class Solution:
2    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
3        window = defaultdict(lambda: set())
4        for s, t in logs:
5            window[t].add(s)
6
7        ans = [0] * len(queries)
8        ans_index = {}
9        for i, t in enumerate(queries):
10            ans_index[t] = i
11
12        times = sorted(set(list(window.keys()) + queries))
13
14        freq = [0] * (n + 1)
15        sub = [defaultdict(int) for _ in range(len(times) + 1)]
16        cnt = 0
17        for i, t in enumerate(times):
18            for s in window[t]:
19                freq[s] += 1
20                if freq[s] == 1: cnt += 1
21
22            for s in sub[i]:
23                freq[s] -= sub[i][s]
24                if freq[s] == 0: cnt -= 1
25
26            next = bisect_left(times, t + x + 1)
27            for s in window[t]:
28                sub[next][s] += 1
29
30            if t in ans_index:
31                ans[ans_index[t]] = n - cnt
32        return ans