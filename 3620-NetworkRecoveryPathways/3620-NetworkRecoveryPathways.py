# Last updated: 7/3/2026, 4:10:35 PM
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
14        def isGood(target):
15            dis = [-inf] * n
16            stack = [(-k, 0)]
17
18            while stack:
19                rem, x = heappop(stack)
20                if x == n-1: return True
21                rem = -rem
22                if dis[x] >= rem: continue
23                dis[x] = rem
24
25                for y, c in graph[x]:
26                    if c < target or c > rem: continue
27                    heappush(stack, (-(rem - c), y))
28
29            return False
30            
31        while l < r:
32            mid = (l + r + 1) // 2
33
34            if isGood(mid):
35                l = mid
36            else:
37                r = mid - 1
38
39        return l
40