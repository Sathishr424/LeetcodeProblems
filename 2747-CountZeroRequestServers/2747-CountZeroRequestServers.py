# Last updated: 11/6/2026, 3:04:14 PM
1class Solution:
2    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
3        heap = [(t, s, 1) for s, t in logs]
4        for t in queries: heap.append((t, n + 1, 2))
5        heapq.heapify(heap)
6
7        ans = [0] * len(queries)
8        ans_index = {}
9        for i, t in enumerate(queries):
10            ans_index[t] = i
11
12        freq = [0] * (n + 1)
13        cnt = 0
14        while heap:
15            t, s, add = heapq.heappop(heap)
16
17            if add != 2: 
18                freq[s] += add
19
20            if add == 1 and freq[s] == 1: cnt += 1
21            if add == -1 and freq[s] == 0: cnt -= 1
22
23            if add == 1: heapq.heappush(heap, (t + x + 1, s, -1))
24
25            if add == 2 and t in ans_index:
26                ans[ans_index[t]] = n - cnt
27
28        return ans