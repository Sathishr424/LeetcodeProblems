# Last updated: 8/5/2026, 11:43:04 AM
1class Solution:
2    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
3        graph = defaultdict(list)
4
5        for u, v in invocations:
6            graph[u].append(v)
7
8        sus = set()
9        vis = set()
10        def rec(x):
11            if x in sus: return True
12            if x in vis: return False
13            vis.add(x)
14            for y in graph[x]:
15                if rec(y): return True
16
17            return False
18
19        rec(k)
20        sus = vis
21        vis = set()
22
23        for x in range(n):
24            if x not in sus:
25                if rec(x): return [i for i in range(n)]
26
27        return [i for i in range(n) if i not in sus]