# Last updated: 5/2/2026, 10:42:15 PM
1class Solution:
2    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
3        n = len(nums)
4        total = 0
5        graph = [[] for _ in range(n)]
6        for u, v in edges:
7            graph[u].append(v)
8            graph[v].append(u)
9
10        def dfs(x, vis):
11            vis.remove(x)
12            for y in graph[x]:
13                if y in vis:
14                    dfs(y, vis)
15
16        for mask in range(1 << n):
17            nodes = set()
18            node = -1
19            s = 0
20            for p in range(n):
21                if mask & (1 << p):
22                    nodes.add(p)
23                    node = p
24                    s += nums[p]
25
26            if len(nodes) == 0 or s % 2: continue
27            dfs(node, nodes)
28            if len(nodes) == 0: total += 1
29
30        return total