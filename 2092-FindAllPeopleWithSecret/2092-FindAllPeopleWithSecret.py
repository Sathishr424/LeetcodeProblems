# Last updated: 12/19/2025, 1:56:40 PM
1class Solution:
2    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
3
4        heaps = [[] for _ in range(n)]
5        for x, y, t in meetings:
6            heaps[x].append((t, y))
7            heaps[y].append((t, x))
8
9        for i in range(n):
10            heaps[i].sort()
11
12        heap = heaps[firstPerson] + heaps[0]
13        heapq.heapify(heap)
14        ret = set()
15        ret.add(0)
16        ret.add(firstPerson)
17        while heap:
18            t, y = heapq.heappop(heap)
19            ret.add(y)
20            while len(heaps[y]) > 0 and heaps[y][-1][0] >= t:
21                tmp = heaps[y].pop()
22                heapq.heappush(heap, tmp)
23
24        return list(ret)
25
26