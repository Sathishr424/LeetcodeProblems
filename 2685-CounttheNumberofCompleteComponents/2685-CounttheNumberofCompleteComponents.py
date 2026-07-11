# Last updated: 7/11/2026, 6:33:01 AM
1class Solution:
2    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
3        graph = [set() for _ in range(n)]
4        for u, v in edges:
5            graph[u].add(v)
6            graph[v].add(u)
7
8        def dfs(x, vis):
9            vis.add(x)
10            visited.add(x)
11            for y in graph[x]:
12                if y not in vis:
13                    dfs(y, vis)
14
15        visited = set()
16        # print(graph)
17        ans = 0
18        for i in range(n):
19            if i in visited: continue
20            curr = set()
21            dfs(i, curr)
22            # print(i, curr)
23
24            for x in curr:
25                if len(graph[x]) != len(curr) - 1: break
26            else:
27                ans += 1
28
29        return ans