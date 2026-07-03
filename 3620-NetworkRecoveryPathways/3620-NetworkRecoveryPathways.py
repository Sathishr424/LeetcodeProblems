# Last updated: 7/3/2026, 4:13:05 PM
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
19
20            stack = [(-k, 0)]
21            dis[0] = k
22
23            while stack:
24                rem, x = heappop(stack)
25                if x == n-1: return True
26                rem = -rem
27                if dis[x] > rem: continue
28
29                for y, c in graph[x]:
30                    if c < target or c > rem: continue
31                    new_rem = rem - c
32                    if new_rem > dis[y]:
33                        dis[y] = new_rem
34                        heappush(stack, (-new_rem, y))
35
36            return False
37            
38        while l < r:
39            mid = (l + r + 1) // 2
40
41            if isGood(mid):
42                l = mid
43            else:
44                r = mid - 1
45
46        return l