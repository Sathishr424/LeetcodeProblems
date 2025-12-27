# Last updated: 12/28/2025, 12:58:35 AM
1class Solution:
2    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
3        graph = [[] for _ in range(n)]
4        for u, v in edges:
5            graph[u].append(v)
6            graph[v].append(u)
7        
8        freq = defaultdict(int)
9        for g in group:
10            freq[g] += 1
11        
12        ans = 0
13        def dfs(x, par, g):
14            nonlocal ans
15            bottom = 0
16            if group[x] == g: bottom += 1
17            for y in graph[x]:
18                if y == par: continue
19                bottom += dfs(y, x, g)
20            
21            top = freq[g] - bottom
22            ans += top * bottom
23
24            return bottom
25        
26        for g in freq:
27            dfs(0, -1, g)
28        
29        return ans
30
31            
32        