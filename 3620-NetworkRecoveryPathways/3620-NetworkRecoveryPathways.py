# Last updated: 7/3/2026, 4:10:20 PM
1inf = 10**20
2class Solution:
3    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
4        n = len(online)
5
6        graph = [[] for _ in range(n)]
7        l = -1
8        r = -1
9        for u, v, c in edges:
10            if online[u] and online[v]:
11                graph[u].append((v, c))
12                r = max(r, c)
13        
14        for x in range(n):
15            graph[x].sort(key=lambda y: y[1])
16
17        def isGood(target):
18            dis = [-inf] * n
19            stack = [(-k, 0)]
20
21            while stack:
22                rem, x = heappop(stack)
23                if x == n-1: return True
24                rem = -rem
25                if dis[x] >= rem: continue
26                dis[x] = rem
27
28                for y, c in graph[x]:
29                    if c < target or c > rem: continue
30                    heappush(stack, (-(rem - c), y))
31
32            return False
33            
34        while l < r:
35            mid = (l + r + 1) // 2
36
37            if isGood(mid):
38                l = mid
39            else:
40                r = mid - 1
41
42        return l
43