# Last updated: 8/5/2026, 11:42:26 AM
1class Solution:
2    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
3        graph = defaultdict(list)
4
5
6        for u, v in invocations:
7            graph[u].append(v)
8
9        sus = set()
10        vis = set()
11        def rec(x):
12            if x in sus: return True
13            if x in vis: return False
14            vis.add(x)
15            for y in graph[x]:
16                if rec(y): return True
17
18            return False
19
20        rec(k)
21        sus = vis
22        vis = set()
23
24        for x in range(n):
25            if x not in sus:
26                if rec(x): return [i for i in range(n)]
27
28        return [i for i in range(n) if i not in sus]