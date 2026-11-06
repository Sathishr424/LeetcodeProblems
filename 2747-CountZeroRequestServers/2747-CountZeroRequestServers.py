# Last updated: 11/6/2026, 3:07:20 PM
1class Solution:
2    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
3        heap = [(t, s, 1) for s, t in logs]
4        for t in queries: heap.append((t, n + 1, 0))
5        heapq.heapify(heap)
6
7        ans = [0] * len(queries)
8        ans_index = {}
9        for i, t in enumerate(queries):
10            ans_index[t] = i
11
12        freq = [0] * (n + 2)
13        cnt = 0
14        while heap:
15            t, s, add = heapq.heappop(heap)
16
17            freq[s] += add
18
19            if add == 1:
20                if freq[s] == 1: cnt += 1
21                heapq.heappush(heap, (t + x + 1, s, -1))
22            elif add == -1:
23                if freq[s] == 0: cnt -= 1
24            elif add == 0:
25                if t in ans_index:
26                    ans[ans_index[t]] = n - cnt
27
28        return ans