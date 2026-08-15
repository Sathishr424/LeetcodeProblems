# Last updated: 8/16/2026, 12:00:18 AM
1class Solution:
2    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
3        direction = [(-1, 0, 0), (0, 1, 1), (1, 0, 1), (0, -1, 0)]
4        inf = 10**20
5        heap = [(1, 1, 0, 0)]
6
7        dis = [[[inf, inf] for _ in range(n)] for _ in range(m)]
8        dis[0][0][1] = 1
9
10        while heap:
11            cost, odd, i, j = heappop(heap)
12
13            if i == m-1 and j == n-1:
14                return cost
15
16            new_is_odd = odd ^ 1
17
18            for i2, j2, match in direction:
19                i2 += i
20                j2 += j
21                new_cost = cost + (i2 + 1) * (j2 + 1)
22                pen_cost = new_cost + penalty[i][j]
23
24                if 0 <= i2 < m and 0 <= j2 < n:
25                    if pen_cost < dis[i2][j2][odd]:
26                        if match != new_is_odd:
27                            pen_cost += penalty[i][j]
28                        heappush(heap, (pen_cost, odd, i2, j2))
29                        dis[i2][j2][odd] = pen_cost
30
31                    if match != odd: 
32                        new_cost = new_cost + penalty[i][j]
33
34                    if new_cost < dis[i2][j2][new_is_odd]:
35                        heappush(heap, (new_cost, new_is_odd, i2, j2))
36                        dis[i2][j2][new_is_odd] = new_cost
37        return -1