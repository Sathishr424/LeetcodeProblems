# Last updated: 12/19/2025, 1:58:48 PM
1class Solution:
2    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
3        relations = [[] for _ in range(n)]
4        for x, y, t in meetings:
5            relations[x].append((t, y))
6            relations[y].append((t, x))
7
8        for i in range(n):
9            relations[i].sort()
10
11        heap = relations[firstPerson] + relations[0]
12        heapq.heapify(heap)
13        ret = set()
14        ret.add(0)
15        ret.add(firstPerson)
16        while heap:
17            t, y = heapq.heappop(heap)
18            ret.add(y)
19            while len(relations[y]) > 0 and relations[y][-1][0] >= t:
20                tmp = relations[y].pop()
21                heapq.heappush(heap, tmp)
22
23        return list(ret)
24
25