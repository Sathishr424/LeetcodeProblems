# Last updated: 11/6/2026, 3:15:28 PM
1class Solution:
2    def countServersSortedList(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
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
29
30        
31    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
32        window = defaultdict(lambda: set())
33        for s, t in logs:
34            window[t].add(s)
35
36        ans = [0] * len(queries)
37        ans_index = {}
38        for i, t in enumerate(queries):
39            ans_index[t] = i
40
41        times = sorted(set(list(window.keys()) + queries))
42
43        freq = [0] * (n + 1)
44        sub = [defaultdict(int) for _ in range(len(times) + 1)]
45        cnt = 0
46        for i, t in enumerate(times):
47            for s in window[t]:
48                freq[s] += 1
49                if freq[s] == 1: cnt += 1
50
51            for s in sub[i]:
52                freq[s] -= sub[i][s]
53                if freq[s] == 0: cnt -= 1
54
55            next = bisect_left(times, t + x + 1)
56            for s in window[t]:
57                sub[next][s] += 1
58
59            if t in ans_index:
60                ans[ans_index[t]] = n - cnt
61        return ans