# Last updated: 8/5/2026, 11:46:00 AM
1class Solution:
2    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
3        graph = defaultdict(list)
4
5        for u, v in invocations:
6            graph[u].append(v)
7
8        vis = [0] * n
9        sus = [0] * n
10        def rec(x):
11            if sus[x]: return True
12            if vis[x]: return False
13            vis[x] = 1
14            for y in graph[x]:
15                if rec(y): return True
16
17            return False
18
19        rec(k)
20        sus, vis = vis, sus
21
22        for x in range(n):
23            if sus[x] == 0:
24                if rec(x): return [i for i in range(n)]
25
26        return [i for i in range(n) if sus[i] == 0]