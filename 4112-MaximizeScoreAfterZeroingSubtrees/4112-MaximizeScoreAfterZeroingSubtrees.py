# Last updated: 11/15/2026, 5:59:53 PM
1class Solution:
2    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
3        n = len(parent)
4
5        graph = [[] for _ in range(n)]
6        for i in range(1, n):
7            graph[parent[i]].append(i)
8
9        def dfs(x):
10            if len(graph[x]) == 0: return score[x]
11            mn = inf
12            tot = score[x]
13            for y in graph[x]:
14                curr = dfs(y)
15                mn = min(mn, curr)
16                tot += curr
17                
18            if op[x]:
19                return tot - mn
20            else:
21                return max(tot, tot - mn)
22
23        return dfs(0)