# Last updated: 10/31/2026, 8:31:49 PM
1class Solution:
2    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
3        inf = 10**9
4        graph = [[] for _ in range(n)]
5        labels = [ord(c) - ord('a') for c in labels]
6        for u, v, w in edges:
7            graph[u].append((v, w))
8
9        # Weight, cnt, prev_character, node
10        stack = [(0, 1, labels[0], 0)]
11        dis = [[[inf] * (k + 1) for _ in range(26)] for _ in range(n)]
12        dis[0][labels[0]][1] = 0
13
14        while stack:
15            curr_w, cnt, prev_c, u = heapq.heappop(stack)
16            if u == n-1: return curr_w
17
18            for v, w in graph[u]:
19                new_w = curr_w + w
20                new_cnt = 1
21                c = labels[v]
22                if c == prev_c:
23                    new_cnt += cnt
24                if new_cnt <= k and new_w < dis[v][c][new_cnt]:
25                    heapq.heappush(stack, (new_w, new_cnt, c, v))
26                    dis[v][c][new_cnt] = new_w
27
28        return -1