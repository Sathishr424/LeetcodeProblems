# Last updated: 11/24/2026, 6:48:26 PM
1class Solution:
2    def earliestActivationTimes(self, n: int, edges: list[list[int]], requiredSignals: list[int]) -> list[int]:
3        graph = [[] for _ in range(n)]
4        requiredSignals[0] = 1
5
6        for u, v, delay in edges:
7            graph[u].append((v, delay))
8
9        heap = [(0, 0)]
10        ans = [-1] * n
11        received = [0] * n
12
13        while heap:
14            t, u = heapq.heappop(heap)
15            if received[u] == requiredSignals[u]: continue
16            
17            received[u] += 1
18            if received[u] == requiredSignals[u]:
19                ans[u] = t
20                for v, delay in graph[u]:
21                    if ans[v] == -1:
22                        heapq.heappush(heap, (t + delay, v))
23
24        return ans