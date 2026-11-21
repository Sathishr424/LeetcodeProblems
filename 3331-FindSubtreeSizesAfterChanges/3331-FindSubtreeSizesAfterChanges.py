# Last updated: 11/21/2026, 9:43:03 PM
1class Solution:
2    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
3        n = len(parent)
4
5        graph = [[] for _ in range(n)]
6        for i in range(1, n):
7            graph[parent[i]].append(i)
8
9        def dfs(node: int, anc):
10            if s[node] in anc:
11                parent[node] = anc[s[node]]
12            anc[s[node]] = node
13
14            for y in graph[node]:
15                dfs(y, dict.copy(anc))
16
17        dfs(0, {})
18
19        counts = [0] * n
20        def countSubTree(node):
21            cnt = 1
22            for y in graph[node]:
23                cnt += countSubTree(y)
24            counts[node] = cnt
25            return cnt
26
27        graph = [[] for _ in range(n)]
28        for i in range(1, n):
29            graph[parent[i]].append(i)
30
31        countSubTree(0)
32        return counts