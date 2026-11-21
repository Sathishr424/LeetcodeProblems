# Last updated: 11/21/2026, 9:54:51 PM
1class Solution:
2    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
3        n = len(parent)
4        s = [ord(c) - ord('a') for c in s]
5
6        graph = [[] for _ in range(n)]
7        for i in range(1, n):
8            graph[parent[i]].append(i)
9
10        def dfs(node: int, anc):
11            if anc[s[node]] != -1:
12                parent[node] = anc[s[node]]
13
14            prev = anc[s[node]] 
15            anc[s[node]] = node
16
17            for y in graph[node]:
18                dfs(y, anc)
19                
20            anc[s[node]] = prev
21        
22        dfs(0, [-1] * 26)
23
24        counts = [0] * n
25        def countSubTree(node):
26            cnt = 1
27            for y in graph[node]:
28                cnt += countSubTree(y)
29            counts[node] = cnt
30            return cnt
31
32        graph = [[] for _ in range(n)]
33        for i in range(1, n):
34            graph[parent[i]].append(i)
35
36        countSubTree(0)
37        return counts